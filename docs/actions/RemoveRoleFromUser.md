Action Name: RemoveRoleFromUser

**Category:** User Management

**Description:** 

The `RemoveRoleFromUser` action is designed to automate the process of removing roles from a user in the system. This action plays a crucial role in managing user permissions and access controls within the Pathlock Cloud platform. The primary flow involves checking for the username provided in the parameters and then executing role removal based on several conditions, including roles specified in workflow requests, roles defined by current workflow step, or roles directly provided to the action. It allows for role removal both from specific requests and as part of certification processes, ensuring that user access rights are appropriately managed according to governance, compliance, and security policies.

**Parameters:**

*Basic:*

- Name: RemoveRoleFromRequest
    - Description: Determines whether the role specified in an authorization request should be removed from the user.
    - Default value: N/A
    - Mandatory: No

- Name: RequestedRole
    - Description: Specifies the role to be removed from the user. This is used when a specific role removal is requested.
    - Default value: N/A
    - Mandatory: No

*Advanced:*

- Name: IgnoreAdditionalRequestedRoles
    - Description: If set, any additional roles requested in the same operation will not be removed.
    - Default value: N/A
    - Mandatory: No

- Name: RemoveRolesBySetValidty
    - Description: Indicates if the removal process should set the role's validity to the current date, effectively deactivating it.
    - Default value: N/A
    - Mandatory: No

**Business impact:** 

Removing roles from users directly impacts the security and compliance posture of the organization. By enabling precise control over the access rights of users, the action helps in maintaining the principle of least privilege, risk management, and compliance with internal and external regulations. This ensures that users have access only to the resources necessary for their roles, reducing the risk of unauthorized access or data breaches.

**Example of usage:** 

As part of a user offboarding workflow, the `RemoveRoleFromUser` action can be configured to remove all roles associated with the departing employee, ensuring that access is revoked in a timely and auditable manner.

**Prerequisites:** 

- Correct permissions to execute workflow actions within the Pathlock Cloud platform.
- Valid user identifier and role name(s) as input parameters.
- Adequate system connectivity and access rights for the execution of role removal operations.

**Error Handling and Troubleshooting:** 

- **Common Error Scenario:** Role removal fails due to an invalid user or role name.
    - **Probable Cause:** The specified user or role does not exist.
    - **Recommended Solution:** Verify the user and role names for accuracy and existence in the system.

- **Common Error Scenario:** Role removal is skipped or not executed.
    - **Probable Cause:** `IgnoreAdditionalRequestedRoles` parameter set to true, preventing further removal actions.
    - **Recommended Solution:** Ensure the `IgnoreAdditionalRequestedRoles` parameter is correctly set as per the desired outcome.

- **Common Error Scenario:** Action execution throws InvalidOperationException.
    - **Probable Cause:** Internal operation failed due to system constraints or issues.
    - **Recommended Solution:** Review system logs for detailed error messages. Check system status and constraints that may affect the operation.