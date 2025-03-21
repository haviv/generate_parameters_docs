# Report Scheduler Web Address

**Technical Name:** ReportSchedulerWebAddress

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Report Scheduler Web Address parameter specifies the URL address used by the Pathlock Cloud GRC platform for invoking web services related to report scheduling and execution. This involves accessing, generating, and managing reports through automated schedules or on-demand requests.

**Business Impact:**

Proper configuration of the Report Scheduler Web Address ensures that users can automatically schedule, generate, and retrieve reports critical for compliance, audit, and risk management purposes. Incorrect configuration might result in the inability to access or generate required reports, potentially affecting compliance status and decision-making processes.

**Technical Impact when configured:**

When the Report Scheduler Web Address is configured correctly, the system can successfully communicate with the web service responsible for report generation and scheduling. This includes tasks such as executing complex reports on-demand or according to predefined schedules, thus supporting timely and efficient access to critical data for analysis and decision-making.

**Examples Scenario:**

- A compliance officer needs to schedule a monthly report that audits user access rights across all systems managed by the Pathlock Cloud GRC platform. Configuring the Report Scheduler Web Address allows this report to be automatically generated and sent to relevant stakeholders on the first day of each month.

**Related Settings:**

- SystemIdsToIgnore

**Best Practices:** configure when setting up the initial system settings and whenever there are changes to the domain or web service responsible for report management; avoid when the system is undergoing maintenance or updates that might temporarily affect report generation services.