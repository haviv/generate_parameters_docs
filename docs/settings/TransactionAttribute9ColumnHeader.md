# Transaction Attribute9 Column Header

**Technical Name:** TransactionAttribute9ColumnHeader 

**Category:** Reporting

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `TransactionAttribute9ColumnHeader` parameter is used to define the column header for the ninth customizable transaction attribute within the Pathlock Cloud GRC platform's reporting interface. This allows organizations to customize their reporting views by naming transaction attributes in a way that aligns with their internal data classification and reporting standards.

**Business Impact:**

Customizing the column headers for transaction attributes enables organizations to tailor their security, risk, and compliance reports to better match internal terminologies, making the reports more intuitive and actionable for users. This can lead to improved efficiency in audits and compliance activities, as well as enhanced communication across the organization.

**Technical Impact when configured:**

- Alters the display name of the ninth transaction attribute in reports.
- Enables more meaningful reporting, aligning the interface with business-specific language and requirements.
- Facilitates easier identification and analysis of transactions based on customized attribute definitions.

**Examples Scenario:**

An organization uses a specific custom attribute in their transaction reports to track the department responsible for the transaction. By setting `TransactionAttribute9ColumnHeader` to "Responsible Department," the organization can easily configure reports to display this information clearly, enhancing the understanding and readability of the report for audit and compliance purposes.

**Related Settings:**

- `TransactionAttribute5ColumnHeader`
- `TransactionAttribute7ColumnHeader`

**Best Practices:** configure when you need to align the GRC platform’s reporting capabilities with your organization-specific requirements for transaction attribute nomenclature; avoid when standard reporting attributes suffice for your organization’s needs.