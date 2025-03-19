Action Name: RemoveDeclinedRolesFromUser

**Category:** User Management

**Description:** 

This action is designed to remove roles from a user within the Pathlock Cloud system that have been previously marked as 'Declined' within a workflow context. When executed, it iterates through all roles associated with a workflow instance, identifying roles flagged as declined. It then groups these roles by their respective systems, ensuring that only those relevant to the customer's context are processed. For each system, the action attempts to remove the declined roles from the specified user, leveraging system-specific connectors and handling different user identifiers as necessary. This process is crucial for maintaining accurate and appropriate access rights, ensuring that declined roles do not remain erroneously assigned.

**Parameters:** 

- Basic Parameters:
    - Name: UseRequestUserNameAsFallback
    - Description: A boolean parameter that, when set to true, uses the requested username as a fallback identifier if a specific username for the current system cannot be determined.
    - Default value: False
    - Mandatory: No

- Advanced Parameters:
    *No advanced parameters are required for this action as it relies on intrinsic workflow data and context.*

**Business impact:** 

The execution of this action has significant implications for both security and compliance within an organization. By ensuring that only approved roles are retained and that declined roles are promptly removed, the company can maintain tighter control over access rights and permissions. This is crucial for compliance with internal policies and external regulations concerning access management. Additionally, from a security perspective, it minimizes the risk associated with inappropriate access levels, thereby safeguarding sensitive information and systems.

**Example of usage:** 

Imagine a scenario where a user requests access to multiple roles through the Pathlock Cloud's self-service portal. After the request undergoes a review, some roles are approved while others are declined based on predefined criteria or reviewer judgment. Upon conclusion of this process, the `RemoveDeclinedRolesFromUser` action is triggered automatically to remove the declined roles from the user's profile, ensuring the user's access rights remain accurately reflective of the approved permissions only.

**Prerequisites:** 

- The user executing the action must have sufficient permissions to modify role assignments within the Pathlock Cloud system.
- The workflow instance associated with the user's request must be in a state that allows role modification (i.e., not closed or archived).
- Connectivity with all relevant system connectors must be intact to perform the role removal operations.

**Error Handling and Troubleshooting:** 

- **Common Error Scenario:** Attempting to remove a role fails, and an error message "Remove role failed: [RoleName]" is logged.
    - **Probable Cause:** The role might no longer exist, or the system connector might be experiencing issues.
    - **Solution:** Verify the existence of the role and the health of the system connector. Retry the operation if the issue was temporary.

- **Common Error Scenario:** The action fails with no specific error message, only a generic failure is logged.
    - **Probable Cause:** Connectivity issues or misconfigurations in the system connector setup.
    - **Solution:** Check the system connector configuration and ensure there is network connectivity. Review logs for detailed error information.