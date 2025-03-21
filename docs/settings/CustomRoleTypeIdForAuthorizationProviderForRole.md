# Custom Role Type Id For Authorization Provider For Role

**Technical Name:** CustomRoleTypeIdForAuthorizationProviderForRole

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:** A parameter used to identify custom role types within the authorization provider specifically for roles. It is critical in differentiating and identifying roles within the system for appropriate access and permissions settings.

**Business Impact:** Configuring this parameter correctly ensures that users are granted the correct permissions according to their roles, which is essential for maintaining the integrity of secure access within the organization. Incorrect configurations could lead to unauthorized access or denial of access to legitimate users, impacting both security and productivity.

**Technical Impact when configured:** Allows the system to correctly map roles to permissions and access controls within applications managed by the Pathlock GRC platform, ensuring that security policies are enforced consistently.

**Examples Scenario:** An organization implements a new set of custom roles within their ERP system that requires specific permissions different from the standard roles. By setting the `CustomRoleTypeIdForAuthorizationProviderForRole`, the system can recognize these new roles and apply the correct access policies to users assigned to them.

**Related Settings:**

**Best Practices:** 

- **Configure when:** introducing new custom roles within your systems that require distinct access controls from existing roles.
- **Avoid when:** using standard roles that are already recognized and properly managed by the Pathlock GRC platform.