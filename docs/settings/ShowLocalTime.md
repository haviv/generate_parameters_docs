# Show local date and time for each event

**Technical Name:** ShowLocalTime

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

Displays the local date and time for each event within the Pathlock Cloud GRC platform, ensuring that audit trails and event logs reflect the accurate timestamp as per the user's timezone. This feature is crucial for tracking and understanding the specific timing of security, risk, and compliance-related activities within the system.

**Business Impact:**

Enabling ShowLocalTime enhances compliance and auditing processes by providing precise time references for each event, facilitating easier analysis and reporting. It also assists in troubleshooting and monitoring activities by offering a clear timeline of events according to the local time zone of the viewer, which is essential for global organizations operating across multiple time zones.

**Technical Impact when configured:**

Once configured, all event timestamps displayed to the user will automatically convert to the viewer’s local time zone. This adjustment allows for consistent time reporting and eliminates confusion related to time zone differences, enhancing the user's ability to make informed decisions based on the timing of events.

**Examples Scenario:**

- When reviewing access logs for compliance purposes, it’s imperative that the security team sees events in the local time zone to accurately assess and understand the sequence of actions.
- During an audit, auditors require precise timestamps tied to each event to align them with other records. The ShowLocalTime parameter ensures that these times are accurately reflected as per the auditor's local time zone.

**Related Settings:** 

- `ShowAllUserRequestsLinkOnRequestSubmittedPage`: While reviewing user requests, showing events in local time aids in evaluating request timelines.

**Best Practices:** 

- **Configure when:** You operate in a multi-time zone environment to ensure clarity in reporting and auditing. Accurate local timestamps are vital for compliance, security monitoring, and incident investigation processes.
- **Avoid when:** Only if all system users and operations are confined to a single time zone, where displaying event times in UTC or a single time zone does not lead to confusion or inaccuracies in time perception.