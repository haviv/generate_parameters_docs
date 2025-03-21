# Sap Query Query Code Length

**Technical Name:** SAPQueryQueryCodeLength

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SAPQueryQueryCodeLength` parameter controls the maximum length of code that can be used in SAP Queries for custom reporting and data extraction. It is designed to ensure optimal performance and security of SAP reports by limiting the size of the query code.

**Business Impact:**

Setting the correct value for `SAPQueryQueryCodeLength` is critical in maintaining the balance between system performance and the ability of users to run complex queries for business analysis, compliance, and audit purposes. Too low of a value might restrict users from executing necessary detailed reports, while too high of a value could potentially hamper system performance or expose the system to risks of malicious queries.

**Technical Impact when configured:**

When configured, this parameter determines the maximum allowable characters in the SAP Query codes. It directly impacts the complexity and granularity of the reports that can be generated using the SAP connector within the Pathlock Cloud GRC platform.

**Examples Scenario:**

A compliance officer needs to generate a detailed report on user activities and system changes within the SAP environment over the past year. To achieve this, they write a custom SAP Query that pulls data from various tables within SAP. The `SAPQueryQueryCodeLength` parameter ensures that their query does not exceed the maximum length set by their organization's IT policy, balancing the need for detailed information with system performance and security.

**Related Settings:**

- `SAPQueryPreFix`

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform to ensure that SAP Queries are optimized for performance and security.
- **Avoid when:** There is not enough understanding of the business reporting requirements or the impact on system performance has not been assessed.