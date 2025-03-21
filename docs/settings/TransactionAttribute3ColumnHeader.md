# Transaction Attribute3 Column Header

**Technical Name:** TransactionAttribute3ColumnHeader

**Category:** Reporting

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter specifies the column header for the third transaction attribute in reports related to user activities. It allows for customization of reporting views within the Pathlock Cloud GRC platform, ensuring that reporting outputs align with organizational terminology and preferences.

**Business Impact:**

The correct configuration of this parameter directly affects the clarity and relevance of reporting data, facilitating better decision-making regarding security, risk management, and compliance. It ensures that reports are tailored to the specific needs and terminologies of the organization, enhancing the readability and usability of reports for end-users.

**Technical Impact when configured:**

When appropriately configured, the third transaction attribute's column header will be customized in the report outputs. This customization does not affect the underlying data collection or report generation processes but improves the user interface by making report data more accessible and understandable to the end-users.

**Examples Scenario:**

- **Before Configuration:** The column header for the third transaction attribute is set to a default or a generic term, which might not accurately reflect its meaning to the organization.
  
- **After Configuration:** The column header is updated to "Payment Approval Status," accurately reflecting its content and making it clearer to report readers what the column data signifies regarding business operations.

**Related Settings:** 

While the code references do not explicitly mention related settings, similar parameters for other transaction attributes (e.g., `TransactionAttribute1ColumnHeader`, `TransactionAttribute2ColumnHeader`) likely exist and should be configured in concert to ensure consistency across report columns.

**Best Practices:** 
- **Configure when:** You need to align report outputs with organizational terminology or when introducing new types of transactions that require clear identification.
- **Avoid when:** The default or current column headers already accurately represent the data being reported, or when changes could confuse users familiar with existing reports.