# Show Transaction Attribute3

**Technical Name:** ShowTransactionAttribute3

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The ShowTransactionAttribute3 parameter controls the visibility of a specific attribute related to transactions in generated reports. When enabled, reports will include an additional column or data field that provides detailed information pertinent to the third attribute of a transaction. This might involve showing criticality, time-related data, or any custom-defined attribute that has been deemed essential for review within the scope of governance, risk, and compliance (GRC) processes.

**Business Impact:**

Enabling this attribute can significantly improve audit readiness by providing auditors and compliance officers with more granular data on transactions. It allows for a deeper analysis of transaction-related risks and aids in the detection of potentially fraudulent activities or non-compliance with internal or external regulations. Businesses can use this additional data to refine their internal controls, enhance security measures, and ensure compliance standards are met.

**Technical Impact when configured:**

Upon activation, the system will dynamically add a data column in relevant reports, which details the third transaction attribute. This could impact system performance based on the volume of data processed and might require additional configuration to ensure the accurate representation of this attribute in reports.

**Examples Scenario:**

A financial institution uses ShowTransactionAttribute3 to include a criticality rating of transactions in their monthly compliance reports. This enables them to quickly identify high-risk transactions that require immediate attention and streamline their audit processes by focusing on areas of highest concern.

**Related Settings:**

- ShowHighRiskColumnTransaction

**Applicable Workflows Actions:**

**Best Practices:** 

- **Configure when:** There's a need to enhance the understanding and visibility of transaction attributes that are critical for compliance, auditing, and risk management.
  
- **Avoid when:** The inclusion of extra data might overwhelm the report readers or when the system's performance is a concern due to the large volume of transactions.