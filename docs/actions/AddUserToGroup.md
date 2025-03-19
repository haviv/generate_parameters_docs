## Action name: AddUserToGroup

**Category:** User Management

**Description:**

The AddUserToGroup action automates the process of assigning a user to a specific user group within the Pathlock Cloud platform. This action is a core component of the platform's identity and access management capabilities, facilitating efficient and streamlined user group assignments. When executed, it takes a user and the target user group as inputs, and associates the user with the specified group by creating a relationship entry within the platform's database. This action is critical for managing access controls, implementing proper segregation of duties, and ensuring users have the necessary permissions to perform their job functions.

**Parameters:**

Basic:

- Name: User Group Name
- Description: The name of the user group to which the user will be added. This parameter is used to identify the target group in the platform's database and is crucial for the action to successfully associate the user with the specified group.
- Default value: None
- Mandatory: Yes

Advanced:

_None_

**Business impact:**

The AddUserToGroup action directly impacts the effectiveness of identity and access management processes within an organization. By automating user group assignments, this action helps ensure that access rights and permissions are distributed appropriately and efficiently across users. It supports adherence to compliance requirements by facilitating proper access controls and segregation of duties. Prompt and accurate user group assignments play a vital role in minimizing unauthorized access risks and enhancing the overall security posture.

**Example of usage:**

```csharp
// Assuming User and UsersGroup objects are already populated with relevant data
User exampleUser = new User() { UserId = "exampleUser123" };
UsersGroup exampleGroup = new UsersGroup() { Id = "exampleGroup456" };

AddUserToGroup action = new AddUserToGroup();
action.DoActionOnUserAndGroup(exampleUser, exampleGroup);
```

**Prerequisites:**

To execute the AddUserToGroup action, you must have:

- Administrative privileges or equivalent permissions that allow modifying user-group relationships within the Pathlock Cloud platform.
- Valid User and UsersGroup objects representing the target user and group.

**Error Handling and Troubleshooting:**

Common error scenarios include:

- **User or Group Not Found:** If the specified user or group cannot be found in the platform's database, ensure the provided identifiers are correct and that both entities exist before attempting to execute the action again.
- **Duplicate Group Assignment:** Attempting to add a user to a group they are already a member of may result in an error. Verify user group memberships before executing the action.
- **Database Connectivity Issues:** If there are issues connecting to the database to insert the user-group relationship, verify database access permissions and network connectivity.

In case of encountering errors, reviewing application logs for specific error messages and stack traces can provide further insights into the issue's root cause.