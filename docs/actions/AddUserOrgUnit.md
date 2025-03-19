# AddUserOrgUnit

**Category:** User Management

**Description:** 

The `AddUserOrgUnit` action is designed to augment a user's profile by assigning new organizational unit roles within the Pathlock Cloud's identity management system. When an organization wants to update or assign a new department, project team, or any organizational unit to a user, this action ensures the user gets access to necessary resources by assigning the roles associated with the new organizational unit. The process involves querying the current user's information, identifying the new organizational unit, and assigning all roles related to that unit to the user.

**Parameters:** 

_Basic Parameters:_

- Name: Organization Unit Name
  - Description: The name of the organizational unit whose roles are to be added to the user. This parameter is critical as it determines which roles are deemed necessary for the user based on their new or updated organizational alignment. The workflow retrieves this organizational unit's roles and assigns them to the user to ensure access is aligned with their responsibilities.
  - Default value: N/A
  - Mandatory: Yes

_Advanced Parameters:_

N/A

**Business impact:** 

Implementing the `AddUserOrgUnit` action streamlines the process of updating user roles in accordance with changes in their organizational unit assignments. It plays a pivotal role in ensuring that access management remains dynamic and reflects organizational changes, thereby maintaining security and compliance while enhancing productivity. By automating role assignment, it significantly reduces the administrative burden and potential errors associated with manual updates.

**Example of usage:** 

To assign a user to a new department 'Finance', the administrator would execute the `AddUserOrgUnit` action with the 'Organization Unit Name' parameter set to "Finance". This action would automatically query all roles associated with the 'Finance' organizational unit and assign them to the user, granting them access to all necessary resources without manual intervention.

**Prerequisites:** 

1. The administrator executing the action must have sufficient permissions to modify user roles within the Pathlock Cloud system.
2. The organization unit name provided must exist within the Company's organizational structure in Pathlock Cloud.
3. The user to whom the roles are being assigned must exist in the system.

**Error Handling and Troubleshooting:** 

- *Error:* User not found
  - *Cause:* The user ID provided does not match any user within the system.
  - *Solution:* Verify the user ID and ensure that the user exists within the Pathlock Cloud system.
  
- *Error:* Organization Unit not found
  - *Cause:* The specified organization unit name does not exist or is misspelled.
  - *Solution:* Verify the organization unit name for accuracy and ensure it exists within the company's organizational structure in Pathlock Cloud.
  
- *Error:* Role assignment failure
  - *Cause:* Could be due to a variety of issues including system connectivity, permissions, or the roles no longer existing.
  - *Solution:* Check system logs for detailed error messages. Ensure that the system is online, the executing user has adequate permissions, and the roles associated with the organization unit are valid and exist.