# Show Transaction Attributes On Reports

**Technical Name:** ShowTransactionAttributesOnReports

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the display of transaction attributes within various reports, adding a layer of detail that helps in analyzing transactions from different perspectives, such as security or compliance.

**Business Impact:**

Having transaction attributes visible on reports greatly enhances the understanding of transaction contexts, contributing to better decision-making regarding security, risk management, and compliance reporting.

**Technical Impact when configured:**

When enabled, this parameter leads to the inclusion of extra data columns in the reports generated, which detail the attributes associated with each transaction. This can impact report size, generation time, and readability.

**Examples Scenario:**

- **Security Reporting:** For reports aimed at auditing security events, enabling this parameter would provide auditors with detailed attributes of each transaction, aiding in the detection of anomalies or breaches.
- **Compliance Auditing:** When generating compliance reports, transaction attributes could prove crucial to demonstrate adherence to regulatory standards by providing a deeper insight into transactional data.

**Related Settings:**

`ActivityGroupRulesSheetImporter`, `ExcelMatrix/BaseUserActivityMatrixPage`, `ActivityGridColumnBuilder`

**Best Practices:** configure when detailed transactional analysis is required for security or compliance purposes; avoid when simple transactional summaries are sufficient or to reduce report complexity and size.