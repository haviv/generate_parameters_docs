# Enable Password History

**Technical Name:** NewPasswordRule_Enable_PasswordHistory

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:**

The `Enable Password History` setting is designed to enhance security by preventing users from reusing their previous passwords. When enabled, the system will check the user's new password against a store of their recent passwords to ensure it has not been used before within a specified period or number of password changes.

**Business Impact:**

Implementing this setting can significantly reduce the risk of unauthorized access stemming from password compromises. It encourages users to create unique passwords at each change interval, thus mitigating the threat posed by attackers who may have gained access to a user's past passwords. This policy is crucial for maintaining user account security and protecting sensitive business information.

**Technical Impact: when configured**

Upon configuration, the system will validate each new password against a database of the user's previous passwords. If the new password matches any within the history constraint, the change will be rejected, and the user will be prompted to create a new password that meets the organization's security standards.

**Examples Scenario:**

For instance, if an organization sets the password history constraint to remember the last five passwords, the system will prevent the user from reusing any of his or her last five passwords. This policy compels the user to come up with a fresh password that hasn't been used recently, thereby enhancing the account's security.

**Related Settings:**

- `NewPasswordRule_Enable_MaximumPasswordAge`
- `NewPasswordRule_MaximumPasswordDays`

**Best Practices:** configure when implementing a robust password policy to enhance security. Avoid when the system does not have the capability to securely store and manage password histories, or if the policy does not align with organizational needs and practices.