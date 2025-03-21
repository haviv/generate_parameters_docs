# Authorization Review By Role Job Roles And Activity Disable Role Include

**Technical Name:** AuthorizationReviewByRoleJobRolesAndActivityDisableRoleInclude

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to include or exclude roles within the scope of authorization reviews based on their job roles and activities. When enabled, it allows for a finer granularity in the review process by considering the specific activities and job roles associated with the roles.

**Business Impact:**

Enabling this parameter can significantly enhance the security posture by ensuring that only relevant roles are included in the authorization review process. This targeted approach helps in mitigating risks associated with excessive or inappropriate permissions, thereby enhancing overall compliance and security.

**Technical Impact when configured:**

Once configured, this parameter affects how roles are selected for review in the authorization process. Roles that match the specified job roles and activities criteria are included, while others are excluded. This ensures that the authorization review is more focused and efficient, reducing the overhead of reviewing irrelevant roles.

**Examples Scenario:**

In a scenario where an organization wants to review the authorization of roles involved in financial transactions, this parameter can be configured to include only those roles with job roles and activities related to financial operations. This ensures that the review process is concentrated on roles with potential financial impact while excluding unrelated roles, thus enhancing the effectiveness of the review process.

**Related Settings:**

- CustomRoleTypeIdForAuthorizationProviderForRole

**Best Practices:** 

- **Configure when:** There is a need for targeted authorization reviews that focus on specific job roles and activities within the organization. This is particularly useful in large organizations with diverse roles and permissions.
  
- **Avoid when:** The organization prefers a broad and comprehensive review that covers all roles without focusing on specific activities or job roles. This may be the case in smaller organizations or when conducting a high-level audit.