# Number of Historic Passwords to Compare with New Password

**Technical Name:** NewPasswordRule_NumberOfPasswordsInHistory

**Category:** Security

**Default Value:** Not specified

**Impact Level:** High

**Description:**

This parameter is designed to enforce password history policies within the Pathlock Cloud GRC platform. When enabled, it prevents users from reusing their previous passwords by specifying how many of the user's past passwords the new password must be unique from.

**Business Impact:**

Implementing this parameter strengthens an organization's security posture by mitigating the risks associated with the reuse of old passwords. It ensures that users regularly update their passwords to new, unique ones, thus reducing the likelihood of successful brute force or dictionary attacks.

**Technical Impact when configured:**

After configuration, the system checks the new password against a specified number of the user's most recent passwords. If the new password matches any within the defined history, the system rejects it, prompting the user to choose a different password.

**Examples Scenario:**

A company requires that its employees' new passwords must be different from any of the last six passwords used. By setting this parameter to 6, when employees update their passwords, the system ensures that the new password is not the same as any of the last six passwords used by the respective user.

**Related Settings:**

- `NewPasswordRule_Enable_PasswordHistory`
- `NewPasswordRule_MaximumPasswordDays`

**Best Practices:** configure when, avoid when

- **Configure when:**
  - You want to enforce a robust password policy that prevents the reuse of passwords. This is particularly important for organizations with stringent security and compliance requirements.
- **Avoid when:**
  - Users frequently change passwords or if there is a minimal risk associated with password reuse. Overly strict history requirements may lead to diminished user experience or an increase in password reset requests.