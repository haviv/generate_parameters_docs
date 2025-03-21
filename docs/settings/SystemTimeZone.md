**Technical Name:** SystemTimeZone

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** 

The SystemTimeZone parameter is used to configure the timezone for the system. This setting ensures that all date and time-related operations within the Pathlock GRC platform are consistent with the specified timezone.

**Business Impact:**

Proper configuration of the SystemTimeZone is crucial for maintaining the accuracy of time-sensitive operations and reports within the Pathlock GRC environment. Incorrect settings can lead to discrepancies in reporting, workflow triggers, and data extraction processes, potentially affecting compliance status and decision-making processes.

**Technical Impact when configured:**

When correctly configured, the SystemTimeZone parameter ensures that:
- All date and time calculations are performed relative to the specified timezone.
- Time-sensitive actions and reports are executed accurately, reflecting the correct times for the configured region.
- Data extractions and integrations that depend on timestamp information operate correctly, preventing data consistency issues.

**Examples Scenario:**

A company operating in the Central European Time (CET) zone configures the SystemTimeZone to CET to ensure that audit reports reflect the correct time for access logs and user activity within their Pathlock GRC platform. This setting is crucial for meeting compliance requirements that mandate accurate timestamping of security and access logs.

**Related Settings:** 

- `GetDateInCurrentTimezone`: Utilizes the SystemTimeZone parameter to convert times to the correct timezone.
- `ExternalTableExtractionsService`, `ActiveDirectoryConnector`: Services and connectors that would benefit from having a coherent timezone setting to accurately process external data and Active Directory synchronization.

**Best Practices:** 

- **Configure when**: Setting up the Pathlock GRC platform for the first time or modifying the system's operational timezone to accommodate changes in business operations or daylight saving time adjustments.
- **Avoid when**: There is uncertainty about the correct timezone in which the platform is operating, as this could lead to data and reporting inaccuracies. Confirm the appropriate timezone before making changes.