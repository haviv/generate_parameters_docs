# Add Business Role To User

**Category:** User Management

**Description:** The "Add Business Role To User" action is designed to assign specific business roles to users within the system, enhancing user lifecycle management by dynamically adapting access rights and roles based on the organization's governance policies. This action assesses the validity of targeted users and roles, applying the specified business role to the user if both are validated, with an option to define an expiration date for the role assignment. It supports both singular and bulk updates across systems, allowing for nuanced control over access provisioning in a compliance-conscious environment.

**Parameters:**

_Basic:_

- Name: EnableAffectedRoles
  - Description: Controls whether roles affected by the workflow should be identified and processed.
  - Default value: `false`
  - Mandatory: no

- Name: EnableApplyRolesToUser
  - Description: Determines if the designated roles should be directly applied to the user.
  - Default value: `false`
  - Mandatory: no

- Name: BusinessRole_FromForm
  - Description: Specifies the business role to be added to the user, identified by name.
  - Default value: `null`
  - Mandatory: yes

_Advanced:_

- Name: SingleSystem
  - Description: Flag to apply the role change on a single, specified system, enabling targeted role assignments.
  - Default value: `false`
  - Mandatory: no

- Name: AllSystems
  - Description: Flag to apply the role change across all systems, enabling widespread role assignments.
  - Default value: `false`
  - Mandatory: no

- Name: BusinessRole_UntilDate
  - Description: The expiration date of the assigned role, allowing for time-bound access management.
  - Default value: `null`
  - Mandatory: no

**Business impact:** Implementing this action streamlines the process of managing user roles and access rights, significantly reducing manual overhead and enhancing security by ensuring only authorized individuals have access to critical systems and data. It supports compliance with internal and external audit requirements by enabling precise control and reporting of user access.

**Example of usage:** 

To assign a business role named "Data Analyst" to an employee with ID `EMP123` until the end of the year, the workflow would be configured with the following parameters:

- EnableApplyRolesToUser: `true`
- BusinessRole_FromForm: "Data Analyst"
- BusinessRole_UntilDate: `12/31/2023`

This configuration will automatically validate and assign the "Data Analyst" role to `EMP123`, ensuring the role expires at the specified date.

**Prerequisites:** 

1. The executing user must have sufficient permissions to modify user roles within the system.
2. Target users and roles must exist within the system's database prior to execution.
3. Workflow settings must be properly configured to allow dynamic role assignment actions.

**Error Handling and Troubleshooting:** 

- Common Error: Employee or role not found
  - Cause: The specified employee ID or role name does not exist in the database.
  - Solution: Verify the employee ID and role name for accuracy and ensure they exist within the system.
  
- Common Error: Role assignment failed
  - Cause: Insufficient permissions or system configuration prevents the application of the role to the user.
  - Solution: Check the executing user's permissions and the system's role assignment settings.

For further troubleshooting, consult the system's event logs and contact technical support for assistance with complex issues not resolved through initial checks.