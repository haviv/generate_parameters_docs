# MergeUserRolesWorkflowAction

**Category:** User Management

**Description:** 
The MergeUserRolesWorkflowAction is designed to consolidate multiple user roles into a single role within a specified target system. This process involves identifying roles to merge based on inclusion and exclusion criteria, including or excluding roles based on usage, and optionally removing activities associated with the merged roles. The action supports a test run mode that allows execution without applying the changes. This automation simplifies role management, ensures compliance, and enhances the efficiency of access management processes.

**Parameters:** 

*Basic:*

- Name: NewRoleName
  - Description: The name of the new role that will be created as a result of merging existing roles.
  - Default value: N/A
  - Mandatory: Yes

- Name: TargetSystem
  - Description: The system identifier where the role merge will take place. If not provided, the system ID is inferred from the user's context.
  - Default value: User's system ID
  - Mandatory: No

- Name: RolesToExclude
  - Description: A list of role names that should be excluded from the merging process.
  - Default value: Empty array
  - Mandatory: No

*Advanced:*

- Name: RolesToInclude
  - Description: Specifies roles to be explicitly included in the merge process. If empty, roles are selected based on the user's current roles and possibly filtered by excluded activities.
  - Default value: User's roles
  - Mandatory: No

- Name: ActivitiesToExclude
  - Description: Activities within roles that should not be transferred to the new merged role.
  - Default value: Empty list
  - Mandatory: No

- Name: ExcludeBasedOnUsage
  - Description: When true, roles not used by the user are excluded from the merge process.
  - Default value: false
  - Mandatory: No

- Name: IdentifyRolesBasedOnExcludedActivities
  - Description: Determines roles to merge by excluding activities defined in ActivitiesToExclude.
  - Default value: false
  - Mandatory: No

- Name: IsTestRun
  - Description: Executes the merge action in test mode without applying changes to check for potential errors or conflicts.
  - Default value: false
  - Mandatory: No

**Business impact:** 
This workflow action streamlines the management of user roles by merging multiple roles into a single, consolidated role. It directly impacts security and compliance by ensuring users have access based only on their current requirements, eliminating obsolete or unused permissions. It also simplifies the governance of role-based access, making the system easier to audit and manage.

**Example of usage:** 
Suppose a company needs to consolidate access roles after reorganizing its departments. Administrators can use MergeUserRolesWorkflowAction to merge roles related to specific departments into a single role per reorganized department, reducing complexity and ensuring that access rights are current and relevant.

**Prerequisites:** 
- Administrator permissions on the target system.
- A clear definition of roles to include or exclude and activities to exclude if applicable.
- Understanding the impact of merging roles to prevent unintended access rights assignments.

**Error Handling and Troubleshooting:** 
- If no roles are merged, verify that the rolesToInclude and rolesToExclude parameters are correctly set and that there are applicable roles for the user.
- If the target system cannot be determined, ensure that the TargetSystem parameter is correctly specified or that the user's context is correctly set to infer the system.
- For errors during the test run mode, review the roles and activities specified for any inconsistencies or conflicts.