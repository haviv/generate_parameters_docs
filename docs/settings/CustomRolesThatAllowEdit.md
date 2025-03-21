# Custom Roles That Allow Edit

**Technical Name:** CustomRolesThatAllowEdit

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The parameter "CustomRolesThatAllowEdit" is utilized within the Pathlock Cloud GRC platform to define and control which custom roles are granted the permission to edit certain modules or settings. This is critical for maintaining the integrity and security of the configurations, ensuring that only authorized users can make changes.

**Business Impact:**

Restricting edit access to sensitive settings and modules to only those users with custom roles specifically allowed to edit, ensures that inadvertent or unauthorized changes are minimized. This plays a significant role in preserving the organization's compliance stance and mitigating risk related to security configurations and sensitive information handling.

**Technical Impact when configured:**

When this parameter is configured, the system dynamically checks if the currently accessed module by a user falls under the specified custom roles that allow edit permissions. If the user's role matches, edit capabilities are granted; otherwise, they are restricted from making changes. This ensures a granular level of access control within the platform, directly influencing the system's overall security posture.

**Examples Scenario:**

If an organization wishes to restrict editing capabilities on the financial reporting module to only senior finance managers and above, "CustomRolesThatAllowEdit" can be configured to include only the roles associated with those positions. This way, even if other users have access to view these reports, they cannot modify them without the appropriate role designation.

**Related Settings:**

- RoleSystem.ConfigurationEditRole

**Best Practices:** configure when, avoid when 

- **Configure when:** You need to ensure tight control over who can make changes to critical system configurations and sensitive information.
- **Avoid when:** Every user of the system needs equal access to edit capabilities, which is rarely a recommended security practice.