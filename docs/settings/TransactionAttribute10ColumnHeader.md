**Technical Name:** TransactionAttribute10ColumnHeader

**Category:** Reporting

**Default Value:** Not Applicable

**Impact Level:** Medium

**Description:**

This parameter defines the column header for the Attribute 10 in transaction reports. It is used to customize how the 10th attribute of a transaction is displayed in the user interface and reports. This customization aids in aligning the display names with the organization's terminology, ensuring clarity and relevance.

**Business Impact:**

Configuring the TransactionAttribute10ColumnHeader allows businesses to tailor the appearance and names of transaction attributes in reports to match their internal nomenclature. This customization can improve the clarity of reports for decision-makers, facilitating quicker and more informed decisions based on transactions data.

**Technical Impact when configured:**

When configured, this parameter changes the display name of the 10th attribute in transaction reports. It does not affect the underlying data or how it is processed but alters how the data is presented to the user in the Pathlock Cloud GRC platform.

**Examples Scenario:**

- In a financial institution, the 10th transaction attribute might be custom labeled as "Approval Status" to indicate whether a transaction has been approved, pending, or denied. Configuring the TransactionAttribute10ColumnHeader to "Approval Status" would make report columns more intuitive for reviewers.
  
**Related Settings:**

- TransactionAttribute8ColumnHeader
- TransactionAttribute7ColumnHeader

**Best Practices:** configure when you need to align report terminologies with your organization's internal nomenclature; avoid when default settings meet your organization's reporting requirements.