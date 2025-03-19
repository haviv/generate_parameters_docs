# DeActivateUser

**Category:** User Management

**Description:**  
The DeActivateUser action is responsible for deactivating a user account within the Pathlock Cloud platform, particularly applicable to systems integrated like SAP. This action encompasses locking the user, setting expiration for the user account, and removing any existing authorizations. It dynamically chooses the deactivation approach based on provided parameters, supporting both specific and system-wide deactivation options. This action performs checks and actions conditionally, based on the specified user and system ID, providing flexibility for application in various scenarios.

**Parameters:**  
_Basic Parameters:_
- Name: DeActivateUser_Username
  - Description: The username of the account to be deactivated. This is initially checked, and if not provided, the action may alternatively target the requesting user based on further parameters.
  - Default value: None
  - Mandatory: No

_Advanced Parameters:_
- Name: ActivateUser_RunOnRequestUser
  - Description: A boolean parameter that decides whether the deactivation should be run on the user making the request if the username is not provided. Used in scenarios where the action targets the requester directly.
  - Default value: false
  - Mandatory: No
- Name: DeactivateUser
  - Description: System-wide options for deactivating a user. Allows specifying whether to lock the account, set expiration, or remove authorizations at a global level.
  - Default value: None
  - Mandatory: No

**Business impact:**  
The DeActivateUser action directly impacts the security and compliance posture of the organization by ensuring that user accounts can be deactivated or modified in response to varying requirements such as end of employment, changes in roles, or security incidents. Efficient handling of user deactivation helps in maintaining the least privilege principle and reduces the risk associated with orphaned or overly privileged accounts.

**Example of usage:**  
In a scenario where an employee leaves the organization, DeActivateUser can be triggered to immediately lock the account, set an expiration date to disable any future login attempts, and remove all assigned authorizations to safeguard against unauthorized access.

**Prerequisites:**  
- Proper permissions to invoke workflow actions within the Pathlock Cloud.
- An existing user account identified by a valid `SapUserName`.
- The invoking user must have the authority to perform user management tasks.

**Error Handling and Troubleshooting:**  
- **User Not Found:** If the specified username does not exist within the system, cross-verify the username for any typos or inconsistencies.
- **Action Fails:** If any of the deactivation steps (lock, set expiration, remove authorizations) fails, consult the error message for specifics. Common causes include network issues, insufficient permissions, or system-specific constraints.
- **System-Wide Parameter Inconsistencies:** If the deactivation does not perform as expected with system-wide parameters, verify the parameter strings for correctness and ensure they are applicable to the target system and user.