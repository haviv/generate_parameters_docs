# Schedule Mail Without Report

**Technical Name:** ScheduleMailWithoutReport

**Category:** Reporting

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This setting allows for the scheduling of email notifications without attaching the report. When enabled, users can schedule emails related to reports that will be sent to specified recipients without including the report as an attachment, potentially for confidentiality or data size considerations.

**Business Impact:**

Enabling this feature can significantly impact operational efficiency and data security. It ensures that sensitive information is not inadvertently shared beyond its intended audience while still keeping stakeholders informed about the reporting timelines or statuses.

**Technical Impact when configured:**

When configured, this parameter alters the behavior of the report scheduling functionality. It will send out scheduled emails to the intended recipients without attaching the report itself. This could be utilized in scenarios where the notification of a report's completion is required without distributing the report via email.

**Examples Scenario:**

- **Compliance Reporting:** In a scenario where compliance reports are generated and a record of their completion needs to be communicated to certain stakeholders without sharing the detailed contents, this parameter can be employed to send an email notification indicating the report's completion without the report attached.

**Related Settings:**

- `ScheduleReportFilePath`
- `ScheduleReportFileExtension`

**Best Practices:** Configure when you need to notify stakeholders about report generation without exposing the contents of the report. Avoid when reports need to be shared directly for immediate review.