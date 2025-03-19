Action name: Close User for Virtual System

**Category:** User Management

**Description:** 

The "Close User for Virtual System" action is designed for the Pathlock Cloud Identity and Governance, Risk, and Compliance (GRC) platform. This action plays a crucial role in managing the lifecycle of user identities across virtual systems by enabling administrators to programmatically close user accounts. It supports operations like marking a user as deleted or locking the user account, based on the provided parameters. This action ensures that only authorized users have access to systems, thereby maintaining the integrity and security of the system environment.

**Parameters:** 

Basic:

- **Name:** MarkUserasDeleted
- **Description:** A boolean parameter that determines the operation to be performed on the user. If true, the user's account is marked as deleted, the lock status is set to 128, and the deletion timestamp is recorded. If false, the user's account is locked by setting the lock status to 64 without marking as deleted.
- **Default value:** None
- **Mandatory:** No

Advanced:

- *No advanced parameters are defined for this action.*

**Business impact:** 

This action directly impacts the security posture and compliance status of the organization. By enabling administrators to swiftly lock or delete user accounts, it ensures that access to sensitive systems and data is appropriately managed throughout the user lifecycle. It helps in mitigating the risk of unauthorized access and potential data breaches, thus preserving the organizational integrity and compliance with relevant policies and regulations.

**Example of usage:** 

To mark a user as deleted on a virtual system, an administrator would invoke this action with the MarkUserasDeleted parameter set to true. This operation would be utilized in scenarios such as employee offboarding or after detecting a compromised user account, ensuring that the account is immediately rendered inactive and flagged for deletion.

**Prerequisites:** 

- The executing user must have administrative privileges on the Pathlock Cloud platform.
- Appropriate permissions to access and modify user statuses on the targeted virtual system.

**Error Handling and Troubleshooting:** 

- **Error:** User not found
  - **Cause:** The specified user does not exist in the system.
  - **Solution:** Verify the user identity and ensure correct information is used to identify the user.
  
- **Error:** Insufficient permissions
  - **Cause:** The user executing the action does not have adequate permissions to modify the user status.
  - **Solution:** Ensure the user has administrative privileges on the Pathlock Cloud platform and necessary permissions on the targeted virtual system.

- **Error:** Action fails without marking the user as deleted
  - **Cause:** The MarkUserasDeleted parameter might not be passed correctly.
  - **Solution:** Confirm that the parameter is correctly specified, ensuring it matches the expected boolean value.

For any persistent issues, consult the Pathlock Cloud platform documentation or contact support for further assistance.