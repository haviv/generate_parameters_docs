# Minimum Password Age (days)

**Technical Name:** NewPasswordRule_MinimumPasswordDays

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

The Minimum Password Age parameter dictates the minimum number of days a user must wait before they are allowed to change their password again. This setting is designed to prevent users from bypassing password history requirements by immediately changing their password multiple times.

**Business Impact:**

Implementing a minimum password age can significantly enhance an organization's security posture by ensuring that passwords are not changed too frequently. This approach helps in maintaining the effectiveness of password history and avoiding the reuse of recent passwords, which can be a common vector for security breaches.

**Technical Impact: when configured**

When configured, this parameter enforces a delay before passwords can be changed again, thereby helping to prevent rapid, repeated changes that could allow users to circumvent other password security measures like password history checks.

**Examples Scenario:**

A company has set the Minimum Password Age to 5 days. This means once users update their password, they cannot change it again for another 5 days. This prevents employees from changing their password back to an old, possibly compromised one soon after a mandatory password reset, enhancing overall security.

**Related Settings:**

- `NewPasswordRule_Enable_PasswordMustNotContainUsername`
- `NewPasswordRule_Enable_MinimumPasswordAge`

**Best Practices:** configure when the organization seeks to strengthen its password policy and security measures. Avoid setting the minimum password age too high as it may cause inconvenience to users, especially in cases where a password change is urgently needed due to a suspected security breach.