Action Name: ApplyRolesToUserFromWorkflowAffectedRoles

**Category:** User Management

**Description:** This action is designed to manage user roles within the Pathlock Cloud identity and Governance, Risk, and Compliance (GRC) platform. It automates the process of assigning or removing user roles based on self-service requests or workflow triggers. The action allows for both adding new roles to a user and removing existing roles, with optional constraints such as only affecting roles within the current system or running the action across all systems. Additionally, it supports running opposite actions, effectively swapping the add and remove roles operations based on the workflow's needs. This capability is crucial for maintaining accurate role assignments and ensuring users have the appropriate access rights within various systems managed by Pathlock Cloud.

**Parameters:**

Basic:

- Name: DisableRemoveRoles
  Description: When enabled, the action will not remove any roles, only add roles. This parameter is used to safeguard against unintended role removal during the workflow execution.
  Default value: `false`
  Mandatory: No

- Name: DisableAddRoles
  Description: When enabled, the action only removes roles and does not add any new roles. This is useful for workflows focused on revoking access rather than granting new access.
  Default value: `false`
  Mandatory: No

Advanced:

- Name: OnlyAssignRolesInCurrentSystem
  Description: This parameter limits the role assignment action to the system currently being processed. It's mainly used in scenarios where the workflow is intended to affect a single, specific system rather than multiple systems.
  Default value: `false`
  Mandatory: No

- Name: RunOnAllSystems
  Description: This parameter allows the action to be executed across all systems, overriding the 'OnlyAssignRolesInCurrentSystem' parameter if both are specified. It expands the workflow's reach to ensure comprehensive role management across the enterprise.
  Default value: `false`
  Mandatory: No

- Name: RunOppositeAction
  Description: This innovative parameter inverts the add and remove operations. If a role is marked for addition, it will be removed, and vice versa. This is used for workflows requiring a reversal of planned role adjustments.
  Default value: `false`
  Mandatory: No

**Business impact:** The action directly influences user access control within the organization by dynamically managing role assignments based on specified criteria and workflow triggers. It plays a critical role in ensuring that users have the necessary permissions for their role within the organization while adhering to the principle of least privilege to minimize security risks.

**Example of usage:** In a scenario where a user needs to be granted access to additional resources for a limited project duration, the workflow could add specific roles to the user's profile at the project start and remove them upon completion. Using this action, roles relevant to the project are added, ensuring the user has the necessary access without manually adjusting their role memberships.

**Prerequisites:** Users or administrators looking to execute this action must have appropriate permissions within the Pathlock Cloud platform to manage roles and execute workflow actions. Additionally, a clear understanding of the target systems and roles affected by the execution of this action is necessary to avoid unintended access grants or revocations.

**Error Handling and Troubleshooting:**

- Common Error: Incomplete role assignment
  Probable Causes: Incorrect configuration of parameters, such as specifying `DisableAddRoles` or `DisableRemoveRoles` inadvertently.
  Recommended Solution: Review the action's parameters to ensure they accurately reflect the intended operation. Check for typos or logical errors in the parameter configuration.

- Common Error: Action applies to unintended systems
  Probable Causes: Misconfiguration of `RunOnAllSystems` or `OnlyAssignRolesInCurrentSystem` parameters.
  Recommended Solution: Clarify the scope of the intended role adjustments and adjust these parameters accordingly to target the correct systems. Ensure that the logic behind using these parameters aligns with the workflow's objectives.

- For further troubleshooting or errors not covered here, consulting the Pathlock Cloud's support documentation or reaching out to the support team is recommended.