# SoD Full Report Run Offline Notify In Mail

**Technical Name:** SodFullReportRunOfflineNotifiyInMail

**Category:** Reporting

**Default Value:** True

**Impact Level:** Medium

**Description:** This parameter enables the system to notify users via email when a Separation of Duties (SoD) full report is run in offline mode. When set to true, relevant stakeholders are informed automatically once the report generation is completed, facilitating more efficient, proactive management of compliance and risk.

**Business Impact:** Ensures timely dissemination of critical SoD report information to designated users, enhancing decision-making processes around security, risk management, and compliance adherence. This setting plays a vital role in maintaining internal control environments and supporting audit readiness by ensuring stakeholders are informed of SoD status without delay.

**Technical Impact when configured:** Upon configuration, this setting engages the email notification system within Pathlock to dispatch notifications to predefined users specified in `SodFullReportRunOfflineUsers`. It's only operative when `SodFullReportRunOfflineEnable` is set to true, indicating the system's readiness to generate SoD reports in offline mode.

**Examples Scenario:**

- **Compliance Reporting:** An organization requires regular SoD analysis to ensure that no employees hold conflicting roles. By enabling this notification, compliance officers are immediately informed when the SoD report is ready for review, irrespective of the report's generation time, allowing for timely action.
  
**Related Settings:** `SodFullReportRunOfflineEnable`, `SodFullReportRunOfflineUsers`

**Best Practices:** configure when the organization requires immediate knowledge of SoD report completion to keep up with compliance and audit schedules; avoid when unnecessary to reduce excessive notification load or if real-time report generation meets organizational needs.