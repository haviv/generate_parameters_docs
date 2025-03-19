Action Name: RemoveUserToGroup

**Category:** User Management

**Description:** 

The `RemoveUserToGroup` action is designed to automatically remove a specified user from a given user group within the Pathlock cloud platform. This is part of the broader identity and access management functionality, facilitating dynamic adjustments to user permissions and access control based on organizational policies or individual user status changes. The action operates by identifying the user and group relationship in the system's database and subsequently deleting the association, effectively revoking the user's membership in that group.

**Parameters:**

Basic:

- Name: User Group Name
- Description: Specifies the name of the user group from which the user is to be removed. This parameter is utilized to pinpoint the exact relationship between the user and the group to be terminated.
- Default value: N/A
- Mandatory: Yes

**Business Impact:**

Executing the `RemoveUserToGroup` action has significant implications for access control and compliance within an organization. By allowing for the seamless removal of users from specific groups, administrators can ensure that access rights stay aligned with current roles, responsibilities, and security policies. This capability is pivotal in maintaining minimal necessary access, thus reducing the risk of unauthorized or inappropriate access to sensitive systems and information, which aligns with best practices in both PAM (Privileged Access Management) and general IAM (Identity and Access Management).

**Example of usage:**

To remove a user named "JohnDoe" from the "FinanceTeam" group, an administrator would initiate the `RemoveUserToGroup` action, specifying "FinanceTeam" as the User Group Name. This action could be triggered through a self-service portal by John Doe's manager or by the IT department in response to a role change or employment status update for John Doe.

**Prerequisites:**

1. The executing user must have administrative privileges or specific delegated permissions to manage user-group relationships.
2. The user and the user group specified must exist within the Pathlock cloud platform.
3. There must be an existing association between the user and the group to be removed.

**Error Handling and Troubleshooting:**

- **Error:** "User or Group Not Found"
    - **Cause:** The specified user or group name does not exist in the system.
    - **Solution:** Verify that the user and group names are spelled correctly and exist in the platform.
    
- **Error:** "Insufficient Permissions"
    - **Cause:** The executing user does not have the necessary privileges to remove users from groups.
    - **Solution:** Ensure that the user executing the action has administrative rights or has been delegated permissions for user-group management.