# Disable Custom Report Query Caching

**Technical Name:** DisableCustomReportQueyCaching

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Disabling custom report query caching prevents the caching of query results for custom reports. This setting is particularly useful for ensuring report data is always retrieved in real-time, directly from the database, thereby reflecting the most current information available at the time the report is run.

**Business Impact:**

Enabling this parameter might lead to more accurate and up-to-date reporting, which is critical for decision-making processes in areas such as compliance, risk assessment, and security management. However, it may also lead to increased database load and potentially slower report generation times, especially for complex queries or during peak usage periods.

**Technical Impact when configured:**

When this parameter is enabled, the system bypasses the caching mechanism for custom reports, leading to each report query being executed against the database in real-time. While this ensures the most current data is always used, it may also increase the load on the database server and slow down report generation times due to the lack of cached data reuse.

**Examples Scenario:**

1. **Compliance Reporting:** A compliance officer requires the latest data on user access rights for a critical end-of-quarter audit. By disabling query caching, they ensure the report reflects all changes up to the moment the report is run.
   
2. **Security Incident Investigation:** In the wake of a suspected security breach, IT security needs to analyze recent activity logs. Disabling caching for these custom reports ensures they are working with the most current data available, crucial for timely and accurate incident response.

**Related Settings:**

- ServiceConfigurationTesterUseNetPipe

**Best Practices:** 

- **Configure when:** Immediate data freshness is paramount for decision-making, and the impact on database performance is manageable or during low-traffic periods.
- **Avoid when:** Report performance is a critical concern, and data freshness can tolerate minor delays, or if database resources are limited.
