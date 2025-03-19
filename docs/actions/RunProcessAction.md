Action Name: RunProcessAction

**Category:** Workflow

**Description:** The RunProcessAction enables automated execution of defined processes within the Pathlock platform. This action directly interfaces with the system's process management mechanism, specifically targeting operations related to identity management, governance, risk, and compliance (GRC). Upon invocation, the action retrieves and executes a specified process by its name through the ProfileTailorGateway service. This serves to automate routine tasks and enforce policy compliance, thereby streamlining operations and enhancing system efficiency.

**Parameters:** 

_Basic Parameters:_

- Name: RunProcessAction_ProcessName
- Description: Specifies the name of the process to be executed. This parameter is used to identify the process within the system, initiating its execution. The process name is matched against the available processes in the system, and the corresponding process code is retrieved and used to run the process.
- Default value: None
- Mandatory: Yes

_Advanced Parameters:_

No advanced parameters are required for this action.

**Business impact:** Automating process execution with RunProcessAction significantly enhances operational efficiency and ensures consistent enforcement of security policies and compliance requirements. By streamlining access management, risk calculation, and other GRC-related processes, organizations can reduce manual errors, improve response times, and maintain rigorous standards of security and compliance.

**Example of usage:** To automate the running of a password reset process named “ResetUserPassword”, the RunProcessAction can be configured with the `RunProcessAction_ProcessName` parameter set to "ResetUserPassword". This would automatically initiate the password reset process for handling user requests without manual intervention, thereby improving the efficiency of user management operations.

**Prerequisites:** The user must have the necessary permissions to execute the specified process within the system. Additionally, the specified process must exist and be enabled for automation within the Pathlock platform.

**Error Handling and Troubleshooting:**

- **Error:** Process name not found.
  - **Cause:** The specified process name does not match any existing process within the system.
  - **Solution:** Verify that the process name is correct and matches exactly with those defined in the system. Check for typos or use the system's process management interface to confirm process names.

- **Error:** Insufficient permissions.
  - **Cause:** The executing user does not have the necessary permissions to run the specified process.
  - **Solution:** Ensure the user executing the RunProcessAction has the appropriate permissions to perform the specified process. This may require adjusting user roles or permissions settings within the Pathlock platform.