# Switch Request User

**Category:** User Management

**Description:** 

The Switch Request User action is designed to automate the process of transitioning a workflow instance to a new user based on specific criteria. This action facilitates scenarios where the ownership or responsibility of a request, such as privilege access management (PAM), needs to be reassigned to another user dynamically during the workflow execution. The action evaluates conditions to find a suitable user either by belonging to a specified user group or matching a pattern set for usernames, then re-attaches the found user ID to the workflow instance, effectively switching the workflow's current user.

**Parameters:**

- Basic:
  - Name: FindUserByUserGroup
    - Description: A boolean parameter that, when true, initiates the search for a user within a specified user group.
    - Default value: Not provided, but implicitly false if not set.
    - Mandatory: No
  - Name: FindUserByUserGroupNameField
    - Description: Specifies the name of the user group to search within when FindUserByUserGroup is true.
    - Default value: None
    - Mandatory: Yes, if FindUserByUserGroup is true.

- Advanced:
  - Name: FindUserByPatternSet
    - Description: A boolean parameter that directs the action to use a pattern set to generate and find a username, applicable when finding a user by specific naming conventions.
    - Default value: Not provided, but implicitly false if not set.
    - Mandatory: No
  - Name: SwitchReqeustUserName
    - Description: Used to specify or override the username during the user search process. It acts as initial input if FindUserByPatternSet is active.
    - Default value: None
    - Mandatory: No, but required if FindUserByPatternSet is true and the pattern needs an initial seed.

**Business impact:** 

Implementing the Switch Request User action significantly enhances workflow flexibility and automation in handling user access and permissions. By dynamically changing the user associated with a workflow instance based on predefined logic, organizations can streamline operations such as access delegation, risk calculation adjustments, and compliance tasks. This reduces manual intervention, speeds up response times for access requests, and ensures that activities are routed to the correct individuals following organizational policies or changes.

**Example of usage:** 

Consider a scenario where an employee's role is changing, and they now require different system access. A workflow initiated for changing the user's permissions can leverage the Switch Request User action to automatically assign the request to the new responsible user based on the user's new group membership or naming pattern.

**Prerequisites:** 

- WorkflowManager and UserCreationManagement services must be configured and operational.
- Relevant user groups and pattern sets should be predefined in the system.
- The executor of this action must have permission to read user groups, generate usernames based on patterns, and re-assign workflow instances.

**Error Handling and Troubleshooting:** 

- "No user found in Group": Check if the specified user group exists and has eligible users. Ensure users are not deleted or locked.
- "No user found": Verify that the criteria for finding a user by group or pattern set match existing users. If using patterns, confirm that the pattern set generates valid usernames and that these users exist in the system.
- Logging errors or exceptions: Ensure that Logger is properly configured to capture information and exception logs. Check the system and application logs for detailed error messages and stack traces.