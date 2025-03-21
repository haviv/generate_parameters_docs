# Use Business Roles As Composite Roles

**Technical Name:** UseBusinessRolesAsCompositeRoles

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter controls whether business roles are treated as composite roles during system user data processing and workflow actions. When enabled, it allows for granular control over user access by treating business roles as a collection of underlying technical roles or permissions.

**Business Impact:**

Enabling this parameter can significantly streamline the assignment and management of user permissions, especially in complex environments where roles need to encompass various permissions across multiple systems. It simplifies the governance and compliance processes by ensuring that users have access only to what is necessary for their role, reducing the risk of excessive permissions.

**Technical Impact when configured:**

- Business roles are treated as composite, encapsulating multiple technical roles or permissions.
- Changes in user access rights due to this setting can affect system performance during synchronization processes, as the system recalculates permissions based on composite role definitions.
- May influence the outcome of workflow actions related to user role assignment, such as applying or removing business roles from users.

**Examples Scenario:**

If an organization wants to assign a user to a 'Manager' business role, and this role includes access to financial reports, employee records, and operational databases, enabling this parameter ensures that all associated permissions are granted or revoked in a single action. This approach minimizes manual errors and enhances security by ensuring precise alignment of access rights with user responsibilities.

**Related Settings:**

N/A

**Applicable Workflows Actions:**

- ApplyBusinessRoleChanges
- BusinessRoleToUserActionBase
- RemoveAllRolesFromUser

**Best Practices:** 

- **Configure when:** You have well-defined business roles that encompass specific technical roles or permissions. Ideal for organizations looking to streamline permission management and ensure compliance through precise role definitions.
- **Avoid when:** Your user management processes do not require the aggregation of permissions, or if the additional processing overhead may impact system performance adversely.