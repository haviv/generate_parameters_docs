# Show Default Roles For External Users

**Technical Name:** ShowDefaultRolesForExternalUsers

**Category:** General - UI

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether default roles are displayed for external users within the Pathlock Cloud GRC platform user interface. It ensures that administrators can easily manage and review default roles assigned to external users, which is crucial for maintaining system security and compliance.

**Business Impact:**

Ensuring that default roles for external users are correctly managed and visible when necessary helps in maintaining strict access control policies. It directly impacts the organization's ability to protect sensitive information from unauthorized access, align with regulatory compliance requirements, and efficiently manage user permissions.

**Technical Impact when configured:**

When this parameter is enabled, administrators will have the visibility of default roles assigned to external users, thus improving audit trails and accountability. It simplifies the management of external user permissions and aids in the enforcement of least privilege principles by ensuring only the necessary access rights are assigned.

**Examples Scenario:**

An organization needs to periodically audit the access rights of external users, such as contractors or partners, to ensure they comply with the principle of least privilege. By enabling this parameter, administrators can quickly verify if the default roles assigned to these external users align with their current job requirements and the organization's security policies.

**Related Settings:**

- ShowAuthorizationFieldInRoleUsage
- ShowCreationDateInUserCard 

**Best Practices:** 

- Configure when: It's beneficial to enable this setting in environments where external users are frequently granted access to internal resources, and there's a need for stringent access control and compliance adherence.
  
- Avoid when: If the organization does not utilize external user roles or if detailed tracking and visibility of these roles are managed through another system or process.