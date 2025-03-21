**Technical Name:** TimeZone

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The TimeZone parameter allows users to configure the time zone setting for reporting and data visualization within the Pathlock Cloud GRC platform. This setting ensures that timestamps and time-related data are displayed according to the user's or organization's local time zone, providing accurate and contextually relevant information for security, risk, and compliance activities.

**Business Impact:**

Configuring the TimeZone correctly is crucial for ensuring that reports, audits, and risk assessments reflect the accurate timing of events and activities. This accuracy is vital for compliance with regulatory requirements, understanding security events, and making informed decisions based on the timeline of activities.

**Technical Impact when configured:**

When the TimeZone parameter is configured, all reports and data analytics within the Pathlock platform will reflect the selected time zone. This adjustment ensures that the timing of displayed events aligns with the local time, facilitating clearer understanding and interpretation of data, especially in global organizations with users across different time zones.

**Examples Scenario:**

- A compliance officer based in London needs to generate an audit report for activities that occurred over the last quarter. By setting the TimeZone to GMT, the report will accurately reflect the timing of logged events according to the local time in London, aiding in a precise compliance review.
- A security analyst in New York is investigating a potential breach that occurred overnight. Setting the TimeZone to Eastern Standard Time (EST) ensures that the timing of log entries and security alerts in reports will match the local observation, helping to pinpoint when the incident started more accurately.

**Related Settings:**

UserTimeZone

**Best Practices:** 

- Configure the TimeZone parameter upon setup for users or system-wide settings to ensure that from the onset, all time-related data is correctly aligned with your local time zone.
- Avoid changing the TimeZone setting frequently to maintain consistency in reports and data interpretation across the organization.