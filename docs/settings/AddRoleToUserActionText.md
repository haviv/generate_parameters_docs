# Add Role To User Action Text

**Technical Name:** AddRoleToUserActionText

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:** This parameter defines the textual representation used in workflows to denote the action of adding a role to a user. It is a key part of both creating new users and applying authorization changes, as it specifies how roles are designated in the system's XML structure.

**Business Impact:** Accurate configuration of this parameter ensures that roles are correctly assigned to users, which is critical for managing access permissions, enforcing security policies, and maintaining compliance with regulatory requirements. Misconfiguration could lead to improper access control, posing potential security risks.

**Technical Impact when configured:** Proper configuration of the `AddRoleToUserActionText` parameter ensures that the system can correctly interpret and execute actions related to the assignment of roles within workflow processes such as user creation and authorization application. This supports the enforcement of least privilege access and aids in efficient user management.

**Examples Scenario:** When a new user is created in the Pathlock platform and needs to be assigned specific roles based on their job function, the `AddRoleToUserActionText` parameter is used to define how these roles are identified and assigned within the system. Similarly, when a user's authorizations need to be updated, this parameter helps define the textual framework within which the changes are structured.

**Related Settings:** 

- `XmlResource.Request`
- `XmlResource.Roles`
- `XmlResource.Role`
- `XmlResource.RoleId`

**Best Practices:** 

- **Configure when:** You are setting up the Pathlock platform for initially managing user roles and permissions, or when modifying how roles are assigned to users within workflow processes.
  
- **Avoid when:** Not applicable, as this is a critical parameter for user and authorization management within the Pathlock platform.