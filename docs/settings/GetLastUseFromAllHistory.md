# Get Last Use From All History

**Technical Name:** GetLastUseFromAllHistory

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter determines whether to search through all historical data when generating reports on the last use of critical transactions. Enabling this setting may impact report generation time due to the larger volume of data being analyzed.

**Business Impact:** Enabling this feature can provide a comprehensive view of the usage patterns of critical transactions over time, helping organizations to better understand their risk exposure and compliance status. However, it may also result in longer waiting times for reports to be generated due to the increased amount of data analyzed.

**Technical Impact when configured:** When this parameter is set to true, the system will include all historical data in the analysis for the last use date of critical transactions. This is particularly useful for audits and compliance reviews where a complete usage history is required. However, enabling this feature can significantly increase the load and processing time for report generation.

**Examples Scenario:** If an organization is preparing for an audit and needs to understand the last time a particularly sensitive or critical transaction was used, enabling GetLastUseFromAllHistory would allow the system to comb through all available historical data to find the most accurate last usage date.

**Related Settings:** 

- RoleReDesignMode

**Best Practices:** 

- Configure when: Preparing for an audit or when needing a comprehensive analysis of transaction usage over an extended period.
  
- Avoid when: Quick reporting is needed, or the impact on system performance and report generation time is a concern.