# Database Provider Type DB2

**Technical Name:** DatabaseProviderType_DB2

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The DatabaseProviderType_DB2 parameter specifies the type of database provider for cases where DB2 databases are used within the Pathlock Cloud GRC platform. This setting is essential for establishing and managing the correct connection to DB2 database servers, which store and handle vital compliance and risk management information.

**Business Impact:**

Configuring the DatabaseProviderType_DB2 parameter correctly ensures that the Pathlock Cloud GRC platform can securely and efficiently interact with DB2 databases. This interaction is crucial for maintaining the integrity, availability, and confidentiality of sensitive compliance data and for supporting real-time risk management and audit processes.

**Technical Impact when configured:**

When the DatabaseProviderType_DB2 parameter is correctly configured, it enables seamless communication between the Pathlock Cloud GRC platform and DB2 databases. This configuration allows for the efficient execution of queries, updates, and data retrieval operations, which are pivotal for the operations of security, risk management, and compliance functionalities within the platform.

**Examples Scenario:**

- **SAP GRC Integration:** When an organization uses SAP for GRC (Governance, Risk, and Compliance) processes, and the underlying database is DB2, configuring this parameter ensures that Pathlock can access the SAP data stored in the DB2 database for compliance monitoring and risk assessment.

**Related Settings:**

- `DatabaseProviderType_Oracle` for organizations that use Oracle databases instead of DB2.

**Best Practices:** 

- **Configure when:** setting up the Pathlock Cloud GRC platform for the first time in an environment utilizing DB2 databases or when migrating the platform to use a DB2 database.
  
- **Avoid when:** the environment does not use DB2 databases, to prevent misconfiguration and potential connectivity issues.