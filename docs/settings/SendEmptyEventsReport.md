# Send events summary email report even without data:

**Technical Name:** SendEmptyEventsReport

**Category:** Reporting

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `SendEmptyEventsReport` parameter controls whether the Pathlock Cloud GRC platform sends scheduled email reports even when no events or data are available to report within the specified timeframe. This functionality ensures that stakeholders are informed about the status of events monitoring, even when no new incidents have been detected.

**Business Impact:**

Enabling this parameter can significantly enhance transparency and communication within an organization's governance, risk, and compliance (GRC) processes. By receiving scheduled reports regardless of data presence, stakeholders maintain awareness of monitoring activities and can be assured of the system's operational status, aiding in trust and compliance verification.

**Technical Impact when configured:**

When configured, the system triggers the delivery of email reports to designated recipients at scheduled times, even in scenarios where no new data or events have been recorded. This prevents gaps in reporting cycles and supports continuous engagement with the security, risk, and compliance posture of the organization.

**Example Scenario:**

- A compliance officer schedules weekly reports to track certain compliance activities. During a particular week, no violations or incidents are recorded. With `SendEmptyEventsReport` enabled, the officer still receives a scheduled report, confirming that no incidents have been overlooked and that the monitoring systems are functioning correctly.

**Related Settings:**

- `ScheduleReportBodyEmptyReport`: Determines the body content of reports when they are sent without data.

**Best Practices:** 

- **Configure when:** Regular communication to stakeholders regarding the monitoring status is required, especially in low-incident environments, to confirm operational integrity and compliance.
- **Avoid when:** Email notification volume is a concern, or recipients prefer to only receive communications when actionable data is present.