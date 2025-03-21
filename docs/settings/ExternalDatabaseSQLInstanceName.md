# External Database SQLInstance Name

**Technical Name:** ExternalDatabaseSQLInstanceName

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The External Database SQLInstance Name parameter specifies the name of the SQL Server instance for Pathlock's external database connections. This setting is crucial for integrating Pathlock GRC with external data sources, enabling the platform to fetch and synchronize data necessary for managing governance, risk, and compliance (GRC) within an organization.

**Business Impact:**

Configuring the External Database SQLInstance Name correctly is vital for ensuring that Pathlock GRC can access and retrieve data from an organization's external databases. This capacity supports various GRC processes, including risk assessment, compliance auditing, and security management. An incorrect or missing SQLInstance Name may lead to gaps in data synchronization, affecting the organization's ability to manage risk and compliance effectively.

**Technical Impact when configured:**

When properly configured, Pathlock GRC can accurately connect to and interact with the specified SQL Server instance. This ensures that the system can access the necessary data for reporting, analytics, and real-time monitoring of GRC-related activities. It enables seamless integration of external database information into the Pathlock platform.

**Examples Scenario:**

- An organization wishes to integrate employee data from its HRMS located on an external SQL Server into Pathlock GRC for compliance and audit purposes. The ExternalDatabaseSQLInstanceName must be set to the SQL Server instance where the HRMS database resides.
- A company uses an external SQL database to store access logs and security incident data. To include this data in its security monitoring and risk management workflows, the company must configure the ExternalDatabaseSQLInstanceName parameter to point to the SQL instance hosting this data.

**Related Settings:**

- GetActiveDirectoryUserAttributes

**Best Practices:** configure when the Pathlock GRC platform needs to fetch data from an external SQL Server database for GRC processes. Avoid when the data integration requirements can be met without accessing an external database, or when the SQL Server instance details are unknown or not secure.