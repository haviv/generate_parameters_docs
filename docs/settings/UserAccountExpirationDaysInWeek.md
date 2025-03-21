# User Account Expiration Days In Week

**Technical Name:** UserAccountExpirationDaysInWeek

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The User Account Expiration Days In Week parameter specifies the number of days within a week before a newly created user account expires if not activated. It is a key setting within the Pathlock Cloud GRC platform's user management workflow, especially regarding controls around temporary or contingent access.

**Business Impact:**

Setting an appropriate expiration period helps in managing risk by ensuring that temporary accounts do not remain active beyond their needed duration, thus minimizing potential security vulnerabilities. It aids in enforcing policies around the lifecycle of access rights, thereby supporting compliance with internal and external audit requirements.

**Technical Impact when configured:**

When this parameter is configured, it directly impacts how long a new user's account remains valid without activation. It influences the workflow of onboarding new users by enforcing a timeframe for account activation and reducing the risk associated with inactive accounts.

**Examples Scenario:**

- **Scenario:** A company has a policy that new user accounts must be activated within the first week after creation to access the system. By setting the User Account Expiration Days In Week parameter to 7, administrators can automate enforcement of this policy, ensuring that new accounts that haven't been activated within a week are flagged or automatically disabled, thus upholding the company's security standards.

**Related Settings:**

- Workflow UI
- EmailBodyContentFileName

**Applicable Workflows Actions:**

- CreateNewUser

**Best Practices:** 

- **Configure when:** Setting up new user onboarding workflows, especially in environments where there is a high turnover or a significant number of temporary/contract employees.
  
- **Avoid when:** In scenarios where users may require more time to activate their accounts due to extended onboarding processes or when dealing with external users who might not access the system immediately. Alternative measures should be considered to manage these accounts safely.