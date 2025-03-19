# Create Derived Role Action

**Category:** User Management

**Description:** 

The Create Derived Role Action is designed to automate the process of creating new derived roles within an identity and Governance, Risk, and Compliance (GRC) platform, similar to functionalities found in Sailpoint and Savynt. This action takes an original role and generates a new role with specific organizational values and attributes, thereby aiding in the hierarchical structuring of role-based access controls. The flow initiates by building a `RoleAuthorizationChanges` object from input parameters, setting the role name either based on the original derived role or filling it from organizational levels. If not a test run, the action updates the role with the new parameters in the system and refreshes the role data.

**Parameters:** 

_Basic:_

- Name: RoleName
  Description: The name of the role to be created or updated. If the role name includes placeholders (identified by `$$`), they are replaced with organizational values.
  Default value: (None)
  Mandatory: No

- Name: NewParentRole
  Description: The name of the master or parent role from which the new derived role is to be created. This parameter is essential for inheriting access privileges from the parent role.
  Default value: (None)
  Mandatory: Yes

- Name: OriginalRoleName
  Description: The name of the original role from which the derived role is to be generated. This helps in maintaining a lineage and understanding the role evolution.
  Default value: (None)
  Mandatory: No

_Advanced:_

- Name: DestSystemId
  Description: Specifies the target system identifier where the role is to be created or updated. This allows for the role changes to be applied to the correct system within a multi-system environment.
  Default value: SystemId of the current context
  Mandatory: No

- Name: IsTestRun
  Description: A boolean parameter that indicates whether the action should be executed as a test run. If true, the system does not commit the role updates.
  Default value: false
  Mandatory: No

**Business impact:** 

This action supports the secure and efficient management of role-based access controls by automating the role derivation process, ensuring that users have appropriate access rights based on their organizational role and function. It simplifies the process of creating roles that adhere to security and compliance standards, reducing manual errors and administrative overhead.

**Example of usage:** 

A scenario where a company needs to create a new derived role for a specific department within the organization, inheriting certain privileges from a parent role but with department-specific modifications. The company could use the Create Derived Role Action to specify the parent role, the organizational values that distinguish the new role, and optionally, if it's a test run before finalizing the role in the system.

**Prerequisites:** 

- The user must have administrative privileges or relevant permissions within the GRC platform to create or update roles.
- A parent role must exist if creating a derived role that inherits from it.
- Organizational values must be predefined if they are to be incorporated into the new role name or attributes.

**Error Handling and Troubleshooting:** 

- *Error:* Role name not specified
  *Cause:* Neither `RoleName` nor `OriginalRoleName` was provided.
  *Solution:* Ensure that either a new role name or an original role name from which to derive the new role is supplied.

- *Error:* Update failed on the target system
  *Cause:* Could be due to a lack of permissions or incorrect `DestSystemId`.
  *Solution:* Verify that the `DestSystemId` is correct and the user has sufficient permissions to update roles on the target system.