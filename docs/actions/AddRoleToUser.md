### AddRoleToUser

**Category:** User Management

**Description:** The `AddRoleToUser` action is designed to automate the assignment of roles to users within the Pathlock platform. This action is crucial for managing access and permissions efficiently and supports dynamic role assignment based on specific requests or predefined criteria. Through a series of conditional checks and parameter evaluations, this action can assign requested roles directly from user requests or add custom roles as specified by the workflow parameters. The action supports both individual and batch role assignments and includes an error handling mechanism to log issues and provide feedback for troubleshooting.

**Parameters:**

- Basic:
    - Name: `AddRoleFromRequest`
    - Description: Indicates whether to add the role specified in a user's request to the user.
    - Default value: `false`
    - Mandatory: No
    
    - Name: `RequestedRole`
    - Description: Specifies the role to be added to the user if `AddRoleFromRequest` is true. It is used directly to assign a specified role to the user based on a request parameter.
    - Default value: (none)
    - Mandatory: No
    
    - Name: `Custom_Roles_Add`
    - Description: Allows for adding a role to the user that is not specified in the initial request, facilitating custom role assignments beyond the requested scope.
    - Default value: (none)
    - Mandatory: No
    
- Advanced:
    - Name: `IgnoreAdditionalRequestedRoles`
    - Description: Controls whether additional roles specified in the user's request beyond the initially requested role should be ignored.
    - Default value: `false`
    - Mandatory: No
    
    - Name: `OnlyAssignRolesInCurrentSystem`
    - Description: Limits the role assignment to the system currently being processed, ensuring that roles are not inadvertently assigned across multiple systems.
    - Default value: `false`
    - Mandatory: No

**Business impact:** Implementing the `AddRoleToUser` action within workflow automations significantly enhances operational efficiency in user access management. It reduces manual processing time, minimizes the risk of human error, and ensures that access rights align with organizational policies and compliance requirements. Specifically, it facilitates the dynamic and context-sensitive assignment of roles, thereby supporting granular access control and streamlined user onboarding and offboarding processes.

**Example of usage:** To automate the process of adding a role to a user based on specific request parameters, configure the `AddRoleToUser` action within a workflow to listen for role assignment requests. When a request is captured, specify whether to extract the role from the request directly using `AddRoleFromRequest` or to assign a predefined role specified in `RequestedRole`.

**Prerequisites:** Users executing this action must have administrative privileges to assign roles and access to the workflow management interface. Additionally, the relevant roles and user information must be preconfigured in the system, ensuring accurate assignments.

**Error Handling and Troubleshooting:**

- Common Error Scenario: Role does not exist
    - Probable Cause: The role specified for assignment is not defined within the system.
    - Recommended Solution: Verify that the role name is correct and exists within the system. If the role is missing, create the role before attempting to assign it again.
    
- Common Error Scenario: System connector issue
    - Probable Cause: Failure in the system connector operation while attempting to assign the role to the user.
    - Recommended Solution: Check the system connector configuration and logs for any errors. Ensure that the system connector is correctly set up and that there are no issues with network connectivity or permissions.