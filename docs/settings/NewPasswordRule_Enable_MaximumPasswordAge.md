# Enable Maximum Password Age

**Technical Name:** NewPasswordRule_Enable_MaximumPasswordAge

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

Enables the enforcement of a maximum password age policy. This setting requires passwords to be changed after a specified period, ensuring that older passwords are regularly updated for heightened security.

**Business Impact:**

Implementing a maximum password age policy enhances account security by mandating periodic password changes. This practice reduces the risk of unauthorized access from compromised credentials, thus protecting sensitive business data and resources.

**Technical Impact when configured:**

Upon activation, this setting obligates users to update their passwords after the age limit is reached. It prevents the use of a password that contains the username, thereby increasing the complexity and security of user passwords.

**Examples Scenario:**

- **Scenario:** A company implements this parameter to ensure that all employee passwords must be changed every 90 days. This reduces the window of opportunity for compromised credentials to be misused.
  
  **Benefit:** Enhances security by minimizing the risk of older, possibly compromised passwords being used to gain unauthorized access.

**Related Settings:**

- SM20DrillDownTransactions
- MaxReplaceTemplateValusCounter

**Best Practices:** 

- **Configure when:** You want to enhance the security of your system by ensuring that passwords are changed regularly.
- **Avoid when:** Your organization uses alternative security measures that may conflict with frequent password changes, or if such changes significantly disrupt user workflows.