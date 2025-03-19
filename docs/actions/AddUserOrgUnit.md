Action Name: AddUserOrgUnit

**Category:** User Management

**Description:**
The `AddUserOrgUnit` action is designed to manage and automate the process of assigning new organizational unit roles to a specific user within the Pathlock Cloud platform. This process involves identifying the user based on a given workflow instance, determining the new organizational unit (Org Unit) to be assigned, and dynamically attaching all relevant roles associated with that Org Unit to the user. The action utilizes the `ProfileTailorDataClassesDataContext` for database operations, fetching both the target user and Org Unit roles, and subsequently using the `ProvisionService` to apply these roles to the user in question.

**Parameters:**

*Basic:*

-   Name: Organization Unit Name
-   Description: The name of the organization unit whose roles are to be assigned to the user. This parameter is utilized to fetch the corresponding Org Unit and its related roles for the assignment process.
-   Default value: None
-   Mandatory: Yes

*Advanced:*

_None_

**Business impact:**
Implementing the `AddUserOrgUnit` action within workflow automation significantly streamlines user management processes, ensuring users are promptly and accurately granted access based on organizational roles. This efficiency aids in maintaining robust access control, compliance with company policies, and minimizing potential security risks by assigning appropriate permissions automatically.

**Example of usage:**

To utilize the `AddUserOrgUnit` action in a workflow, an administrator might set up a self-service request for new employees to be automatically assigned roles associated with their organizational unit. Upon the creation of a new employee's user account, the workflow is triggered, executing the `AddUserOrgUnit` action with the specific Org Unit Name supplied, thus provisioning the relevant access rights without manual intervention.

**Prerequisites:**

- A valid workflow instance ID must exist.
- The invoking user must have permissions to manage user roles within the system.
- The `Organization Unit Name` parameter must correspond to an existing organizational unit within the system.
- The system must have predefined roles associated with organizational units.

**Error Handling and Troubleshooting:**

- **Error**: Roles not assigned to the user.
  - **Cause**: The specified Org Unit Name does not exist or has no roles associated with it.
  - **Solution**: Ensure the Org Unit Name is correct and verify that roles are associated with this Org Unit in the system. 

- **Error**: User not found.
  - **Cause**: The workflow instance ID provided does not correspond to an existing user.
  - **Solution**: Check the workflow instance ID for accuracy and ensure that the user exists in the system.

For any persistent issues, verify the workflow configuration, check the system's connectivity and access rights, and refer to the system logs for detailed error messages.