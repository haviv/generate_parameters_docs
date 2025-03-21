# Transaction Code Max Length

**Technical Name:** TransactionCodeMaxLength

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:** 

The Transaction Code Max Length parameter specifies the maximum allowed length for transaction codes within the Pathlock Cloud GRC platform. It ensures that transaction codes conform to defined standards, facilitating better management and identification of transactions across the system.

**Business Impact:** 

Setting an appropriate maximum length for transaction codes can significantly impact the organization's capability to manage and track transactions efficiently. It aids in maintaining consistency, avoiding data truncation issues, and ensuring compatibility with external systems or reports that may have length limitations. 

**Technical Impact when configured:** 

When this parameter is configured, it imposes a limit on the length of all transaction codes created or imported into the Pathlock Cloud GRC platform. Transactions with codes exceeding the specified maximum length may be rejected or require modification, influencing data import processes and integration with other systems.

**Examples Scenario:** 

- **Scenario:** An organization wants to ensure that all transaction codes used in their system are no longer than 10 characters to comply with an external auditing tool's requirements. By setting the TransactionCodeMaxLength to 10, the organization can prevent the creation or import of transactions with codes longer than this limit, thus ensuring compatibility with their auditing tool.

**Related Settings:** 

- TransactionAttribute1ColumnHeader
- TransactionAttribute2ColumnHeader

**Best Practices:** 

- **Configure when:** There is a clear requirement for transaction code lengths due to external system integration, reporting standards, or organizational policies on data format consistency.
- **Avoid when:** The organization does not utilize transaction codes extensively, or there are no external constraints on the length of these codes, to prevent unnecessary restrictions.