# CRM Role Prefix

**Technical Name:** CRM_RolePrefix

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

The CRM Role Prefix parameter is used to define a prefix for CRM role names. This prefix is essential for distinguishing CRM-specific roles from other roles within the system and ensuring that the roles are correctly identified and managed within the Pathlock Cloud GRC platform.

**Business Impact:**

Setting the CRM Role Prefix correctly ensures that CRM roles are properly identified, contributing to more accurate role management and assignment. This leads to enhanced security and compliance postures by ensuring that users have appropriate access rights based on their roles. Incorrect or missing configuration can lead to misidentification of roles, potentially causing unauthorized access or compliance issues.

**Technical Impact when configured:**

When the CRM Role Prefix is configured, it allows the Pathlock Cloud GRC platform to precisely filter and manage CRM roles from non-CRM roles. This configuration supports better alignment between user access rights and their actual job functions, facilitating tighter security and compliance controls.

**Examples Scenario:**

- If "CRM_" is set as the CRM Role Prefix, then any role starting with "CRM_" would be recognized as a CRM role by the system. This makes role assignment more streamlined and reduces the risk of misconfiguration in role-based access control settings.

**Related Settings:** Not Specified

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for the first time or adding new CRM roles. It's crucial for distinguishing CRM-related roles for proper security and compliance management.
- **Avoid when:** If CRM roles do not have a specific naming convention or if the naming convention overlaps with non-CRM roles, it's important to reevaluate the prefix to ensure accurate role identification and management.