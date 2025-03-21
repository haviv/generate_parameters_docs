# External Database Employees Select Query For Secondary Provider

**Technical Name:** ExternalDatabaseEmployeesSelectQuery_ForSecondaryProvider

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the SQL query used to select employee data from an external database for a secondary provider in the Pathlock Cloud GRC platform. It allows for the customization of data retrieval queries when integrating with external organizational structure databases, ensuring that specific data requirements or formats can be accommodated.

**Business Impact:**

Configuring this parameter ensures that the Pathlock platform can accurately and efficiently pull relevant employee data from external sources. This is critical for maintaining up-to-date records on the platform, which directly impacts security, compliance, and risk management workflows by ensuring that employee data reflects the current organizational structure and roles.

**Technical Impact when configured:**

When this parameter is properly configured, it allows the Pathlock system to query an external database for employee information using a secondary provider's requirements. This enables the system to adapt to various external database schemas or data arrangements, thus enhancing compatibility and flexibility in data integration efforts.

**Examples Scenario:**

Consider a scenario where your organization uses a primary HR system for most employee data but also maintains a secondary, specialized HR system for contractors. The primary system's data structure might not align with the secondary system. By configuring this parameter, you can specify a custom query that selects contractor information according to the secondary system’s unique schema, ensuring that contractor data is also integrated and managed within the Pathlock platform.

**Related Settings:**

- ExternalDatabaseManagerSelectQuery_ForSecondaryProvider

**Best Practices:** configure when there is a need to integrate employee data from a secondary external system with a different data schema. Avoid configuration without proper validation of the SQL query to prevent data integrity or performance issues.