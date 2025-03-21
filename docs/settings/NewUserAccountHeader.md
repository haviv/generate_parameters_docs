# New User Account Header

**Technical Name:** NewUserAccountHeader

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

Controls configurations applied during the creation of new user accounts and their subsequent authorization process. Ensures newly created user accounts adhere to specified guidelines and permissions are correctly applied.

**Business Impact:**

Directly influences the operational security and compliance posture by ensuring user accounts are created with appropriate access levels. Supports adherence to principles of least privilege and segregation of duties, critical for audit compliance and minimizing security risks.

**Technical Impact when configured:**

- Streamlines the user onboarding process by automating email notifications and including necessary CC addresses.
- Supports the enforcement of password rules and security standards for new accounts.
- Facilitates the proper allocation of authorizations and roles to new users, ensuring access control policies are maintained.

**Examples Scenario:**

When a new employee joins the organization, the NewUserAccountHeader parameter ensures they receive an automated welcome email with login details. Additionally, the employee is granted access permissions according to their role, applying predefined authorization rules to prevent unauthorized access to sensitive information.

**Related Settings:**

- TechnicalNameForEmployeeFirstNameHebrew
- TechnicalNameForEmployeeLastNameHebrew
- NewPasswordRule_MaximumPasswordDays

**Best Practices:** 

- Configure upon the creation of new user accounts to ensure security policies are enforced from day one.
- Avoid manual configurations for individual accounts to prevent inconsistency in security practices and potential breaches.