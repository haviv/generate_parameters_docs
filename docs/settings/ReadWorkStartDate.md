# Read Work Start Date

**Technical Name:** ReadWorkStartDate

**Category:** User Management

**Default Value:** None provided

**Impact Level:** Medium

**Description:**

This parameter is designed to configure the system to read the start date of work for employees from an external or internal HR system. It is tailored to integrate seamlessly within the Pathlock Cloud GRC platform, focusing specifically on enhancing user management processes.

**Business Impact:**

Effectively using the Read Work Start Date parameter ensures that the organization's security, compliance, and risk management processes are aligned with the actual employment dates of its workforce. By accurately defining the start dates, organizations can manage access permissions, audits, and compliance reports more effectively, minimizing the risk of unauthorized access or non-compliance with regulatory standards.

**Technical Impact when configured:**

When configured, this parameter actively filters and structures user data by their actual start date in the organization. It enables granular access control, ensuring that employees gain access to systems and data pertinent to their role from the correct start date. Additionally, it supports compliance by providing accurate data for audit trails and compliance reporting.

**Examples Scenario:**

Consider a scenario where an organization needs to audit access rights and permissions for new employees. By utilizing the Read Work Start Date parameter, the audit team can effectively filter employees who recently joined the organization and review their access rights, ensuring they are aligned with the job role and compliance requirements.

**Related Settings:**

- `ProfileTailorUser`
- `NotifyApproverWorkflowDeclinedTemplateId`

**Best Practices:** configure when you need to synchronize employee start dates across internal and external systems for accurate access management. Avoid when the organization does not use dynamic access control based on employment dates.