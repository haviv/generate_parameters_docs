import os
from pathlib import Path
import subprocess
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import sys

def find_param_references(code_folder: str, param_name: str) -> List[dict]:
    """
    Find all files containing references to the given parameter.
    Returns a list of dictionaries containing file paths and relevant code snippets.
    """
    results = []
    MAX_CONTEXT_LENGTH = 500  # Maximum characters per context
    CONTEXT_LINES = 10  # Number of lines before and after the match
    
    try:
        # Use grep to search for parameter references recursively in .cs files only
        param_name = param_name
        cmd = f'grep -r --include="*.cs" "{param_name}" {code_folder}'
        output = subprocess.check_output(cmd, shell=True, text=True)
        
        # Process grep output
        for line in output.splitlines():
            if ':' in line:
                file_path, content = line.split(':', 1)
                if os.path.isfile(file_path):
                    # Read the context around the matched line
                    with open(file_path, 'r') as f:
                        file_content = f.readlines()
                    
                    # Find the line number of the match
                    for i, line_content in enumerate(file_content):
                        if param_name in line_content:
                            # Get context (3 lines before and after)
                            start = max(0, i - CONTEXT_LINES)
                            end = min(len(file_content), i + CONTEXT_LINES + 1)
                            context = ''.join(file_content[start:end])
                            
                            # Truncate context if it's too long
                            if len(context) > MAX_CONTEXT_LENGTH:
                                context = context[:MAX_CONTEXT_LENGTH] + "..."
                            
                            results.append({
                                'file_path': file_path,
                                'context': context
                            })
                            
                            # Only take the first occurrence in each file to reduce context
                            break
    except subprocess.CalledProcessError:
        # No matches found
        pass
    
    # Limit the number of files if we found too many
    MAX_FILES = 5
    if len(results) > MAX_FILES:
        print(f"Found {len(results)} files, limiting to {MAX_FILES} for token management")
        results = results[:MAX_FILES]
    
    return results

def generate_param_documentation(param_name: str, references: List[dict]) -> str:
    """
    Generate documentation for a parameter using OpenAI API.
    """
    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI client with API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    # print("===========api_key", api_key)
    
    client = OpenAI(api_key=api_key)
    
    # Prepare the context from all references
    context = f"Parameter name: {param_name}\n\nCode references:\n\n"
    for ref in references:
        context += f"File: {ref['file_path']}\n```\n{ref['context']}\n```\n\n"
    
    # Create the prompt for OpenAI
    prompt = f"""Based on the following code references, generate comprehensive markdown documentation for the parameter '{param_name}'.
    go over the code and then understand what is the purposes of the param so you can create a documentation for end user that wants to use this param in this format. it has to be in markdown format - this is super important!
make sure you generate a valid markdown file. dont add ```markdown at the beginning or at the end of the file.
For context, these params are part of the Pathlock Cloud GRC platform. Pathlock is a cloud-based GRC platform that helps organizations manage their security, risk, and compliance.
When you give examples, make sure to give examples that are relevant to the business impact of the param.
    Generate the next format:
Category:
Default Value:
Impact Level:
Description:
Business Impact:
Technical Impact: when configured
Examples Scenario:
Related Settings:
Best Practices: configure when, avoid when 
Context:
{context}

Please format the response in Markdown."""

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a technical documentation expert. Generate clear, concise, and accurate documentation based on code analysis."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_doc(code_folder: str, param_names: List[str], output_folder: str):
    """
    Generate documentation for a list of parameters based on their usage in code.
    
    Args:
        code_folder (str): Path to the folder containing the source code
        param_names (List[str]): List of parameter names to document
        output_folder (str): Path where the generated documentation should be stored
    """
    # Load environment variables
    load_dotenv()
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Process each parameter
    for param_name in param_names:
        print(f"Processing parameter: {param_name}")
        
        # Find all references to the parameter in the code
        references = find_param_references(code_folder, param_name)
        
        if not references:
            print(f"No references found for parameter: {param_name}")
            continue
    
        
        # Generate documentation using OpenAI
        documentation = generate_param_documentation(param_name, references)
        
        # Save documentation to file
        output_file = Path(output_folder) / f"{param_name}.md"
        with open(output_file, 'w') as f:
            f.write(documentation)
        
        print(f"Documentation generated for {param_name}: {output_file}")

def read_params_from_file(file_path: str) -> List[str]:
    """
    Read parameter names from a file, one parameter per line.
    Empty lines and lines starting with # are ignored.
    """
    params = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Strip whitespace and skip empty lines or comments
                line = line.strip()
                if line and not line.startswith('#'):
                    params.append(line)
    except FileNotFoundError:
        print(f"Error: Parameters file not found: {file_path}")
        sys.exit(1)
    
    return params

if __name__ == "__main__":
    # Read parameters from file
    code_folder = "/Users/haviv_rosh/work/PathlockGRC/"
    params_file = "params.txt"
    output_folder = "docs/"
    
    # Read parameters from file
    param_names = read_params_from_file(params_file)
    print(f"Found {len(param_names)} parameters to process")
    
    generate_doc(code_folder, param_names, output_folder) 