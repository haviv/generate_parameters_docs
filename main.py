import os
from pathlib import Path
import subprocess
from typing import List
from openai import OpenAI
from dotenv import load_dotenv

def find_param_references(code_folder: str, param_name: str) -> List[dict]:
    """
    Find all files containing references to the given parameter.
    Returns a list of dictionaries containing file paths and relevant code snippets.
    """
    results = []
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
                            # Get context (5 lines before and after)
                            start = max(0, i - 5)
                            end = min(len(file_content), i + 6)
                            context = ''.join(file_content[start:end])
                            
                            results.append({
                                'file_path': file_path,
                                'context': context
                            })
    except subprocess.CalledProcessError:
        # No matches found
        pass
    
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

if __name__ == "__main__":
    # Example usage
    code_folder = "/Users/haviv_rosh/work/PathlockGRC/"
    param_names = ["CheckProcessQueueEvery"]
    output_folder = "docs/"
    
    generate_doc(code_folder, param_names, output_folder) 