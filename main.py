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
    CONTEXT_LINES = 40  # Number of lines before and after the match
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
    
    except subprocess.CalledProcessError as e:
        # No matches found
        print(f"Error in grep command: {e}")
        return results
    except UnicodeDecodeError as e:
        print(f"Unicode decode error: {e}")
        print(f"File causing error: {file_path if 'file_path' in locals() else 'unknown'}")
        return results
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
        print(f"Error type: {type(e).__name__}")
        print(f"Current file being processed: {file_path if 'file_path' in locals() else 'unknown'}")
        return results
    
    # Limit the number of files if we found too many
    MAX_FILES = 8
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
    # Load environment variables from .env file directly
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if not os.path.exists(env_path):
        raise ValueError(f".env file not found at {env_path}")
    
    with open(env_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                if key == 'OPENAI_API_KEY':
                    api_key = value
                    break
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    print(f"Using API key from .env file: {api_key[:10]}...")
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
    # Ensure output folder exists
    settings_docs_folder = os.path.join(output_folder, "settings")
    os.makedirs(settings_docs_folder, exist_ok=True)
    
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
            output_file = Path(settings_docs_folder) / f"{param_info['param_name']}.md"
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

def extract_class_name(line: str) -> str:
    """Extract the class name from a line containing a class definition."""
    try:
        # Extract text between 'class' and ':'
        class_part = line.split('class')[1].split(':')[0].strip()
        return class_part
    except:
        return None

def find_class_code(code_folder: str, class_name: str) -> tuple[str, str]:
    """
    Find and extract the complete class code for a given class name.
    Returns a tuple of (file_path, class_code).
    """
    try:
        # Search for the class definition
        cmd = f'grep -r --include="*.cs" "class {class_name}" {code_folder}'
        output = subprocess.check_output(cmd, shell=True, text=True)
        
        if not output:
            return None, None
            
        # Get the file path from the first match
        file_path = output.splitlines()[0].split(':')[0]
        
        if not os.path.isfile(file_path):
            return None, None
            
        # Read the entire file
        with open(file_path, 'r') as f:
            file_content = f.readlines()
        
        # Find the class definition line
        class_start = -1
        brace_count = 0
        found_class = False
        class_code_lines = []
        
        for i, line in enumerate(file_content):
            if f"class {class_name}" in line:
                class_start = i
                found_class = True
                
            if found_class:
                class_code_lines.append(line)
                brace_count += line.count('{') - line.count('}')
                
                if brace_count == 0 and len(class_code_lines) > 1:
                    # We've found the complete class
                    break
        
        if class_code_lines:
            return file_path, ''.join(class_code_lines)
        
        return None, None
        
    except subprocess.CalledProcessError:
        return None, None

def generate_action_documentation(class_name: str, file_path: str, class_code: str) -> str:
    """
    Generate documentation for a workflow action using OpenAI API.
    """
    # Load environment variables from .env file directly
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if not os.path.exists(env_path):
        raise ValueError(f".env file not found at {env_path}")
    
    with open(env_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                if key == 'OPENAI_API_KEY':
                    api_key = value
                    break
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    print(f"Using API key from .env file: {api_key[:10]}...")
    client = OpenAI(api_key=api_key)
    
    # Create the prompt for OpenAI
    prompt = f"""
you are a technical doc creator, you need to create a technical documentation for a saas company called Pathlock in a product called Pathlock clooud whcih is an identity and GRC platform. Similar to Sailpoint and Savynt.
One of the core component is the workflow engine which used to automate and expose a self service requests to end users like PAM, Access, Risk calculation, etc.,.
You need to document a workflow action based on the code that I will provide.
An action class exetnds IWorkflowAction and implement a Perform method whcih you need to understand what it does.
Guidelines:
1. When you give examples, make sure to give examples that are relevant to the business impact of the param.
2. when you reference someting, only do it if you are sure that the reference is relevant to the param and that it exist.
3. Generate the next format, leave a blank line between each section (**this is mandatory**)
4. Add a Header with the Action Name 

Generate the Documentation in This Exact Format:
Action name: (header format)
**Category:** (based on the code references decide which category it fits, for example: "Security", "Risk", "Compliance", "Workflow", "Audit", "Reporting", "User Management", "Configuration", "SOD")
**Description:** (provide a description of the action with high level overview and the flow of the actions so end user can understand what it does)
**Parameters:** (per parameter follow this strucrture:
    Name:
    Description:
    Default value:
    Mandatory: yes/no)
    Important: group the parametes into 2 buckets: basic and advanced. understand from the code what are the must have, mandatory params and what are not and they are extract config
    Important: when you write the descripiton, add the explanantion on how its being used in the code, what is the flow that uses it, under which context it is being used.

**Business impact:** (describe the business impact of the action)
**Example of usage:** (provide an example of usage of the action)
**Prerequisites:** (Clearly state required pre-conditions or permissions the user must have to execute this action.)
**Error Handling and Troubleshooting:** (List common error scenarios, their probable causes, and recommended solutions or workarounds.)

Important:Parameters format example:
**Parameters:**

_Basic Parameters:_

- Name: usernameParameter
  - Description: The username or comma-separated usernames to be added to the specified approval group. The system first checks this parameter; if it is not provided, it uses the username associated with the current workflow instance.
  - Default value: N/A
  - Mandatory: No

_Advanced Parameters:_

- Name: ReplaceApprovers
  - Description: Determines whether to replace all existing approvers in the target group with the new user(s) or to add the new user(s) alongside existing approvers. This boolean parameter enables flexibility in managing group memberships.
  - Default value: false
  - Mandatory: No

the next is the code of the action:
{class_code}

**Final Instructions**
- Ensure markdown validity (no syntax errors).  
- Do NOT add** ```markdown at the beginning or end.  
- Each section must be separated by a blank line (this is critical).  
- Only include relevant attributes—do not guess.  
- generate a valid markdown file. dont add ```markdown at the beginning or at the end of the file.
"""
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4-turbo-preview",
        messages=[
            {"role": "system", "content": "You are a technical documentation expert specializing in C# and workflow systems."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def generate_actions_doc(code_folder: str, actions_file: str, output_folder: str):
    """
    Generate documentation for workflow actions based on their class definitions.
    
    Args:
        code_folder (str): Path to the folder containing the source code
        actions_file (str): Path to the file containing workflow action class definitions
        output_folder (str): Path where the generated documentation should be stored
    """
    # Ensure output folder exists
    actions_docs_folder = os.path.join(output_folder, "actions")
    os.makedirs(actions_docs_folder, exist_ok=True)
    
    try:
        # Read the actions file
        with open(actions_file, 'r') as f:
            action_lines = f.readlines()
        
        print(f"Found {len(action_lines)} workflow actions to process")
        
        # Process each action
        for i, line in enumerate(action_lines, 1):
            # Extract class name
            class_name = extract_class_name(line)
            if not class_name:
                print(f"Skipping line {i}: Could not extract class name")
                continue
                
            print(f"\nProcessing action {i} of {len(action_lines)}: {class_name}")
            
            # Find the class code
            file_path, class_code = find_class_code(code_folder, class_name)
            if not class_code:
                print(f"Could not find code for class: {class_name}")
                continue
            
            # Generate documentation
            documentation = generate_action_documentation(class_name, file_path, class_code)
            
            # Save documentation to file
            output_file = Path(actions_docs_folder) / f"{class_name}.md"
            with open(output_file, 'w') as f:
                f.write(documentation)
            
            print(f"Documentation generated: {output_file}")
            
    except FileNotFoundError:
        print(f"Error: Actions file not found: {actions_file}")
        sys.exit(1)
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)
    
    print("\nAll workflow actions processed successfully!")

def generate_message_field_documentation(field_name: str, file_content: str) -> str:
    """
    Generate documentation for a message field using OpenAI API.
    """
    # Load environment variables from .env file directly
    env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')
    if not os.path.exists(env_path):
        raise ValueError(f".env file not found at {env_path}")
    
    with open(env_path, 'r') as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, value = line.strip().split('=', 1)
                if key == 'OPENAI_API_KEY':
                    api_key = value
                    break
    
    if not api_key:
        raise ValueError("OPENAI_API_KEY not found in .env file")
    
    client = OpenAI(api_key=api_key)
    
    # Create the prompt for OpenAI
    prompt = f"""
You are documenting message fields used in email templates for Pathlock Cloud, an Identity and GRC platform.
I will provide you with the code that uses this field, go over it and understand what this field is used for based on the code.
Dont guess, you should be able to understand what this field is used for based on the code.
The field {field_name} is used in email templates sent during workflow processes.
****Super Important:When you provide example do it int the next format:
    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
After adding the example, dont add any other text, just the example.

Based on the code context below, generate documentation for this message field in the following format:

**Field Name:** {field_name}

**Description:** (Explain what this field represents and its purpose in email templates)

**Usage Context:** (Explain when and where this field is typically used)

**Example:** 


Here's the relevant code context:
{file_content}

Generate clear, concise documentation that helps template authors understand how to use this field effectively.
Focus on practical usage and real-world examples.
If you can't determine certain information from the code context, focus on what can be reasonably inferred.

**Final Instructions**
- Ensure markdown validity (no syntax errors)
- Each section must be separated by a blank line (this is critical)
- Only include information that can be reasonably determined or inferred
- Don't add markdown code block markers
"""
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a technical documentation expert specializing in email template systems."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content

def read_template_content(template_path: str, stop_at_section: str = "## Parameter Details") -> str:
    """
    Read content from a template file up to a specified section.
    
    Args:
        template_path (str): Path to the template file
        stop_at_section (str): Section header where to stop reading (default: "## Parameter Details")
    
    Returns:
        str: Content of the template file up to the specified section
    
    Raises:
        FileNotFoundError: If template file is not found
    """
    with open(template_path, 'r') as f:
        content = ""
        for line in f:
            if line.strip() == stop_at_section:
                break
            content += line
    return content

def generate_message_fields_doc(workflow_mail_path: str, output_folder: str):
    """
    Generate documentation for message fields used in email templates.
    
    Args:
        workflow_mail_path (str): Path to the WorkflowMail.cs file
        output_folder (str): Path where the generated documentation should be stored
    """
    # List of message fields to document
    message_fields = [
        "requestId", "userName"
        , "adminName", "beginWaitingForApproveLink",
        "beginRequestStatusLink", "endLink", "groupOrManager", "beginApproveStepLink",
        "beginRejectStepLink", "beginMoveBackStepLink", "comment", "requestTransaction",
        "requestRole", "requestType", "stepStart", "stepEnd", "stepTargetEndTime",
        "requestInformation", "sapUserName", "beginDetailsLink", "previousApprover",
        "previousApproverComments", "reapprove", "beginRequestsWaitingLink",
        "beginRequestsWaitingLinkForCurrentInstance", "beginAuhtorizationReviewPortalLink",
        "beginDetailsLinkWithThankYou", "requestOpenedOrReturned", "beginDetailsLinkGeneral",
        "beginDetailsLinkWithThankYouGeneral", "beginApproveStepLinkGeneral",
        "beginUserOpenRequestsLink", "beginUserOpenRequestsBootstrapLink",
        "beginExtendStepLink", "beginDetailsLinkWithApproved", "beginDetailsLinkWithDeclined",
        "beginApproveStepLinkThankYou", "beginApproveStepLinkGeneralForFF",
        "beginCreateTasksLink", "delegatedBy"
    ]
    
    # Ensure output folder exists
    message_fields_docs_folder = os.path.join(output_folder, "message_fields")
    os.makedirs(message_fields_docs_folder, exist_ok=True)
    
    try:
        # Read the WorkflowMail.cs file
        with open(workflow_mail_path, 'r') as f:
            file_content = f.read()
        
        print(f"Found {len(message_fields)} message fields to process")
        
        # Read the template file for index content
        template_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'message_field_template.txt')
        index_content = read_template_content(template_path)
        
        # Process each message field
        for i, field_name in enumerate(message_fields, 1):
            print(f"\nProcessing field {i} of {len(message_fields)}: {field_name}")
            
            # Generate documentation
            documentation = generate_message_field_documentation(field_name, file_content)
            
            # Save documentation to file
            output_file = Path(message_fields_docs_folder) / f"{field_name}.md"
            with open(output_file, 'w') as f:
                f.write(documentation)
            
            # Add to index
            index_content += f"{documentation}\n"
            index_content += f"-----------------------------------\n"
            
            print(f"Documentation generated: {output_file}")
        
        # Save index file
        index_file = Path(message_fields_docs_folder) / "index.md"
        with open(index_file, 'w') as f:
            f.write(index_content)
        
        print(f"\nIndex file generated: {index_file}")
        
    except FileNotFoundError as e:
        if str(e).find('WorkflowMail.cs') != -1:
            print(f"Error: WorkflowMail.cs file not found at: {workflow_mail_path}")
        else:
            print(f"Error: Template file not found at: {template_path}")
        sys.exit(1)
    except Exception as e:
        print(f"\nError occurred: {str(e)}")
        sys.exit(1)
    
    print("\nAll message fields processed successfully!")

if __name__ == "__main__":
    # Configuration
    code_folder = "/Users/haviv_rosh/work/PathlockGRC/"
    actions_folder = "/Users/haviv_rosh/work/PathlockGRC/Bl/WorkflowActions"
    workflow_mail_path = "/Users/haviv_rosh/work/PathlockGRC/Bl/WorkflowMail.cs"
    params_file = "params.txt"
    actions_file = "actions.txt"
    output_folder = "docs/"
    
    # Generate parameter documentation
    #generate_doc(code_folder, params_file, output_folder)
    
    # Generate workflow action documentation
    # generate_actions_doc(code_folder, actions_file, output_folder)
    
    # Generate message fields documentation
    generate_message_fields_doc(workflow_mail_path, output_folder) 