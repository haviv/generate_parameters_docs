# External Database SQLInstance Name For Secondary Provider

**Technical Name:** ExternalDatabaseSQLInstanceName_ForSecondaryProvider

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the SQL instance name for accessing an external database when using a secondary provider in the Pathlock Cloud GRC platform. It is critical for integrating external organizational structure data into Pathlock's environment from a secondary SQL database provider.

**Business Impact:**

Configuring this parameter correctly ensures seamless integration of external data sources, leading to improved data accuracy and integrity for compliance, risk management, and security monitoring processes. Incorrect configurations can lead to data integration issues, affecting the overall GRC (Governance, Risk Management, and Compliance) process efficacy.

**Technical Impact when configured:**

Upon correct configuration, the Pathlock platform can accurately query and retrieve employee data from an external SQL database, thus enabling more precise control over data accuracy and the organization's structure within the GRC processes.

**Examples Scenario:**

An organization utilizes a secondary SQL database to manage employee information. By setting the ExternalDatabaseSQLInstanceName_ForSecondaryProvider parameter, Pathlock can directly query this database to import and synchronize employee details, ensuring the GRC processes are aligned with the actual organizational structure.

**Related Settings:**

- RestOrganizationStructureProvider_RunInCloud_ForSecondaryProvider

**Best Practices:** configure when

- Integrating with secondary SQL databases for organizational data synchronization.

avoid when

- The primary provider meets all organizational structure data requirements.