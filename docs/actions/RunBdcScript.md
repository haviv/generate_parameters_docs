Action Name: RunBdcScript

**Category:** Workflow

**Description:** 
The `RunBdcScript` action automates the execution of Batch Data Communication (BDC) scripts within the Pathlock Cloud environment, facilitating seamless data communication and manipulation tasks across various systems. This action initializes the specified system context using the `ProfileTailorContext.InitContext` method and executes a script provided by the user through the system's connector, typically aimed at performing operations like data entry, updates, or migrations in a batch mode. It captures the output of the script execution, formatting it into a readable string result which is then made available for further processing or auditing. This action supports dynamic parameterization, allowing for flexible script executions across different systems or contexts as specified by the user.

**Parameters:**

- Basic Parameters:
    - Name: `RunBdcScript_ScriptFile`
    - Description: Path or identifier for the BDC script file to be executed. This parameter specifies which script the action should run, directing the system’s connector to process the specified batch operations.
    - Default value: None
    - Mandatory: Yes
    
    - Name: `RunBdcScript_SystemId`
    - Description: The system identifier where the BDC script should be executed. This optional parameter allows overriding the default system context, facilitating script execution on a specified target system.
    - Default value: Derived from `WorkflowActionPramaters.SystemId`
    - Mandatory: No

**Business impact:**
Executing BDC scripts through the `RunBdcScript` action significantly enhances the efficiency of data processing and system management within the Pathlock Cloud environment. It enables administrators and users to automate complex data manipulation tasks, ensure data integrity across multiple systems, and facilitate smooth data migrations or updates without manual intervention. This action thus plays a crucial role in maintaining operational efficiency, reducing the risk of human error, and ensuring compliance through traceable and auditable data manipulations.

**Example of usage:**
```csharp
var parameters = new WorkflowActionPramaters();
parameters.SetParameter("RunBdcScript_ScriptFile", "path/to/script");
parameters.SetParameter("RunBdcScript_SystemId", 2001); // Assuming 2001 is the ID of the target system

var runBdcScriptAction = new RunBdcScript();
runBdcScriptAction.Perform(parameters);
```
In this example, the `RunBdcScript` action is configured to execute a BDC script located at "path/to/script" on the system identified by ID 2001.

**Prerequisites:**
- Appropriate permissions to execute scripts on the specified system.
- The target system must be configured and accessible within the Pathlock Cloud environment.
- A valid BDC script file must be available and correctly specified in the parameters.

**Error Handling and Troubleshooting:**
- **Error:** Script file not found
    - **Cause:** The specified script path is incorrect or the file does not exist.
    - **Solution:** Verify the script path and ensure the file is accessible.
  
- **Error:** System connector initialization failure
    - **Cause:** Invalid or unreachable system ID.
    - **Solution:** Check the system ID for correctness and ensure the target system is properly configured and operational within the Pathlock Cloud environment.

- **Error:** Script execution failure
    - **Cause:** Errors within the script, such as syntax errors or operations on non-existent data.
    - **Solution:** Review the script for errors, test it in a controlled environment, and ensure it is compatible with the target system's data schema and operational context.