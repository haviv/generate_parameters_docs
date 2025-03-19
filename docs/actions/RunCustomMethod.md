Action name: RunCustomMethod

**Category:** Workflow

**Description:**

The `RunCustomMethod` action enables Pathlock Cloud users to automate and execute custom methods based on predefined parameters and methods configured in the system. This action can call various types of methods including RFC, SOAP, SQL, REPORT, HTTP, EXE, and PowerShell scripts. It begins by initializing the context with a system ID, followed by parameter preparation where method-specific URLs, connection strings, or other data are dynamically injected into the request. Then, it executes the method based on the call type, handles the output by converting DataTables to dictionaries or directly applying templates, and finally logs the result or error for monitoring or debugging purposes.

**Parameters:**

Basic:

- Name: RunCustomMethod_SystemId
- Description: The Id of the system on which to run the custom method. This is used to initialize the context for method execution.
- Default value: None
- Mandatory: Yes

- Name: RunCustomMethod_Type
- Description: The type of the method to be called (e.g., RFC, SOAP, SQL, etc.). Determines how the method execution is handled.
- Default value: None
- Mandatory: Yes

- Name: RunCustomMethod_Method
- Description: The name of the method to run. It is used to specify the method or the script that will be executed.
- Default value: None
- Mandatory: Yes

Advanced:

- Name: RunCustomMethod_ConnectionString
- Description: If the call type is SQL, this is the connection string to the database. It's used for establishing the database connection.
- Default value: None
- Mandatory: No

- Name: RunCustomMethod_Output
- Description: The template for output message formatting. Used for defining how the action output should be formatted.
- Default value: None
- Mandatory: No

- Name: RunCustomMethod_Url
- Description: The URL for HTTP or SOAP method calls. It specifies the endpoint to which the HTTP request should be sent.
- Default value: None
- Mandatory: No

**Business impact:**

This action enables automation of diverse method calls within the Pathlock Cloud environment, facilitating dynamic and flexible automation scenarios across different systems. It supports various operation types, thus allowing integration with a wide range of external systems and services. This can significantly reduce manual work, increase efficiency, and reduce errors in processes like PAM, access provisioning, and risk calculation.

**Example of usage:**

To execute a PowerShell script that performs user provisioning based on input parameters, configure the action with:

- RunCustomMethod_Type: PowerShell
- RunCustomMethod_Method: PathToScript.ps1
- Additional parameters as needed, like SystemId or URLs for HTTP calls.

This configuration would automate the execution of a PowerShell script, enhancing the provisioning process.

**Prerequisites:**

- Appropriate permissions to execute the specified method type (e.g., database access for SQL, execution policy for PowerShell).
- Availability of the method or script specified in the `RunCustomMethod_Method` parameter.
- Necessary system configurations and settings in place for accessing target systems (e.g., valid system ID, connection strings).

**Error Handling and Troubleshooting:**

Common errors might include file not found (for method scripts), access denied, or connection failures. Troubleshooting steps include:

- Ensuring the specified method name and path are correct and accessible by Pathlock Cloud.
- For database-related errors, verify connection strings and database server availability.
- For HTTP calls, ensure the URL is correct, and the endpoint is reachable from the Pathlock Cloud environment.
- Check logs for detailed error messages and stack traces.