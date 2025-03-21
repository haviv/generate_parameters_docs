# Enable Advanced Db Trace

**Technical Name:** EnableAdvancedDbTrace

**Category:** Audit

**Default Value:** False

**Impact Level:** High

**Description:**

Enables detailed logging of database transactions. This parameter is critical for debugging complex issues related to database operations by providing an in-depth insight into the executed database commands and their outcomes.

**Business Impact:**

Activating this feature can significantly help in identifying the root causes of database-related issues, ensuring data integrity and security. However, it might result in performance overhead due to the extensive logging activities.

**Technical Impact when configured:**

When enabled, this parameter increases the verbosity of database logging, capturing detailed information about each database transaction, which includes execution time, transaction outcomes, and error messages if any. This detailed logging is instrumental in isolating and diagnosing database issues but may consume considerable disk space and processing resources.

**Examples Scenario:**

- **Issue Resolution:** When an application is experiencing intermittent database-related errors, enabling advanced DB trace can help capture detailed logs at the time of error occurrence, aiding developers or DBAs in pinpointing the issue.
  
- **Audit and Compliance:** In situations where an audit requires a detailed trail of database transactions for compliance verification, enabling this feature would ensure that adequate information is logged.

**Related Settings:** None

**Best Practices:** 

- **Configure when:** Investigating complex database issues, performing detailed audits, or when recommended by support for resolution of specific issues.
  
- **Avoid when:** Running in production environments under normal conditions due to the potential performance impact and disk space utilization. It is best used temporarily for troubleshooting purposes.