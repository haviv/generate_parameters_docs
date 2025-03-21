# Password Length

**Technical Name:** PasswordLength

**Category:** Security

**Default Value:** Not specified

**Impact Level:** High

**Description:**

The Password Length parameter specifies the minimum number of characters required for passwords within the Pathlock Cloud GRC platform. This parameter is crucial for enforcing password complexity and strength, making it harder for unauthorized individuals to breach user accounts.

**Business Impact:**

Setting an appropriate Password Length helps in safeguarding sensitive data and system access by ensuring that users create strong passwords. It directly impacts the organization's ability to protect against unauthorized access, thereby reducing the risk of data breaches and compliance violations.

**Technical Impact when configured:**

When configured, the Password Length parameter enforces the creation of new passwords and the updating of existing ones to meet the specified length criteria. It applies during user account creation and password changes, ensuring adherence to the organization's security policies.

**Examples Scenario:**

- **During New User Onboarding:** Ensuring that the new user's passwords are of sufficient length contributes to the overall security posture of the organization from day one.
  
- **Updating Existing User Passwords:** Enforcing a minimum password length when existing users update their passwords helps in maintaining strong security measures over time.

**Related Settings:** 

- ChangeUserPassword
- CreateNewUser

**Applicable Workflows Actions:** 

- ChangeUserPassword
- CreateNewUser

**Best Practices:** 

- **Configure when:** Establishing or updating the organization's password policy to enhance security measures.
  
- **Avoid when:** Such stringent control over password length could potentially lead to a decrease in user convenience or when the organization operates under a policy that emphasizes different aspects of password security, such as multi-factor authentication.