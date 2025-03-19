# AddRolesToUserFromWorkflowAffectedRoles

**Category:** User Management

**Description:** This action automates the process of assigning role-based access to users within the Pathlock platform, specifically focusing on users affected by workflow instances. It filters roles that have not been declined, are not BusinessRole types, and belong to the customer's system. The action identifies the user and system in question, then accordingly assigns or proposes the assignment of the appropriate roles. In case of failure or if no specific username is identified for a given system, a manual action is prompted to ensure proper handling.

**Parameters:**

_Basic:_

- Name: WorkflowInstanceId
  Description: Identifies the workflow instance from which roles are being assigned to the user.
  Default value: N/A
  Mandatory: yes

- Name: UseRequestUserNameAsFallback
  Description: Determines if the workflow should use the requesting username as a fallback option when no specific username is found for the current system.
  Default value: false
  Mandatory: no

_Advanced:_

- Name: UntilDateForRoleAssignment
  Description: Specifies a date until which the roles are valid. This is used to set temporal constraints on the assigned roles.
  Default value: Empty
  Mandatory: no

- Name: CopyRolesListInCuaSystems
  Description: Indicates whether the roles list should be copied in CUA (Central User Administration) systems, facilitating centralized user management.
  Default value: Empty
  Mandatory: no

**Business impact:** This action is crucial for maintaining secure, efficient, and compliant user access across systems within the Pathlock platform. It supports compliance by ensuring only authorized roles are assigned, facilitates user management by automating role assignments, and bolsters security by allowing for temporal constraints on access.

**Example of usage:** To add necessary roles to a new user based on their required access for workflow instance #12345, the workflow engine would trigger this action, automatically assigning the roles predefined for this workflow instance or prompting a manual review if necessary.

**Prerequisites:** 

- The user executing this action must have permissions to manage roles and users within the Pathlock platform.
- The WorkflowInstanceId must be valid and correspond to an existing workflow configuration.
- The affected roles must have already been defined within the workflow configuration.

**Error Handling and Troubleshooting:**

- **Common Error:** Roles not correctly assigned to the user.
  - **Cause:** Often occurs if the specified user does not exist in the specified system or if the system ID is incorrect.
  - **Solution:** Verify the user's existence in the system and ensure the system ID is correct. If using the fallback username, check that the username is correctly configured.

- **Common Error:** Manual action required but not executed.
  - **Cause:** This error happens if automatic role assignment fails, possibly due to system connectivity issues or configuration errors.
  - **Solution:** Review the manual action instructions provided and execute them as specified. Verify system connectivity and configurations.

In both cases, it's advisable to check the logs for any warnings or errors leading up to the issue for additional context.