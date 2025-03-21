# External User Role

**Technical Name:** ExternalUserRole

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter represents roles assigned to external users within the system, determining their access and interaction capabilities with Pathlock Cloud GRC's resources and data.

**Business Impact:**

Effectively using the ExternalUserRole ensures that external users, such as contractors or partners, have appropriate access rights, which is crucial for maintaining data security and compliance. Misconfiguration could lead to unauthorized access or restriction to necessary data, impacting business operations and compliance posture.

**Technical Impact when configured:**

- Enables granular access control by defining what external users can or cannot do within the system.
- Assists in the enforcement of the principle of least privilege by ensuring external users have only the access necessary to perform their roles.
- Aids in audit and compliance efforts by providing clear mapping of external user roles to their access rights.

**Examples Scenario:**

An organization needs to grant limited system access to an external auditor for compliance verification. By assigning an appropriate ExternalUserRole, the auditor can access necessary information without compromising sensitive data or internal controls.

**Related Settings:** ExternalDatabaseEmployeesSelectQuery

**Best Practices:** 

- Configure ExternalUserRole with clear definitions and restrictions to ensure external users can perform their necessary tasks without exceeding their intended scope of access.
- Avoid assigning overly permissive roles to external users to minimize security risks and ensure compliance with data protection regulations.