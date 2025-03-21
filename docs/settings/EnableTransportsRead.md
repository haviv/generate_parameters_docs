# Enable Transports Read

**Technical Name:** EnableTransportsRead

**Category:** Data Sampling

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

The `EnableTransportsRead` parameter allows for the reading of transport activities within the Pathlock Cloud GRC platform, specifically pertaining to SAP systems. Enabling this feature facilitates monitoring and auditing of all transport activities, a critical component for maintaining system integrity and compliance.

**Business Impact:**

Enabling transport read capabilities is essential for organizations that need to ensure the integrity and security of their SAP environment. By monitoring transport activities, businesses can detect unauthorized changes and comply with internal and external audit requirements. This is crucial for maintaining system stability and avoiding potential compliance issues.

**Technical Impact when configured**

When the `EnableTransportsRead` parameter is enabled, the system begins to log and monitor transport activities, identifying all user actions related to SAP transport requests. This includes tracking which user executed each action, the timestamp of the action, and other relevant details such as transaction code and IP address.

**Examples Scenario:**

For instance, an organization that operates under strict regulatory requirements needs to ensure that all changes to their SAP systems are authorized, recorded, and auditable. By enabling `EnableTransportsRead`, they can easily track all transport actions, such as when a transport request is created, released, or imported, providing a comprehensive audit trail for compliance purposes.

**Related Settings:**

- `EnableSM20LogRead`: Allows for reading of security audit logs, complementing the transport read capability by offering insights into security-related actions.

**Best Practices:** 

- Configure `EnableTransportsRead` in environments where stringent monitoring of SAP transport activities is required.
  
- Avoid enabling this feature in development environments where frequent transport activities occur and monitoring is not necessary, to reduce unnecessary data accumulation and performance overhead.