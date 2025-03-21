# Emergency Access Report Template

**Technical Name:** EmergencyAccessReportTemplateId

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:**

The Emergency Access Report Template parameter is utilized within the Pathlock Cloud GRC platform. This parameter specifies the template ID that should be used when generating reports related to emergency access events. Emergency access refers to the provision of unrestricted access rights to users, typically in critical situations requiring immediate action. The reports generated using this template provide insights into the usage of emergency access, helping organizations monitor and audit such activities for compliance and security purposes.

**Business Impact:**

Configuring the Emergency Access Report Template directly influences an organization's ability to effectively monitor, audit, and report on emergency access privileges. By utilizing a specific template, organizations can standardize the format and content of these reports, ensuring that they meet regulatory requirements and internal policies. This also plays a crucial role in identifying potential security risks associated with the misuse of emergency access rights, thus contributing to the overall security posture of the organization.

**Technical Impact when configured:**

When the Emergency Access Report Template is configured, the system will generate reports based on the specified template whenever an emergency access event occurs. This ensures that all relevant data, including the identity of the user granted emergency access, the duration of access, and the specific actions taken during the access period, are captured consistently and accurately. The availability of detailed and standardized reports aids in swift decision-making and facilitates compliance audits.

**Examples Scenario:**

- **Audit Preparation:** An organization is preparing for an external security audit. By configuring the Emergency Access Report Template, they ensure that all emergency access events are documented according to the auditor's requirements, demonstrating governance and control over privileged access management.
- **Compliance Review:** To comply with industry-specific regulations demanding strict oversight of emergency access to critical systems, a financial institution selects an appropriate template for its emergency access reports. This enables the institution to readily provide evidence of compliance with regulations like SOX or GDPR.

**Related Settings:**

- `Send Workflow Mails` in Advanced Configuration
- `EmailBodyContentFileName` for customizing email notifications associated with emergency access events
- `DisplayDeniedWorkflowStep` for additional insights into workflow steps within the reports

**Best Practices:** Configure when establishing or refining your organization's emergency access policies to ensure comprehensiveness and compliance. Avoid when the default reporting structures meet the regulatory and auditing requirements of your organization.