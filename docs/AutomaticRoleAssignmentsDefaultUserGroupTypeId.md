# Automatic Role Assignments Default User Group Type

**Technical Name:** AutomaticRoleAssignmentsDefaultUserGroupTypeId

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter controls the default user group type used in automatic role assignments within the Pathlock Cloud GRC platform. It is utilized specifically within the context of assigning roles to user groups dynamically based on specified criteria or conditions.

**Business Impact:**

Proper configuration of this parameter ensures that the correct user groups are targeted for automatic role assignments, enhancing both the efficiency and compliance of access control within the organization. Misconfiguration may lead to inappropriate access rights being granted or denied, potentially affecting the security posture and compliance status.

**Technical Impact when configured:**

When appropriately configured, this ensures that roles are automatically assigned to the intended user groups based on the organization's security policies and compliance requirements. This automation streamlines user access management, reducing the administrative burden and the risk of human error.

**Examples Scenario:**

- **Setting up automatic role assignment for a new software deployment:** When a new software tool is deployed across the organization, specific roles may need to be automatically assigned to certain user groups. By configuring this parameter to target the correct user group type, the system can automatically assign these roles based on predefined criteria, ensuring a smooth and secure rollout.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:** Setting up dynamic role assignment rules to ensure that the automated system aligns with organizational policies and access requirements.
  
- **Avoid when:** The criteria for automatic role assignments are unclear or the roles do not directly correspond to specific user groups, which could lead to misassignment of permissions.