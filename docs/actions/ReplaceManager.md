# Replace Manager

**Category:** User Management

**Description:** 
The `ReplaceManager` action automates the process of replacing an old manager with a new one within the organization's directory. When executed, this workflow action updates the manager for all employees currently reporting to the specified old manager to report to the new manager instead. It accommodates systems like Active Directory (AD) by translating usernames to their pre-Windows 2000 format and executing the manager update through the AD connector.

**Parameters:** 

_Basic:_

- Name: OldManager
  - Description: The identifier (e.g., email or username) of the manager being replaced. It is split to derive the username in AD specific format. This parameter is essential for identifying the list of subordinates whose managerial assignment needs an update.
  - Default value: N/A
  - Mandatory: yes

- Name: NewManager
  - Description: The identifier (e.g., email or username) of the new manager taking over. Similar to `OldManager`, this is used to update the manager field for all identified subordinates in the directory.
  - Default value: N/A
  - Mandatory: yes

_Advanced:_

- Name: WorkflowActionIdForDocumentation
  - Description: An optional parameter, if specified, it signifies the ID for documenting the action within the system. This parameter is utilized for tracking and logging the replacement process in the database.
  - Default value: null
  - Mandatory: no

**Business impact:** 
Executing this action streamlines managerial transitions within the organization, ensuring that direct reports are immediately realigned under the correct leadership without manual HR intervention. It facilitates seamless changes in management hierarchy, thereby maintaining the integrity and up-to-dateness of organizational structure and access controls.

**Example of usage:** 
To change the manager of all employees currently reporting to 'john.doe@company.com' so that they now report to 'jane.doe@company.com', the action would be initiated with the parameters `OldManager` set to "john.doe@company.com" and `NewManager` set to "jane.doe@company.com".

**Prerequisites:** 
- Access rights to execute workflow actions within the Pathlock cloud platform are required.
- Correct and existing user identifiers for both old and new managers must be provided.
- Active Directory (or similar system) integration must be configured and operable.

**Error Handling and Troubleshooting:** 

_Common error scenarios:_

1. Incorrect Manager Identifiers: If either the `OldManager` or `NewManager` identifiers do not exist or are incorrectly formatted, the action will fail to execute properly.
   
   _Resolution_: Verify that both identifiers are correct and retry the operation.

2. Lack of Permissions: The execution may fail due to insufficient permissions to make changes in the Active Directory.

   _Resolution_: Ensure the executing account or service has the necessary permissions in Active Directory to change manager assignments.

3. WorkflowActionIdForDocumentation Misuse: When specified incorrectly, logging and documentation of the action might not perform as expected.

   _Resolution_: Confirm the `WorkflowActionIdForDocumentation` value is correct or omit it if not necessary for action documentation.
   
In case of persistent issues despite following troubleshooting steps, consulting the system logs and reaching out to Pathlock support is recommended for further assistance.