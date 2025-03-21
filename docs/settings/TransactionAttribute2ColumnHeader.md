# Transaction Attribute2 Column Header

**Technical Name:** TransactionAttribute2ColumnHeader

**Category:** Reporting

**Default Value:** *Not provided in the code references.*

**Impact Level:** Medium

**Description:** This parameter defines the header text for the second transaction attribute column in reports and grids within the Pathlock GRC platform. It is used to customize the presentation of transaction-related data to suit business reporting needs.

**Business Impact:** By configuring the Transaction Attribute2 Column Header, organizations can tailor how transactional data is presented, making reports more understandable and actionable for users. This customization can lead to improved audit trails, better oversight of financial transactions, and enhanced detection of potentially unauthorized or fraudulent activities.

**Technical Impact when configured:** Customizing the header impacts how data is presented in reports and activity grids. It enhances the readability and context of the presented data, which is crucial for effective analysis and decision-making.

**Examples Scenario:** If an organization wishes to closely monitor certain types of transactions for compliance reasons, renaming the Transaction Attribute2 Column Header to something more descriptive, like "Approval Status," can make it easier for auditors and reviewers to quickly understand the nature of the transactions without needing further explanation.

**Related Settings:** 
- `ReportsColumns.TransactionDesc`
- `ReportsColumns.Text_Description`

**Best Practices:** Configure when you need to align the reporting output with internal compliance requirements or external regulatory standards. Avoid when the default configuration meets the organization's reporting needs, to prevent unnecessary configuration complexity.