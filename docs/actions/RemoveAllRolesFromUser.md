# RemoveAllRolesFromUser

**Category:** User Management

**Description:** This action is designed to manage and streamline the process of removing specified roles from a user across one or multiple systems within the Pathlock Cloud platform. It allows administrators to dynamically manage user permissions with options to specify roles to remove, roles to retain, and other configurations that influence how roles are managed. At its core, this action identifies the target user(s) and selectively removes roles based on parameters provided, thereby automating a crucial aspect of identity and access management workflows.

**Parameters:**

- Basic:
    - Name: RunOnAllSystems
      Description: Determines whether the action should be executed across all connected systems.
      Default value: None
      Mandatory: No
    - Name: RoleTypesToRemove
      Description: Specifies the types of roles to be removed, identified by a comma-separated list of role type IDs.
      Default value: None
      Mandatory: Yes
    - Name: RoleToKeep
      Description: Specifies roles that should not be removed, allowing for exceptions in the removal process.
      Default value: None
      Mandatory: No

- Advanced:
    - Name: RemoveAllRolesSingleCall
      Description: Enables the removal of all roles in a single operation if supported by the system connector.
      Default value: None
      Mandatory: No
    - Name: RolePathRemove
      Description: Specifies roles to be removed based on their object path, supporting more granular control over role management.
      Default value: None
      Mandatory: No
    - Name: RemoveRolesBySetValidity
      Description: If set, the action will configure role removal to only affect roles up to the current date, providing a time-bound approach to role management.
      Default value: None
      Mandatory: No
    - Name: DisableUserRefresh
      Description: Prevents the system from refreshing user information before performing the role removal action. Useful in scenarios where current role information is already known or to speed up processing.
      Default value: None
      Mandatory: No

**Business impact:** This action provides a scalable solution to maintaining proper access control and compliance across the Pathlock Cloud platform. By enabling administrators to efficiently remove roles from users, it directly supports identity governance and compliance (IGC) strategies, mitigates access risks, and ensures users have appropriate access rights according to their roles and responsibilities within an organization.

**Example of usage:** To remove all roles associated with the finance department except for a few critical roles from a user in SAP and Salesforce systems, you would configure the action to include the systems in question, specify the roles or role types associated with the finance department, and list the critical roles that need to be retained.

**Prerequisites:** Proper permissions to manage roles and execute workflow actions within the Pathlock Cloud platform. The user in question must exist in the specified systems, and the systems must be accessible by the workflow engine.

**Error Handling and Troubleshooting:**

- Common Error: Role removal operation fails.
  - Probable Cause: Network issues or system connector misconfigurations may prevent the action from communicating with external systems.
  - Recommended Solution: Verify connectivity and system connector configurations. Check if the external system supports the specified operations.
  
- Common Error: Roles specified in "RoleToKeep" are still removed.
  - Probable Cause: Incorrect parameter format or misidentification of roles.
  - Recommended Solution: Ensure the roles are correctly named and the parameters are formatted properly (e.g., comma-separated list).

- Common Error: Action does not execute on all specified systems.
  - Probable Cause: "RunOnAllSystems" parameter incorrectly set or system identifiers misconfigured.
  - Recommended Solution: Verify the "RunOnAllSystems" parameter setting and ensure system identifiers are accurate and correspond to connected systems.