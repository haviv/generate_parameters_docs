# Main Entity Name For Employee

**Technical Name:** MainEntityNameForEmployee

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter configures the main entity identifier for employees within the Pathlock Cloud GRC platform. It specifies the primary source or attribute used to identify employees across various GRC processes.

**Business Impact:**

Proper configuration of this parameter ensures accurate identification and management of employee-related data, which is critical for executing compliance, security policies, and risk assessment accurately. Misconfiguration may lead to misidentification, affecting audit trails, access controls, and overall security posture.

**Technical Impact when configured:**

- Enhances the accuracy of employee identification across GRC workflows.
- Ensures reliable execution of security and compliance policies by accurately associating actions and permissions with the correct employee entities.
- Aids in the proper grouping and management of employee records for reporting and audit purposes.

**Example Scenario:**

In a scenario where an organization needs to tighten its security controls by ensuring only the correct individuals have access to sensitive financial data, the `MainEntityNameForEmployee` parameter could be configured to use employees' unique ID numbers as the primary identifier. This setup guarantees that system access, permissions, and activity logs accurately reflect the actions and access rights of specific employees, facilitating precise control and auditing.

**Related Settings:**

- EmployeeGroupRules
- MailListnerDeclineKeywords
- MailTemplateFormatting

**Best Practices:** 

- **Configure when** setting up the system for the first time or when modifying key employee identification attributes.
- **Avoid when** the information linking employees to their identifiers is not updated or accurate, as this will lead to mismanagement and potential security risks.