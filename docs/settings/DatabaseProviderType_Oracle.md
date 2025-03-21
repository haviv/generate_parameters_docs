# Database Provider Type Oracle

**Technical Name:** DatabaseProviderType_Oracle

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** This parameter is used to specify that the Oracle database provider is being used within the Pathlock Cloud GRC platform.

**Business Impact:** Selecting the correct database provider ensures that the Pathlock platform can accurately connect to and interact with the organization's database, enabling efficient data management and security compliance reporting.

**Technical Impact when configured:** Ensures the Pathlock platform correctly interacts with Oracle databases, utilizing the appropriate drivers and settings for database operations, thus maintaining data integrity and operation efficiency.

**Example Scenario:** If your organization uses an Oracle database for storing security, risk, and compliance data, configuring the `DatabaseProviderType_Oracle` parameter ensures that Pathlock can retrieve, update, and manage this data effectively.

**Related Settings:** Not specified

**Best Practices:** Configure when your organization utilizes Oracle databases for its GRC data management. Avoid when your organization does not use Oracle databases, to prevent incorrect database interactions.