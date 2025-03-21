# Real Time Mail - Header Subject

**Technical Name:** HeaderSubjectFileName

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `HeaderSubjectFileName` parameter is designed to define the subject line for emails sent by the Pathlock Cloud GRC platform. This parameter allows administrators to customize how email notifications are perceived by the recipients, aligning the notification with organizational communication standards or specific alert types.

**Business Impact:**

A well-configured subject line can increase the visibility and urgency of compliance and governance-related notifications, ensuring that critical alerts are promptly addressed. It aids in the efficient management of security, risk, and compliance by ensuring the right messages reach the intended audience effectively and are distinguishable from routine communications.

**Technical Impact when configured:**

Upon configuration, the `HeaderSubjectFileName` directly influences the email subject line for notifications sent to users regarding various events or alerts. This can include breach notifications, compliance alerts, or any other significant event that requires user attention or response.

**Example Scenario:**

For instance, if a compliance issue is detected within a transaction, the system can use the `HeaderSubjectFileName` setting to generate an email with a subject line "Compliance Alert: Transaction Review Required". This immediately informs the recipient of the email content and its priority.

**Related Settings:**

- `FromMail` relates to sending email address configuration.
- `GlobalAdministrator` may be relevant for configurations accessible to system administrators.

**Best Practices:** 

- **Configure when:** you need to ensure that automated email alerts are immediately recognizable and actionable by the recipients. Tailor the subject line to clearly communicate the severity and type of alert or notification being sent.
- **Avoid when:** there is no clear policy or need for customization of email notification subject lines within your organization's GRC communication plan. Default settings might suffice in such cases.