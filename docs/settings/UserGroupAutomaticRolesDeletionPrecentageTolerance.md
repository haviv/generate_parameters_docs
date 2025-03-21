# User Group Automatic Roles Deletion Percentage Tolerance

**Technical Name:** UserGroupAutomaticRolesDeletionPrecentageTolerance

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the tolerance level for automatic deletion of roles within user groups. It defines the percentage of roles that can be automatically removed based on dynamic user group rules calculations. This is particularly relevant in environments where user roles and permissions are frequently updated and need to be kept in sync automatically.

**Business Impact:**

Misconfiguration of this parameter can lead to unintentional mass deletion of user roles, potentially hindering access to critical applications or data. On the other hand, a well-configured tolerance can ensure that user roles are accurately reflected, enhancing security and compliance by automatically adjusting users' access rights.

**Technical Impact when configured:**

- **Correct Configuration:** Ensures that the automatic adjustment of user roles does not exceed the specified tolerance, preventing significant unexpected changes in user access rights.
- **Misconfiguration:** May either prevent necessary updates to user access rights or result in unwanted mass deletions of user roles if the tolerance is set too low or too high, respectively.

**Examples Scenario:**

Suppose an organization implements a policy where roles are dynamically adjusted at the end of each quarter based on user activity and group participation metrics. By setting the User Group Automatic Roles Deletion Percentage Tolerance to a reasonable percentage (e.g., 5%), the system will automatically remove roles that are no longer necessary, but will prevent mass deletion, ensuring no more than 5% of the roles are removed at any calculation cycle, maintaining the balance between security and flexibility.

**Related Settings:** 

- DynamicCalculatedUserGroupRulesService
- CalculateUsers

**Best Practices:** 

- **Configure when:** there is a need for dynamic user role management, and there is confidence in the underlying role calculation logic.
- **Avoid when:** user roles are relatively static, or the automatic calculation rules have not been thoroughly tested and verified.