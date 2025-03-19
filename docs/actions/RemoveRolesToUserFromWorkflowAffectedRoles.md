# Remove Roles From User

**Category:** Workflow

**Description:** This action automates the process of identifying and removing specific roles associated with a user that are deemed affected by a workflow instance. It iterates through roles grouped by systems and attempts to remove these roles for a specific SAP user name. Should the automatic role removal fail, or if specific conditions are met (e.g., no username found for the current system), the action defaults to creating a manual action for later resolution. This ensures that roles not applicable or authorized for the user due to changes in user status or access rights are properly managed, supporting compliance and security protocols.

**Parameters:**

- **Basic Parameters:**
  
  Name: WorkflowInstanceId  
  Description: The unique identifier of the workflow instance triggering this action. It is used to fetch all roles affected by this specific workflow.  
  Default value: None  
  Mandatory: Yes

  Name: UserName  
  Description: The SAP user name of the individual from whom roles are being removed. This name is used to identify and iterate over the systems and roles applicable to the user for potential removal.  
  Default value: Derived from `GetUser().SapUserName.ToUpper()`  
  Mandatory: Yes

- **Advanced Parameters:**

  Name: RolesToRemove  
  Description: A string array converted into a formatted string listing all the roles slated for removal. This parameter is built dynamically based on the roles associated with the user and the specific workflow instance.  
  Default value: None  
  Mandatory: No

**Business impact:** The efficient management of user roles is crucial for maintaining system security and compliance. By automating the process of removing unauthorized or outdated roles from users, the platform ensures that only appropriate access is granted, reducing the risk of data breaches or compliance violations. Additionally, the fallback to manual action creation ensures that all cases are addressed, even when automatic processing is not possible.

**Example of usage:** Upon completion of a compliance review workflow, the `RemoveRolesFromUser` action is triggered to remove any roles that the compliance review identified as no longer appropriate for the user. The action checks each role related to the user and removes them from the user's profile across different systems. If any role cannot be removed due to system restrictions or errors, a manual action is created for manual review and resolution.

**Prerequisites:** 
1. Valid `WorkflowInstanceId` that corresponds to an active workflow.
2. The user executing the action must have permissions to modify roles and initiate or trigger workflows within Pathlock Cloud.
3. Necessary system connectors and permissions should be in place to allow role modifications across integrated systems.

**Error Handling and Troubleshooting:**

- **Common Errors:**  
    - Failure to remove roles due to system connectivity issues or permissions.
    - No username found for the current system, leading to an inability to map and remove specific roles.

- **Probable Causes:**  
    - Network or connectivity issues between Pathlock Cloud and the target system.
    - Insufficient permissions for the service account or the user executing the workflow action.

- **Recommended Solutions:**
    - Verify connectivity and ensure that the Pathlock Cloud platform has the necessary permissions to perform role modifications in all target systems.
    - Review the user mapping to ensure that usernames are correctly associated across systems.
    - If manual actions are created, ensure that they are resolved promptly to maintain compliance and access integrity.

This documentation encapsulates the technical details and operational impacts of the `RemoveRolesFromUser` workflow action, providing all necessary information for effective usage and troubleshooting within Pathlock Cloud's identity and GRC platform.