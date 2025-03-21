# New User Account Password

**Technical Name:** NewUserAccountPassword

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The New User Account Password parameter specifies the initial password setting for newly created user accounts. This parameter is key in the process of automating user account creation and ensuring that initial access to the system is secure.

**Business Impact:**

Proper configuration of the New User Account Password is crucial for maintaining the security and integrity of the system. A strong default password helps prevent unauthorized access and ensures that new users are prompted to establish their credentials securely.

**Technical Impact when configured:**

When configured, the New User Account Password sets a predefined entry point for new users, which integrates with the system's security protocols to encourage password changes on first login, thus aligning with best practices for account security.

**Examples Scenario:**

Scenario: Onboarding New Employees
- In the process of onboarding, new employees are assigned user accounts within the Pathlock platform. The New User Account Password parameter is used to generate initial passwords. These credentials are then shared with the new hires, who are obligated to change their password upon their first login. This ensures that from their first interaction, the accounts are both personalized and secure.

**Related Settings:**

- NewPasswordRule_MinimumPasswordDays

**Applicable Workflows Actions:** 

- ApplyAuthorizationAction
- CreateNewUser

**Best Practices:**

- **Configure when:** setting up the user account creation process to ensure that all new accounts start with a secure, system-generated password that meets the organization's password policy.
  
- **Avoid when:** if it is not feasible to manage or distribute initial passwords securely, consider implementing an alternative secure method for initial account access that still complies with the organization's security policies.