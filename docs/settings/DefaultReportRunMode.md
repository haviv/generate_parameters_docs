# Default time zone for reports:

**Technical Name:** DefaultReportRunMode

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The DefaultReportRunMode parameter configures the default time zone setting used for generating reports within the Pathlock Cloud GRC platform. This setting is crucial for ensuring that report timings align with the user or organizational time zone preferences.

**Business Impact:**

Setting an appropriate default time zone impacts how report data is interpreted across global operations, ensuring that all compliance, audit, and risk management activities are accurately timed and recorded. It helps in synchronizing activities and understanding reports in a time context relevant to the user or business operations.

**Technical Impact when configured:**

Correct configuration ensures that all reports generated reflect the correct time zone, aligning the reported events and activities with the actual time they occurred. Incorrect settings might lead to confusion or misinterpretation of the report data due to time discrepancies.

**Example Scenario:**

A multinational corporation uses the Pathlock Cloud GRC platform for compliance and auditing across its global branches. Setting the DefaultReportRunMode to the local time zone of each branch ensures that when reports are generated, they reflect the local time for activities, ensuring accurate tracking and compliance management.

**Related Settings:**

- `UserTimeZone`

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for the first time or entering a new global market. It is essential when you have operations across different time zones to maintain accuracy in report timings.
  
- **Avoid when:** There is no clear understanding of the regional or global implications of the time zone settings on the reporting data. It is crucial to understand the business operations across time zones before setting a default.