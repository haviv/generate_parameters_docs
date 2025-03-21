# Custom Connection String For Transaction History

**Technical Name:** CustomConnectionStringForTransactionHistory

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The CustomConnectionStringForTransactionHistory parameter allows Pathlock users to specify a custom database connection string for accessing transaction history. This can be used to point the system to a specific database instance or schema tailored for storing and managing transaction logs, different from the default database settings.

**Business Impact:**

Configuring this parameter can significantly impact how transaction data is accessed and reported within the Pathlock platform. Proper configuration ensures that transaction history is efficiently retrieved, supporting compliance, audit, and monitoring workflows. Misconfiguration could lead to an inability to access historical transaction data, affecting audits, compliance reporting, and security monitoring.

**Technical Impact when configured:**

When properly configured, this parameter ensures that the Pathlock system utilizes a custom database effortlessly for transaction history queries. This can lead to improved performance and scalability by leveraging optimized database instances or schemas. It can also enhance data security by isolating transaction data in a dedicated database according to best practices.

**Examples Scenario:**

An organization wants to segregate transaction history data from other operational data within their IT environment for performance and security reasons. By configuring the CustomConnectionStringForTransactionHistory parameter, they direct the Pathlock platform to query a specially optimized database when accessing transaction history, thereby achieving their performance and security objectives.

**Related Settings:**

- OverrideLdapFilterForDirectManagers

**Best Practices:** 

- **Configure when**: You have a dedicated database for transaction logs that is optimized for read operations or when you need to comply with data governance policies requiring segregation of transaction data.
- **Avoid when**: The default database configuration meets your organization's performance, security, and compliance requirements, or if there is a lack of expertise in managing database connection strings, as misconfiguration could lead to data access issues.