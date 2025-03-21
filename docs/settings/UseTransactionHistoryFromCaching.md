# Use Transaction History From Caching

**Technical Name:** UseTransactionHistoryFromCaching

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether the system retrieves transaction histories from its caching system rather than fetching fresh data every time. Utilizing cached data can significantly improve performance for authorization certifications and reporting by minimizing database queries.

**Business Impact:**

Leveraging caching for transaction histories can lead to faster report generation and a more responsive user experience during authorization certification processes. It is particularly beneficial for organizations with large datasets or those that perform frequent audits and certifications.

**Technical Impact when configured:**

When enabled, the system will preferentially pull transaction history data from cached sources, reducing the load on the database and potentially decreasing the time needed to perform authorization certifications and generate reports. However, there may be a slight risk of retrieving stale data if the cache is not updated frequently.

**Example Scenario:**

Suppose an organization conducts daily authorization certifications for hundreds of users across multiple systems. Enabling this parameter could reduce the time taken to generate certification reports from several minutes to just a few seconds, significantly improving the efficiency of compliance operations.

**Related Settings:**

- ReportSchedulerWebAddress
- SystemIdsToIgnore

**Best Practices:** 

- **Configure when:** Rapid reporting and authorization certification response times are needed, especially in environments with large volumes of transactions.
  
- **Avoid when:** The utmost data accuracy is required in real-time, and the system can accommodate the performance overhead of fetching fresh data for each transaction history query.