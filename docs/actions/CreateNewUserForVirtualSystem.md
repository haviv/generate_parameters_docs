# CreateNewUserForVirtualSystem

**Category:** User Management

**Description:** This action is designed to automate the creation of new users within a virtual system. It dynamically associates users with appropriate systems based on roles assigned within the workflow process. If a user does not already exist, a new user profile is created with essential identity attributes such as username, full name, and employee ID. Additionally, this action can reactivate deleted users and update their profiles. The process also includes assigning or removing user roles based on the current workflow, ensuring users have appropriate access rights within the system.

**Parameters:**

- Basic:
    - Name: Username
    - Description: The username for the new or existing user to be created or updated.
    - Default value: None
    - Mandatory: Yes
    - Name: PerformedBy
    - Description: Identifier of the user who initiated the user creation process. If not provided, the system will default to the Windows username of the requester.
    - Default value: Current Windows Username
    - Mandatory: No
- Advanced:
    - Name: new_user_creation_fullname
    - Description: Full name of the user to be created. If not provided, the system will assemble a full name from first and last names.
    - Default value: Concatenation of First Name and Last Name
    - Mandatory: No
    - Name: GetSystemIdFromRoles
    - Description: Determines if the user should be created in a system based on their assigned roles rather than a pre-defined system ID.
    - Default value: False
    - Mandatory: No
    - Name: RoleNamePostfix
    - Description: A postfix to append to role names during user role assignments.
    - Default value: None
    - Mandatory: No

**Business impact:** Streamlines the process of onboarding new users or updating existing user profiles in the virtual system, ensuring timely access to necessary resources. It supports compliance by automating the assignment of system-specific roles and permissions, reducing the risk of human error and unauthorized access.

**Example of usage:** An administrator wants to create a new user or update an existing one based on a specific workflow that triggers this action. The workflow could be initiated due to a request for new user access, changes in an existing user's role, or system access needs. The administrator provides the username, potentially the full name, any necessary role information, and whether the system ID should be derived from the user's roles. Once executed, the workflow creates or updates the user account accordingly, ensuring the user has the appropriate access rights.

**Prerequisites:** The user executing this action must have appropriate permissions within the Pathlock Cloud platform to create or modify user accounts and assign roles. Furthermore, role definitions and system IDs relevant to the action must be pre-configured in the system.

**Error Handling and Troubleshooting:**

- **Error:** User not created - Username not supplied.
    - **Cause:** The 'Username' parameter is missing.
    - **Solution:** Ensure the 'Username' parameter is provided when initiating the workflow action.
- **Error:** User not created - Username already exists.
    - **Cause:** An attempt to create a user with a username that already exists in the system.
    - **Solution:** Use a unique username or update the existing user's profile instead of attempting to create a new one.
- **Error:** Role assignment failure.
    - **Cause:** Issues with role name postfix or system ID mismatches could prevent successful role assignments.
    - **Solution:** Verify the 'RoleNamePostfix' and 'GetSystemIdFromRoles' parameters for accuracy and ensure they align with current system configurations and role definitions.