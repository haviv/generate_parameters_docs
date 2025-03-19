# AddRoleToUser

**Category:** User Management

**Description:** The `AddRoleToUser` action is designed to facilitate role-based access control within Pathlock Cloud by dynamically assigning specified roles to users. This action integrates with the workflow engine to automate the process of role assignment based on specific triggers or conditions, such as user requests or administrator actions. It supports adding roles directly requested by the user, roles specified in the workflow step, or additional roles defined by the administrator. The action leverages the system's connectors to apply the changes directly to the user's profile in the respective system, ensuring that access permissions are updated in real time.

**Parameters:**

  - Basic:
    - Name: `Username`
    - Description: The username of the account to which the role will be added.
    - Default value: N/A
    - Mandatory: Yes
  - Name: `AddRoleFromRequest`
    - Description: Determines if the role to be added should be taken from the user's request.
    - Default value: false
    - Mandatory: No
  - Name: `RequestedRole`
    - Description: Specifies the role to be added to the user. This role is typically defined in the request for workflows triggered by self-service requests.
    - Default value: N/A
    - Mandatory: No
  
  - Advanced:
    - Name: `IgnoreAdditionalRequestedRoles`
    - Description: Indicates whether to ignore any additional roles requested beyond the primary requested role.
    - Default value: false
    - Mandatory: No
    - Name: `Custom_Roles_Add`
    - Description: A custom or dynamically determined list of roles to add to the user, which can be based on workflow logic or admin input.
    - Default value: N/A
    - Mandatory: No
    - Name: `OnlyAssignRolesInCurrentSystem`
    - Description: Restricts role assignment to the current system to avoid cross-system role assignments, ensuring system integrity and compliance.
    - Default value: false
    - Mandatory: No

**Business impact:** Automating role assignment through the `AddRoleToUser` action significantly enhances organizational security and compliance by ensuring that users have the appropriate access levels based on their roles and responsibilities. This process minimizes the risk of unauthorized access and facilitates efficient user management, role-based access control, and compliance with regulatory requirements.

**Example of usage:** As an example, if a user submits a request for access to specific resources needed for a new project, the workflow could be configured to trigger the `AddRoleToUser` action. This action would then automatically assign the relevant roles to the user's profile, granting them the requested access without manual intervention from the IT department.

**Prerequisites:** Users or administrators initiating this action must have sufficient permissions to modify user roles within the target system. Additionally, the system ID and user information must be accurately specified in the workflow parameters.

**Error Handling and Troubleshooting:**

  - **Common error scenario:** Role does not exist.
    - **Probable cause:** The roleName specified does not match any roles within the system.
    - **Recommended solution:** Verify the roleName parameter matches the name of an existing role within the system.

  - **Common error scenario:** User not found.
    - **Probable cause:** The specified username does not exist or is misspelled.
    - **Recommended solution:** Ensure the username is correct and exists in the system.

  - **Common error scenario:** System connection failure.
    - **Probable cause:** Workflow action cannot establish a connection with the target system.
    - **Recommended solution:** Check the system connectivity and ensure the system ID is correct.

For further assistance, consult the system logs or contact technical support.