# AddRolesToUserFromWorkflowAffectedRoles

**Category:** User Management

**Description:** This action is responsible for automating the process of assigning roles to a user within the Pathlock Cloud Identity and Governance Risk Compliance (GRC) platform. When triggered, it fetches all roles associated with a workflow instance that are not declined and belong to non-BusinessRole categories. These roles are then grouped by the system they are associated with. For each system, the action attempts to assign the fetched roles to the specified user, utilizing various parameters to tailor the assignment process. If certain conditions are not met or an error occurs, the action resorts to creating a manual task for later processing.

**Parameters:**  
_Basic Parameters_  
- **Name:** WorkflowInstanceId  
  **Description:** The unique identifier for the workflow instance initiating this action. It is used to fetch all roles associated with this workflow instance.  
  **Default value:** None  
  **Mandatory:** Yes  

- **Name:** UseRequestUserNameAsFallback  
  **Description:** A boolean parameter that dictates whether to use the requested username as a fallback if no specific username can be identified for the current system.  
  **Default value:** False  
  **Mandatory:** No  

_Advanced Parameters_  
- **Name:** UntilDateForRoleAssignment  
  **Description:** Specifies an expiration date for the role assignment. If provided, the system will set this date for the role assignments to indicate when the roles should automatically be unassigned.  
  **Default value:** None  
  **Mandatory:** No  

- **Name:** CopyRolesListInCuaSystems  
  **Description:** Indicates whether the list of roles should be copied in Central User Administration (CUA) systems. It is relevant in scenarios where role assignments are managed centrally.  
  **Default value:** None  
  **Mandatory:** No  

**Business impact:** This action streamlines the process of user role management by automating role assignments based on workflow-driven events. It enhances compliance and efficiency by ensuring that users have the necessary access rights according to their responsibilities and current organization policies. Additionally, by providing fallbacks and manual action creation in case of conflicts or errors, it ensures that no user ends up with incorrect or insufficient roles, thereby mitigating risk.

**Example of usage:** Suppose a new employee needs to be quickly integrated into multiple systems with specific roles. By initiating a workflow that triggers this action, the employee can be automatically granted the necessary roles across the systems without manual intervention, provided all conditions and parameters are correctly set.

**Prerequisites:** Before executing this action, ensure that:
- The WorkflowInstanceId is correctly identified and passed as a parameter.
- The user executing this action has sufficient permissions to assign roles in the targeted systems.
- The necessary systems are correctly configured within the Pathlock Cloud platform to accept and process these automated role assignments.

**Error Handling and Troubleshooting:**  
- If roles fail to be assigned and no specific error is thrown, ensure that the system IDs and role names are correctly specified, and that the targeted systems are available and responsive.
- In case of errors relating to "UntilDateForRoleAssignment" or "CopyRolesListInCuaSystems" parameters, verify their formats and the system’s capability to process these requests.
- If manual actions are being generated frequently, investigate the conditions under which the automated process fails, paying close attention to user name resolutions and role applicability checks. Monitor log files for any exceptions thrown during the action's execution for more detailed diagnosis.