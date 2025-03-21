# External Database Manager Select Query For Secondary Provider

**Technical Name:** ExternalDatabaseManagerSelectQuery_ForSecondaryProvider

**Category:** Configuration

**Default Value:** ""

**Impact Level:** Medium

**Description:**

This parameter specifies the SELECT query to be used for fetching organizational structure data from an external database when configured as a secondary provider. It allows for custom queries to be defined for secondary database connections, enabling the retrieval of organizational structure data that aligns with specific business requirements.

**Business Impact:**

Configuring this parameter with an optimal select query ensures accurate and efficient data synchronization between the Pathlock Cloud GRC platform and the secondary provider's database. It plays a crucial role in maintaining the integrity and accuracy of organizational structure data, which can impact various aspects of security, risk management, and compliance reporting.

**Technical Impact when configured:**

- When configured, this parameter overrides the default query used for organizational data retrieval from the secondary database provider.
- Ensures that the specific data structure and attributes required by the organization are accurately mapped and imported into the Pathlock GRC platform.
- It can affect performance based on the complexity and efficiency of the SQL query defined.

**Examples Scenario:**

An organization has a primary and a secondary provider for their organizational structure data. The primary provider's data structure does not support a recent reorganization in department structures that the secondary provider does. The `ExternalDatabaseManagerSelectQuery_ForSecondaryProvider` parameter can be configured with a custom SQL query that accurately reflects the new organizational structure from the secondary provider, enabling correct data representation in the Pathlock platform.

**Related Settings:**

- ExternalDatabaseOrgStructureSelectQuery

**Best Practices:** 

- Configure this parameter when the default organizational structure retrieval query does not meet the specific data structure requirements of the secondary provider.
- Avoid complex queries that might significantly impact the performance of the synchronization process. Keep the query efficient and focused on the necessary data only.