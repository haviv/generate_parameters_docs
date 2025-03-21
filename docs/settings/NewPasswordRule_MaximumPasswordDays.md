# Maximum Password Age (days)

**Technical Name:** NewPasswordRule_MaximumPasswordDays

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

The Maximum Password Age parameter defines the maximum number of days a password can be used before it must be changed. This setting enforces password updates regularly, enhancing the security posture by minimizing the window of opportunity for password-related attacks.

**Business Impact:**

Implementing a Maximum Password Age policy ensures that credentials are refreshed periodically, reducing the risk of prolonged access by unauthorized users who might have compromised a password. It supports compliance with security best practices and regulatory requirements, helping prevent potential data breaches and maintaining trust in organizational security measures.

**Technical Impact when configured:**

When this parameter is configured, users will be required to update their passwords after the specified number of days has passed. If not updated, the user may be locked out of their account or lose access to certain resources, until a new password is set. This prompts users to create new, strong passwords at regular intervals, thereby reducing the risk of security breaches due to compromised, reused, or old passwords.

**Examples Scenario:**

- **Scenario 1:** To comply with industry-standard security policies, a financial institution sets the Maximum Password Age to 90 days to ensure all staff members change their passwords within this period, reducing the risk of unauthorized access to sensitive financial data.

**Related Settings:**

- `NewPasswordRule_Enable_MaximumPasswordAge`

**Best Practices:** 

- **Configure when:** Regular password changes are a necessary part of your organization's security policy to meet compliance and security standards.
- **Avoid when:** Users utilize systems where frequent password changes can significantly disrupt workflows or systems that employ alternate, strong authentication methods that make frequent password changes redundant or less effective.