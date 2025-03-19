Action Name: SwitchUserForEA

**Category:** User Management

**Description:** The SwitchUserForEA action automates the process of switching a user's identity within the Pathlock Cloud platform. This action is particularly useful in scenarios where an administrative or automated process needs to act on behalf of another user, typically for the purpose of identity and access management tasks. When executed, the action searches for users based on a set of criteria, selects an appropriate user according to provided parameters, and then updates the workflow instance with the new user's identity. This process is essential for operations such as Privileged Access Management (PAM), where acting on behalf of another user is a common requirement.

**Parameters:**

_Basic:_

- Name: SearchByEmail
    - Description: Determines the method for user search. If true, the action searches for users by email matching the email of the user in the current workflow instance. Used in contexts where email uniqueness is maintained and can be relied upon for identifying users.
    - Default value: N/A
    - Mandatory: Yes

_Advanced:_

- Name: UserStartWithFilter
    - Description: Filters users whose identifiers (such as usernames) start with the specified prefix. This parameter is used to narrow down the list of relevant users in large datasets or in systems where user identifiers follow a naming convention based on roles, departments, etc.
    - Default value: N/A
    - Mandatory: No
    
**Business impact:** The ability to seamlessly switch user contexts within automated workflows significantly enhances the efficiency of access and identity management processes. This capability facilitates smooth and secure operations across various GRC (Governance, Risk Management, and Compliance) activities, ensuring that actions such as access requests, risk calculations, and privilege management are executed promptly and accurately, minimizing the risk of unauthorized access or non-compliance with internal policies and external regulations.

**Example of usage:** An administrative workflow requires temporarily granting an auditor the access rights of a specific user to review their access privileges and usage logs. By using the SwitchUserForEA action, the workflow can dynamically switch the auditor's context to that of the target user, allowing the auditor to perform the necessary reviews without permanently altering user access levels or requiring manual intervention.

**Prerequisites:** The executing user or system must have sufficient permissions to perform user identity switches within the Pathlock Cloud platform. This typically involves administrative-level access or specific delegation permissions, ensuring that only authorized entities can execute such changes.

**Error Handling and Troubleshooting:**

- *Error: "User not created, See server logs for more information"*
    - Cause: The action failed to switch to a new user, possibly because no users matched the search criteria or due to a database update failure.
    - Solution: Ensure that the search parameters are correctly specified and that there are eligible users that meet the criteria. Additionally, check the server logs for more detailed error messages which may indicate a more specific problem, such as database connectivity issues or permission-related errors.