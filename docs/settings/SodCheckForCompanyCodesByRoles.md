# SoD Check For Company Codes By Roles

**Technical Name:** SodCheckForCompanyCodesByRoles

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter evaluates user group combinations against predefined expressions to identify high-risk authorizations within specific company codes and roles. It is integral to enforcing Segregation of Duties (SoD) controls by pinpointing potential security risks in user access rights across different company codes within the organization.

**Business Impact:**

Implementing this check can significantly reduce the risk of fraud and errors by ensuring that no individual has conflicting roles that could lead to a lack of checks and balances within company operations. It supports compliance with internal and external audit requirements by maintaining stringent SoD policies.

**Technical Impact when configured:**

When configured, this parameter actively scans for and identifies instances where users may have been granted authorizations that, when combined, pose a high risk according to the organization's SoD policy. It leverages expressions to scrutinize user group combinations across different systems and authorization sets.

**Examples Scenario:**

For example, in a financial system, a user should not have the ability to both create vendors and approve payments. If such a combination is detected by the SoD Check For Company Codes By Roles, it would flag this as a violation, prompting necessary review and action to remediate the risk.

**Related Settings:**

- MaxItemsInColumnFilter
- SharedItemsEmailTemplateId

**Best Practices:** 

- **configure when:** setting up roles and permissions in environments with multiple company codes, particularly in complex ERP systems like SAP to ensure fine-grained access control and compliance with SoD policies.
  
- **avoid when:** the complexity of managing individual exceptions outweighs the potential risk of SoD violations. In such cases, alternative controls should be considered.
