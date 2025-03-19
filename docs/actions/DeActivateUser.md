# DeActivateUser

**Category:** User Management

**Description:**  
The DeActivateUser action is designed to automate the process of deactivating a user account within the Pathlock Cloud identity and GRC platform. This action executes several key operations: locking the user account, setting expiration for the account (effectively disabling it), and removing any existing authorizations assigned to the user. The workflow leverages conditional logic to target a specific user based on the supplied parameters, with a fallback to operate on the request user if no specific username is provided or found. This action is fundamental in maintaining the security posture and compliance status of an organization by ensuring that user access is appropriately revoked when no longer needed or in cases of employee departure.

**Parameters:**  
- Basic
    - Name: DeActivateUser_Username
      Description: The technical name for identifying the user to deactivate. It is used to query the user from the system based on the SAP username. If not provided, the action may target the requesting user subject to the `ActivateUser_RunOnRequestUser` parameter.
      Default value: None
      Mandatory: No
- Advanced
    - Name: ActivateUser_RunOnRequestUser
      Description: A boolean parameter that determines if the action should run on the user making the request when no specific username is provided. This parameter adds flexibility for automated processes where the target is the requester.
      Default value: false
      Mandatory: No
    - Name: DeactivateUser
      Description: Specifies system-wide options for deactivating users, such as "Lock", "Set Expiration", or "Remove Authorizations". These options dictate what operations are performed as part of the user deactivation process.
      Default value: None
      Mandatory: No

**Business impact:**  
Deactivating user accounts promptly after they are no longer required or in response to particular events (e.g., employee termination) is pivotal for an organization's security and compliance. This action helps prevent unauthorized access and reduces the attack surface by ensuring only current, legitimate users have access. Additionally, it aids in compliance with various regulatory and audit requirements that mandate strict control over access rights.

**Example of usage:**  
An administrator wants to deactivate a user who has recently left the company. The administrator specifies the SAP username of the departed employee as the `DeActivateUser_Username` parameter and executes the DeActivateUser action. The action locks the user account, sets the expiration date, and removes all assigned authorizations, effectively disabling the account and logging all actions for audit purposes.

**Prerequisites:**  
- The executing user must have sufficient permissions to manage user accounts and execute workflow actions.
- The target user account must exist within the Pathlock Cloud system database.
- Relevant parameters (like SAP username) must correctly identify the user to deactivate.

**Error Handling and Troubleshooting:**  
- **Error:** "User not found"
  - **Cause:** The specified username does not match any user in the system.
  - **Solution:** Verify the username parameter for accuracy and ensure the user exists in the system.
- **Error:** Action failed with a message indicating a specific operation (e.g., "Lock User failed...")
  - **Cause:** A step within the deactivation process encountered an issue, such as a permission error or a connectivity problem.
  - **Solution:** Review the specific error message for clues and check system logs for more details. Ensure all prerequisites are met, and retry the action.