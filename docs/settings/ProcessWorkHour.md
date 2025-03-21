# Process Work Hour

**Technical Name:** ProcessWorkHour

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

Configures specific hours during which automated processes and reports are allowed to run in the Pathlock Cloud GRC platform. This setting helps in managing system load and ensuring that heavy processes do not impact system performance during peak business hours.

**Business Impact:**

Proper configuration ensures that system resources are optimally used, preventing potential slowdowns during critical business operations. By scheduling resource-intensive tasks outside of peak hours, organizations can maintain system responsiveness for end-users, thereby supporting continuous business operations without interruption.

**Technical Impact when configured:**

When configured, this parameter specifies the hour or range of hours when automated tasks, such as report generation and data processing, are permitted to execute. It effectively schedules these tasks to run during off-peak hours, reducing the load on system resources during business-critical times.

**Examples Scenario:**

A company may configure the `ProcessWorkHour` to only allow report generation and other heavy data processing tasks to run between 2 AM and 4 AM. This ensures that these processes do not interfere with the system's performance during the day when users are actively using the system for their critical tasks.

**Related Settings:**

- RunReportOnStart

**Best Practices:** 

- **Configure when:** You have identified non-peak hours during which the system utilization is low and can handle additional load without impacting user experience.
  
- **Avoid when:** System resources are limited and cannot handle additional load even during off-peak hours, or if business operations require 24/7 real-time data processing and reporting, making it impractical to limit processing to specific hours.