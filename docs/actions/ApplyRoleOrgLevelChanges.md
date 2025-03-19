Action Name: ApplyRoleOrgLevelChanges

**Category:** User Management

**Description:**

The ApplyRoleOrgLevelChanges action is designed to facilitate user role assignments and adjustments across organizational levels within the Pathlock Cloud platform. This action, as part of the identity and Governance, Risk, and Compliance (GRC) suite, automates the process of applying changes to user roles based on predefined parameters. This workflow action extends the capabilities of the ApplyRoleChanges action, focusing specifically on adjustments that pertain to organizational hierarchy and roles. It leverages the GetRoleChanges method to dynamically generate a set of role authorization changes derived from the input parameters, which are then applied to the system, ensuring users have the correct access rights and permissions at every organizational level.

**Parameters:**

Basic:
- Name: WorkflowActionParameters
- Description: This is the collection of parameters required to execute the ApplyRoleOrgLevelChanges action. Within the code, this object contains all the necessary information to build the changes object through the CreateDerivedRoleAction.BuildChangesObject method. These parameters include details such as the specific roles, users, and organizational levels involved in the change process.
- Default value: N/A
- Mandatory: Yes

Advanced:
(No advanced parameters are specified in the provided code snippet. All necessary parameters are encompassed within the WorkflowActionParameters object.)

**Business impact:**

Implementing the ApplyRoleOrgLevelChanges action within an organization’s user management process streamlines the process of updating role assignments across different organizational levels. This ensures that access rights and permissions are correctly aligned with each user’s responsibilities and the organizational hierarchy, enhancing security and compliance. By automating this process, it reduces manual errors, saves time, and ensures a consistent application of access control policies across the organization.

**Example of usage:**

An organization needs to update the access rights of a group of users after a departmental restructure. Using the ApplyRoleOrgLevelChanges action, administrators can define the required changes in roles and permissions at different organizational levels and apply these changes in bulk, ensuring that each affected user receives the correct access rights according to their new position and department.

**Prerequisites:**

- Administrative access to the Pathlock Cloud platform.
- A predefined set of role changes that need to be applied, encapsulated within the WorkflowActionParameters object.
- Understanding of the organizational structure to accurately define the role changes at the correct organizational levels.

**Error Handling and Troubleshooting:**

- **Error: Incomplete Parameters**: Ensure all mandatory fields in the WorkflowActionParameters are filled. Review the input parameters for completeness.

- **Error: Unauthorized Action**: Verify that the executing user has the necessary permissions to perform role changes across the specified organizational levels.

- **Error: Failed to Apply Changes**: If changes cannot be applied, review the specified parameters for any inconsistencies or errors in the definition of roles and organizational levels. Ensure that the roles and levels specified exist and are configured correctly within the system.