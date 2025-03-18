# Automatic User Lock Override Disable Default Action

**Technical Name:** AutomaticUserLockOverrideDisableDefaultAction

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:**

The **Automatic User Lock Override Disable Default Action** parameter is designed to enhance the security posture of an organization by providing an option to disable the default action for automatically overriding user locks. This parameter becomes crucial in scenarios where additional control and confirmation are required before unlocking a user account, specifically those locked out due to incorrect login attempts, or periods of inactivity.

**Business Impact:**

Enabling this parameter helps organizations mitigate the risk of unauthorized access by ensuring that user accounts, locked due to security policies like incorrect login attempts or inactivity, are not automatically unlocked without proper verification. This supports compliance with strict security standards and reduces the potential for compromise.

**Technical Impact: when configured**

When configured, this parameter prevents automatic unlocking actions from being applied to user accounts that have been locked. It requires manual intervention or an alternative, specified workflow action to unlock the user account. This adds an additional layer of security by ensuring that each unlock action is intentional and authorized.

**Examples Scenario:**

- An organization faces regulatory compliance requirements that mandate strict control over user account unlock procedures. Activating this parameter ensures compliance by necessitating manual review or a specified workflow action before any locked account is unlocked, especially after multiple failed login attempts or extended periods of inactivity.
  
- To protect against brute force attacks where an attacker might benefit from automated unlocking policies, an organization activates this parameter to require manual intervention, significantly increasing the security of user accounts.

**Related Settings:**

- **AutomaticLockUserEnableWorkflowAction:** Determines if the workflow action to lock users automatically is enabled.
- **AutomaticUserLockIncludeUsersLockedByIncorrectLogons:** Specifies if users locked out due to incorrect login attempts should be included in the automatic lock and unlock processes.

**Best Practices:** 

- **Configure when:** Enhanced security around user account management is necessary, especially in highly regulated environments or sectors with stringent data protection requirements.
- **Avoid when:** The organization has mature automated processes that do not require this additional layer of security, or user account lockout management does not represent a significant security threat.