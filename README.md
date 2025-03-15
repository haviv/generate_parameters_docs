# Pathlock GRC Parameter Documentation Generator

## Overview
This Python tool automates the generation of parameter documentation for Pathlock Cloud GRC parameters. It scans C# code for parameter references, collects relevant context snippets, and generates comprehensive documentation using OpenAI's GPT-4.

---

## Prerequisites

- **Python 3.8+**
- **OpenAI Python SDK**
- **grep command-line tool** (available on Unix/Linux/macOS)
- **dotenv** package (`pip install python-dotenv`)
- An **OpenAI API Key** stored in an `.env` file:
  
        OPENAI_API_KEY=your_openai_api_key_here

---

## Project Structure

- `params.txt`: Contains parameter names to document (one per line).
- `docs/`: Directory where markdown documentation files are saved.
- Source code directory (`.cs` files): configurable via the script.

---

## How it Works

### Step-by-Step Workflow:

**1. Parameter Listing:**
- Parameters to document are read from `params.txt`, one per line.

**2. Parameter Reference Discovery:**
- The script uses `grep` to recursively scan `.cs` files, capturing occurrences of each parameter.
- Extracts context around each occurrence (default: 10 lines context).

**3. Documentation Generation (with OpenAI GPT-4):**
- Collected references and contexts are sent to the GPT-4 model.
- GPT-4 analyzes the context and generates meaningful documentation for each parameter.

**4. Output Documentation:**
- Markdown documentation files are generated and saved to a specified output folder (`docs/`).

---

## Usage Instructions

### 1. Prepare Environment:
- Install dependencies:

        pip install openai python-dotenv

- Set your OpenAI API key in a `.env` file at the project root:

        OPENAI_API_KEY=your_openai_api_key_here

### 2. Configure Files:
- **`params.txt`**:
  - Include parameters you wish to document, one per line. Example:

        AdditinalDomainsCustomUser
        CustomDomains
        LdapFilter

### 2. Run the Script:
- Execute the Python script:

        python generate_docs.py

### 3. View Output:
- Generated markdown files are stored in the `docs/` folder.

---

## Customization

- **Context lines:** Modify how many context lines are extracted around matches in the `find_param_references` function.
- **Output format:** Adjust prompts sent to GPT-4 for customized documentation styles.
- **Output path:** Change `output_folder` path to store documentation elsewhere.

---

## Example Output

A sample parameter documentation generated looks like this:

**Example:**

### AdditinalDomainsCustomUser

- **Category:** Active Directory Integration  
- **Default Value:** (none)  
- **Impact Level:** High  

**Description:**  
Specifies the username used to authenticate with additional Active Directory domains, enabling retrieval of user and group data from those domains.

**Business Impact:**  
- Enables user data synchronization from multiple domains.
- Critical for enterprises with multiple or cross-forest domains.

**Technical Impact:**  
- Required for multi-domain integrations.
- Misconfiguration can lead to authentication failures and incomplete user data synchronization.

**Example Scenario:**  
- Integration with multiple Active Directory forests/domains requiring specific credentials.

**Best Practices:**  
- Configure this parameter alongside `AdditinalDomainsCustomPassword`.  
- Ensure credentials have minimal necessary privileges.  
- Regularly update and rotate credentials to maintain security.

---

## Limitations and Considerations

- Currently supports `.cs` files only. Modify the grep command for additional file types.
- Ensure your API token is secure and has appropriate OpenAI usage permissions.
- Limit context size to optimize OpenAI API usage and costs.

---

## Troubleshooting

- Ensure `grep` is installed and accessible via terminal.
- Verify your OpenAI API key permissions and quota.
- Review logs for any `subprocess` related issues or
