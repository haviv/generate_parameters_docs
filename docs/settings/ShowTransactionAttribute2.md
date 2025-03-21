# Show Transaction Attribute2

**Technical Name:** ShowTransactionAttribute2

**Category:** Reporting

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The `ShowTransactionAttribute2` parameter controls the visibility of a specified set of transaction attributes within reports or matrices. It allows for a dynamic display of transaction-related information based on configuration settings, enhancing the granularity and relevance of the reported data.

**Business Impact:**

Enabling this parameter ensures that stakeholders have access to critical transaction attributes that may influence decision-making processes. It aids in the auditability, traceability, and overall governance of transaction data, providing insights into high-risk transactions and user activities.

**Technical Impact when configured:**

When `ShowTransactionAttribute2` is configured, the system dynamically includes or excludes the second set of transaction attributes in the reporting output. This impacts data presentation and the level of detail available in reports, which can be crucial for pinpoint analyses of transactions in terms of security, compliance, or risk.

**Example Scenario:**

In an audit scenario, auditors require a report that explicitly shows transactions deemed high risk. By enabling `ShowTransactionAttribute2`, the system can generate reports that include detailed attributes of transactions flagged as high-risk, facilitating a targeted and efficient audit review.

**Related Settings:** 

- `ShowHighRiskColumnTransaction`: Determines if high-risk transactions should be distinctly marked or highlighted in reports, working in tandem with `ShowTransactionAttribute2` for more granular reporting.

**Best Practices:** 

- **Configure when:** Detailed transaction reporting is required for audit, compliance, or risk management purposes. It's particularly useful when there's a need to focus on specific attributes of transactions that are not covered by the standard transaction details.
  
- **Avoid when:** Simplicity is key in reporting, or when the inclusion of additional transaction attributes could complicate or clutter reports unnecessarily.