# Show Sap Company Column

**Technical Name:** ShowSapCompanyColumn

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ShowSapCompanyColumn` parameter controls the visibility of the SAP Company column within the Pathlock Cloud GRC platform's reporting views. When enabled, this feature allows users to include the SAP Company Name alongside other user-related information in their reports, providing a clearer, more comprehensive view of user data within the context of their specific SAP environment.

**Business Impact:**

Enabling the SAP Company Column in reports enhances data granularity and insight for compliance and audit purposes, facilitating better decision-making and more precise risk assessments within the SAP landscape. Organizations can monitor and manage access controls more effectively by correlating user activities with specific SAP companies.

**Technical Impact when configured:**

When activated, this setting dynamically includes the SAP Company column in relevant reports. This inclusion aids in the segregation and analysis of data by company within the SAP environment, thus improving report relevance and utility for compliance, risk management, and audit activities within the organization.

**Examples Scenario:**

A multinational corporation uses SAP to manage its operations across several subsidiaries. By enabling the `ShowSapCompanyColumn`, security analysts can generate reports that detail user activities broken down by company, making it simpler to spot anomalies, assess access compliance, and support audit requirements on a company-by-company basis.

**Related Settings:**

- ShowLastLogOn
- ShowCreatedOnColumn

**Best Practices:** configure when the organization operates in a multi-company SAP environment to enhance reporting detail and support compliance efforts; avoid when unnecessary to reduce report complexity and improve processing time.