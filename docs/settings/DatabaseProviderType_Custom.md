**Technical Name:** DatabaseProviderType_Custom

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `DatabaseProviderType_Custom` parameter allows the specification of a custom database provider type within the Pathlock Cloud GRC platform. This setting is critical for ensuring that the Pathlock platform can establish a connection to the organization's specific database system not covered by the predefined provider types (Oracle, SqlServer, etc.).

**Business Impact:**

Configuring the `DatabaseProviderType_Custom` correctly is essential for integrating Pathlock Cloud GRC with an organization’s existing database infrastructure. It directly impacts the system's ability to perform risk assessment, compliance monitoring, and security management tasks by accessing and analyzing the data stored in the database. Incorrect configuration could lead to incomplete or inaccurate GRC insights, affecting decision-making processes.

**Technical Impact when configured:**

Upon proper configuration, Pathlock Cloud GRC will be able to communicate with the specified custom database provider. This enables the platform to execute queries, fetch data, and perform operations required for compliance, risk management, and security monitoring activities. It ensures that the application's data layer is adaptable to various database technologies, enhancing flexibility and extending support to a broader range of database systems.

**Examples Scenario:**

An organization is using a bespoke database system for which a direct Pathlock Cloud GRC connector is not available. By setting the `DatabaseProviderType_Custom` parameter, the organization can specify their unique database type, enabling Pathlock Cloud GRC to interact with their database system. This custom configuration ensures that their specific risk, compliance, and security management needs are met, leveraging the full capabilities of the Pathlock platform.

**Related Settings:** 

- `DatabaseProviderType_Oracle`
- `DatabaseProviderType_SqlServer`
- `DatabaseProviderType_DB2`

**Best Practices:** 

- **Configure when:** You are integrating Pathlock Cloud GRC with a database system for which no predefined connector exists.  
- **Avoid when:** A predefined database provider type meets the organization's needs, as using standard configurations simplifies maintenance and support.