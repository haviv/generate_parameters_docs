# Roles Spllitter Roles Child Role Pattern

**Technical Name:** RolesSplliterRolesChildRolePattern

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls how child roles are identified and patterned during the role splitting process in the Pathlock Cloud GRC platform. It is used to distinguish between child roles based on naming conventions, aiding in the accurate segmentation and management of roles.

**Business Impact:**

Proper configuration of this parameter ensures a streamlined role governance process, facilitating the easier identification, assignment, and auditing of roles within the organization. It impacts how effectively role-based access controls are implemented and managed, directly affecting the organization's security posture and compliance with internal and external policies.

**Technical Impact when configured:**

- Ensures the correct identification and categorization of child roles based on specified naming patterns.
- Helps in maintaining a clean and organized role structure, which simplifies access management and auditing.
- Aids in automating the role provisioning and de-provisioning processes by accurately identifying roles that fit specific patterns.

**Examples Scenario:**

In an organization, roles are named with prefixes indicating their category, such as "_C" for compliance roles and "_S" for security roles. The organization wants to automate the provisioning of access rights such that any new or updated role containing the "_C" prefix is automatically assigned to users in the compliance department. By configuring `RolesSplliterRolesChildRolePattern` appropriately, the Pathlock Cloud GRC platform can identify and act on these roles correctly, ensuring users have the necessary access without manual intervention.

**Related Settings:** RolesSplliterRolesPrefix

**Best Practices:** configure when the organization has a complex role structure with clear naming conventions to ensure roles are easily identifiable and manageable. Avoid when role names are too dynamic or do not follow a consistent pattern, as misconfiguration may lead to roles being incorrectly categorized or overlooked.