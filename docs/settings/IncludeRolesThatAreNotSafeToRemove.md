# Include Roles That Are Not Safe To Remove

**Technical Name:** IncludeRolesThatAreNotSafeToRemove

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether roles that are not safe to remove are included in workflow processes for role removal. It ensures that roles critical to system operations or user responsibilities are accounted for during automated role management tasks.

**Business Impact:**

Activating this setting can mitigate the risk of inadvertently removing roles essential for business operations, compliance requirements, or security policies. It helps in maintaining operational integrity and compliance with regulatory standards by safeguarding necessary roles.

**Technical Impact when configured:**

When enabled, the system includes roles that are identified as not safe to remove in the removal workflow process. This requires additional scrutiny and approval before such roles can be removed from users, reducing the likelihood of impacting critical business operations or security postures.

**Examples Scenario:**

- When performing mass role removals as part of a system cleanup or downgrade, you may want to ensure that roles crucial to system security or user jobs are not accidentally removed. Enabling this feature will flag such roles for review before removal.

**Related Settings:** N/A

**Best Practices:** Configure this setting when undertaking broad role management and cleanup activities to protect essential roles. Avoid turning this on for routine operations to prevent workflow congestion.