import os
from pathlib import Path
import subprocess
from typing import List
from openai import OpenAI
from dotenv import load_dotenv
import sys
import json

def load_checkpoint(checkpoint_file: str) -> int:
    """Load the last processed parameter index from checkpoint file."""
    try:
        with open(checkpoint_file, 'r') as f:
            checkpoint = json.load(f)
            return checkpoint.get('last_processed_index', 0)
    except (FileNotFoundError, json.JSONDecodeError):
        return 0

def save_checkpoint(checkpoint_file: str, index: int):
    """Save the last processed parameter index to checkpoint file."""
    with open(checkpoint_file, 'w') as f:
        json.dump({'last_processed_index': index}, f)

def find_param_references(code_folder: str, param_name: str) -> List[dict]:
    """
    Find all files containing references to the given parameter.
    Returns a list of dictionaries containing file paths and relevant code snippets.
    """
    results = []
    MAX_CONTEXT_LENGTH = 500  # Maximum characters per context
    CONTEXT_LINES = 20  # Number of lines before and after the match
    WORKFLOW_INTERFACES = ["IWorkflowAction", "IWorkflowActionWithVerify", "IWorkflowActionParameters"]
    
    try:
        # Use grep to search for parameter references recursively in .cs files only
        cmd = f'grep -r --include="*.cs" "{param_name}" {code_folder}'
        output = subprocess.check_output(cmd, shell=True, text=True)
        
        # Process grep output
        for line in output.splitlines():
            if ':' in line:
                file_path, content = line.split(':', 1)
                if os.path.isfile(file_path):
                    # Read the file content
                    with open(file_path, 'r') as f:
                        file_content = f.readlines()
                    
                    # print(f"\nScanning {file_path}:")
                    workflow_actions = {}  # Dictionary of line number to action name
                    param_references = []  # List to store parameter references with context
                    
                    # Single pass through the file
                    for i, line_content in enumerate(file_content):
                        # Check for workflow action class definitions
                        if "class" in line_content and ":" in line_content:
                            if any(interface in line_content for interface in WORKFLOW_INTERFACES):
                                class_part = line_content.split("class")[1].split(":")[0].strip()
                                # print(f"Found workflow action: {class_part} at line {i+1}")
                                workflow_actions[i] = class_part
                        
                        # Check for parameter references
                        if param_name in line_content:
                            # Get context around the parameter reference
                            start = max(0, i - CONTEXT_LINES)
                            end = min(len(file_content), i + CONTEXT_LINES + 1)
                            context_lines = file_content[start:end]
                            context = ''.join(context_lines)
                            
                            # Find the nearest workflow action before this line
                            nearest_action = None
                            nearest_action_line = -1
                            for action_line, action_name in workflow_actions.items():
                                if action_line <= i and action_line > nearest_action_line:
                                    nearest_action = action_name
                                    nearest_action_line = action_line
                            
                            if nearest_action:
                                # print(f"Parameter {param_name} at line {i+1} belongs to workflow action: {nearest_action}")
                                context = f"[WORKFLOW_ACTION: {nearest_action}]\n{context}"
                            
                            # Truncate context if it's too long
                            if len(context) > MAX_CONTEXT_LENGTH:
                                context = context[:MAX_CONTEXT_LENGTH] + "..."
                            
                            results.append({
                                'file_path': file_path,
                                'context': context,
                                'workflow_action': nearest_action
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

def read_params_from_file(file_path: str) -> List[dict]:
    """
    Read parameter names and display names from a file.
    Format: DisplayName,ParamName (one per line)
    Empty lines and lines starting with # are ignored.
    """
    params = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Strip whitespace and skip empty lines or comments
                line = line.strip()
                if line and not line.startswith('#'):
                    display_name, param_name = line.split(',', 1)
                    params.append({
                        'display_name': display_name.strip(),
                        'param_name': param_name.strip()
                    })
    except FileNotFoundError:
        print(f"Error: Parameters file not found: {file_path}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error: Invalid format in params file. Each line should be 'DisplayName,ParamName'")
        sys.exit(1)
    
    return params

def generate_param_documentation(param_info: dict, references: List[dict]) -> str:
    """
    Generate documentation for a parameter using OpenAI API.
    """
    # Load environment variables
    load_dotenv()
    
    # Initialize OpenAI client with API key
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in environment variables")
    
    client = OpenAI(api_key=api_key)
    
    # Prepare the context from all references
    context = f"Parameter name: {param_info['param_name']}\n\nCode references:\n\n"
    workflow_actions = set()  # Use set to avoid duplicates
    
    for ref in references:
        # Collect workflow actions
        if ref['workflow_action']:
            workflow_actions.add(ref['workflow_action'])
            
        context += f"File: {ref['file_path']}"
        if ref['workflow_action']:
            context += f" (Workflow Action: {ref['workflow_action']})"
        context += f"\n```\n{ref['context']}\n```\n\n"
    
    # Add summary of workflow actions if any were found
    if workflow_actions:
        context = f"Found in Workflow Actions: {', '.join(sorted(workflow_actions))}\n\n{context}"
    
    # Create the prompt for OpenAI
    prompt = f"""

Based on the following code references, generate comprehensive markdown documentation for this parameter.
Go over the code and then understand what is the purposes of the param so you can create a documentation for end user that wants to use this param in this format. It has to be in markdown format - this is super important!
For context, these params are part of the Pathlock Cloud GRC platform. Pathlock is a cloud-based GRC platform that helps organizations manage their security, risk, and compliance.
Guidelines:
1. When you give examples, make sure to give examples that are relevant to the business impact of the param.
2. When presenting Applicable Workflows Actions, if there are no relevant workflow actions, dont add this attribute.
3. when you reference someting, only do it if you are sure that the reference is relevant to the param and that it exist.
4. Generate the next format, leave a blank line between each section (**this is mandatory**)
5. Add a Header with the parameter display name: {param_info['display_name']}

Generate the Documentation in This Exact Format:

**Technical Name:** {param_info['param_name']} **

**Category:** (based on the code references decide which category it fits, for example: "Security", "Risk", "Compliance", "Workflow", "Audit", "Reporting", "User Management", "Configuration", "SOD")

**Default Value:**

**Impact Level:** (based on the code references decide which impact level it fits, for example: "Low", "Medium", "High")

**Description:**

**Business Impact:**

**Technical Impact: when configured **

**Examples Scenario:**

**Related Settings:** (add related settings only if you saw them in the code references. Dont add them unless you are sure)

**Applicable Workflows Actions:** (list the specific workflows actions relevant here, take them from the Context section only - workflow_action attribute, dont add this attribute if there are no relevant workflow actions) 

**Best Practices:** configure when, avoid when 

the next are the code references:
{context}

**Final Instructions**
- Ensure markdown validity (no syntax errors).  
- Do NOT add** ```markdown at the beginning or end.  
- Each section must be separated by a blank line (this is critical).  
- Only include relevant attributes—do not guess.  
- generate a valid markdown file. dont add ```markdown at the beginning or at the end of the file."""
    
    # print(prompt)

    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a technical documentation expert. Generate clear, concise, and accurate documentation based on code analysis."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_doc(code_folder: str, params_file: str, output_folder: str):
    """
    Generate documentation for a list of parameters based on their usage in code.
    
    Args:
        code_folder (str): Path to the folder containing the source code
        params_file (str): Path to the file containing parameter names and display names
        output_folder (str): Path where the generated documentation should be stored
    """
    # Load environment variables
    load_dotenv()
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)
    
    # Read parameters from file
    params = read_params_from_file(params_file)
    print(f"Found {len(params)} parameters to process")
    
    # Load checkpoint
    checkpoint_file = "checkpoint.json"
    start_index = load_checkpoint(checkpoint_file)
    print(f"Resuming from parameter {start_index + 1} of {len(params)}")
    
    # Process each parameter
    try:
        for i, param_info in enumerate(params[start_index:], start=start_index):
            print(f"\nProcessing parameter {i + 1} of {len(params)}: {param_info['display_name']} ({param_info['param_name']})")
            
            # Find all references to the parameter in the code
            references = find_param_references(code_folder, param_info['param_name'])
            
            if not references:
                print(f"No references found for parameter: {param_info['param_name']}")
                # Save checkpoint even for skipped parameters
                save_checkpoint(checkpoint_file, i + 1)
                continue
            
            # Generate documentation using OpenAI
            documentation = generate_param_documentation(param_info, references)
            
            # Save documentation to file
            output_file = Path(output_folder) / f"{param_info['param_name']}.md"
            with open(output_file, 'w') as f:
                f.write(documentation)
            
            print(f"Documentation generated: {output_file}")
            
            # Save checkpoint after each successful processing
            save_checkpoint(checkpoint_file, i + 1)
            
    except KeyboardInterrupt:
        print("\nProcess interrupted by user. Progress has been saved.")
        sys.exit(1)
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        print("Progress has been saved. You can resume from the last successful parameter.")
        sys.exit(1)
    
    # Clear checkpoint after successful completion
    if os.path.exists(checkpoint_file):
        os.remove(checkpoint_file)
    print("\nAll parameters processed successfully!")

if __name__ == "__main__":
    # Configuration
    code_folder = "/Users/haviv_rosh/work/PathlockGRC/"
    params_file = "params.txt"
    output_folder = "docs/"
    
    generate_doc(code_folder, params_file, output_folder) 