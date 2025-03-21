# Check User SoD By Employee Authorizations

**Technical Name:** SoCheckUserSoDByEmployeeAuthorizations

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter enables the Pathlock Cloud GRC platform to check for Segregation of Duties (SoD) violations based on user roles and authorizations by employee. It helps in identifying and mitigating potential security and compliance risks associated with inappropriate combinations of roles assigned to a single user.

**Business Impact:**

Implementing this check ensures that employee access rights are in compliance with company policies and regulatory requirements, reducing the risk of fraud, data breaches, and compliance violations. It supports a strong internal control environment by preventing the assignment of conflicting roles to a user, thus safeguarding sensitive business processes.

**Technical Impact: when configured**

When configured, this parameter works by analyzing user roles and their associated authorizations to detect any SoD violations. It takes into account not only the explicit role assignments but also considers inherited roles and mitigated roles to provide a comprehensive view of the user's effective authorizations.

**Examples Scenario:**

If an employee is assigned roles that allow them both to create purchase orders and approve payments, this could lead to a potential conflict of interest or even fraudulent activities. Enabling `SoCheckUserSoDByEmployeeAuthorizations` would help in identifying such risky combinations and facilitating remediation actions before any damage is done.

**Related Settings:**

- AdditionalMitigatedSoxViolationsForRoles
- SodCombinationByRoleResultManager

**Best Practices:** configure when implementing or reviewing internal controls within the organization to ensure compliance with SoD policies. Avoid when roles and authorizations are not well defined or documented, as this could lead to false positives or an inability to accurately detect SoD violations.