# Automatic User Lock Include Users Locked By Incorrect Logons

**Technical Name:** AutomaticUserLockIncludeUsersLockedByIncorrectLogons

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether users who have been locked out due to incorrect logon attempts are included in automatic lockout processes. Enabling this feature enhances security by ensuring that users who fail multiple login attempts are not able to access the system, even if the automatic user lock process is triggered.

**Business Impact:**

Enabling this parameter significantly improves the security posture by preventing potential unauthorized access. In environments where security compliance is crucial, this setting helps in maintaining a stringent access control mechanism, reducing the risk of security breaches.

**Technical Impact when configured:**

When activated, any user account that is locked out due to incorrect logon attempts will be included in the automatic user lock process. This ensures a comprehensive approach to user account security by combining the responses to various user account incidents into a cohesive security strategy.

**Examples Scenario:**

In a scenario where an organization faces constant threat from brute force attacks, enabling this parameter would provide an additional layer of security. If an attacker tries multiple incorrect logon attempts and gets locked out, this setting ensures the user account remains locked even if there's an automatic unlock process in place, thereby preventing unauthorized access.

**Related Settings:**

- `AdditionalAdminMailRecipients`
- `CanBeLockedUserTypes`
- `NonUsageDayLocking`
- `AutomaticLockUserEnableWorkflowAction`

**Best Practices:** 

- **Configure when:** The organization requires a robust security mechanism to automatically manage user accounts that display suspicious login behaviors.
  
- **Avoid when:** If the setting might cause operational disruptions, for instance in environments where users frequently lock themselves out due to forgotten passwords but pose no security risk.