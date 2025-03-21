# Database Provider Type Sql Server

**Technical Name:** DatabaseProviderType_SqlServer

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:** This parameter specifies the type of database provider to be used for SQL Server connections within the Pathlock Cloud GRC platform. It directly influences how the application connects to SQL Server databases, ensuring that the right protocols and standards are adhered to for security, data integrity, and connectivity.

**Business Impact:** Selecting the correct Database Provider Type is crucial for maintaining secure and reliable access to SQL Server databases. It impacts the efficiency and stability of data-driven operations within the GRC processes, affecting compliance reporting, risk management, and audit functionalities.

**Technical Impact when configured:** Proper configuration ensures optimal communication with SQL Server databases, enabling robust, secure, and efficient data transactions. Misconfiguration may lead to connectivity issues, data integrity problems, and potential security vulnerabilities.

**Examples Scenario:** If an organization uses SQL Server as its database for storing compliance data, configuring the DatabaseProviderType_SqlServer parameter correctly will ensure that the Pathlock Cloud GRC platform can reliably and securely access this data for compliance reporting, risk assessments, and audit trails.

**Related Settings:**
- ConnectionStringKeywords.InitialCatalog
- Utilities.ConnectorTypes.SapEccSM20 (for context comparison)

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when** setting up the Pathlock Cloud GRC platform to ensure that it can successfully connect to and interact with SQL Server databases.
- **Avoid when** the database in use is not SQL Server, as this setting is specifically tailored for SQL Server connectivity.