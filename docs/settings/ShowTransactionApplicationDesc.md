**Technical Name:** ShowTransactionApplicationDesc

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:**

Controls whether additional descriptive information about transactions is displayed in report columns. When enabled, it allows for more detailed reporting by including extra attributes associated with each transaction.

**Business Impact:**

Enabling this parameter can significantly enhance the transparency and comprehensibility of reports pertaining to transactions. This can aid in audit processes, compliance verification, and risk management by providing more context around each transaction.

**Technical Impact when configured:**

The system will include additional columns in reports that show descriptive attributes of transactions, potentially increasing report generation times but improving informational value.

**Examples Scenario:**

- An audit requires a detailed report of all transactions related to a sensitive account. Enabling ShowTransactionApplicationDesc would allow the report to include descriptive attributes, giving auditors a clearer picture of each transaction's nature and purpose.
  
**Related Settings:**

- ShowTransactionAttributesOnReports

**Best Practices:** 

- Configure when detailed transaction reporting is necessary for audits, regulatory compliance, or internal reviews to increase transparency.
- Avoid when simplicity is preferred in transaction reporting, or when additional information may clutter reports unnecessarily.