# Send Daily Mail As Attachment

**Technical Name:** SendDailyMailAsAttachment

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

Enables the delivery of daily reports via email with the report content attached. This setting is crucial for ensuring that stakeholders receive timely and direct reports on system activities, compliance status, or security incidents, directly in their mailbox, without the need to log in to the Pathlock Cloud GRC platform.

**Business Impact:**

Improves accessibility and immediacy of critical information distribution. Stakeholders and decision-makers can stay informed about the latest compliance and security statuses, directly through their email, facilitating quicker response times to potential risks or compliance issues.

**Technical Impact when configured:**

When enabled, the system compiles daily reports based on the specified criteria (e.g., security, compliance) and sends these as an email attachment to the configured recipient list. This process automates the distribution of reports, ensuring consistent delivery and reducing the manual effort required to keep stakeholders informed.

**Example Scenario:**

A compliance officer sets up the SendDailyMailAsAttachment parameter to ensure that daily compliance reports are automatically sent to the governance, risk management, and compliance (GRC) team. This ensures that the team is always up to date with the latest compliance status, can quickly identify any issues, and take corrective action if necessary.

**Related Settings:**

- CommonSettings.Default.DailyEmailSubject

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** Immediate distribution of daily reports via email is necessary for keeping internal stakeholders informed without requiring them to manually check the platform.
  
- **Avoid when:** Concerns about email security or the sensitive nature of attached reports necessitate more secure methods of report distribution.