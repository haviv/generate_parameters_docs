# RemoveBusinessRoleToUserAction

**Category:** User Management

**Description:** The `RemoveBusinessRoleToUserAction` is designed to facilitate the removal of business roles from a specified user within the Pathlock Cloud platform. It leverages a workflow-based approach to automate and streamline the process of detaching business roles. Upon invocation, the action evaluates the roles currently assigned to a user and selectively removes the specified role if it is found. This operation is crucial in managing user access rights and ensuring that the principle of least privilege is upheld across the organization's digital assets.

**Parameters:**

_Basic Parameters:_

- Name: BusinessRole_FromForm
  - Description: Specifies the business role intended to be removed from the user. This parameter is crucial as it directly influences which role is targeted for removal during the workflow execution.
  - Default value: N/A
  - Mandatory: yes

_Advanced Parameters:_

- Name: EnableAffectedRoles
  - Description: This parameter determines whether the workflow should consider other roles that might be affected by the removal of the specified business role. When set to true, the workflow ascertains the impact on dependent roles.
  - Default value: N/A (as it depends on specific implementation and organizational policies)
  - Mandatory: no

- Name: EnableApplyRolesToUser
  - Description: Dictates whether the changes regarding role removal should be applied directly to the user. This parameter is integral to the operational flow, determining if the removal procedure is to be executed or merely simulated.
  - Default value: N/A (dependent on organizational need and workflow configuration)
  - Mandatory: no

**Business impact:** Removing unnecessary or outdated business roles from users plays a fundamental role in maintaining operational security and compliance within an organization. It ensures users have only the access necessary for their current roles and responsibilities, minimizing the risk associated with excessive privileges. This operation supports governance, risk, and compliance (GRC) initiatives by enforcing the principle of least privilege and aiding in the management of internal controls.

**Example of usage:** A scenario involving the usage of this action might involve an HR department initiating a request to remove a "Finance Auditor" role from an employee who has been reassigned from the finance department to the human resources department. The workflow would be executed with the employee's ID and the specific role ("Finance Auditor") as input parameters, ensuring the employee's access rights are updated to reflect their new position.

**Prerequisites:** To execute the `RemoveBusinessRoleToUserAction`, the following preconditions must be met:
- The user initiating the request must have adequate permissions to modify user roles within the Pathlock Cloud platform.
- The specified business role must exist in the system's role catalog.
- The user from whom the role is to be removed must be correctly identified and exist within the system.

**Error Handling and Troubleshooting:**

_Common Error Scenarios:_

- **Role Not Found:** If the specified business role does not exist in the system, verify the role name for accuracy and reattempt the operation.
- **User Not Found:** Ensure the specified user ID is correct and corresponds to an existing user.
- **Insufficient Permissions:** If the operation fails due to permissions, verify that the account executing the action has adequate rights to modify roles.

_Recommended Solutions:_

- Double-check parameter values for accuracy.
- Review the executing user's permissions to ensure they align with the operation's requirements.
- Consult system logs for detailed error information to aid in troubleshooting.

