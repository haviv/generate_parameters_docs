**Connectors Folder**

**Technical Name:** ConnectorsFolder

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** High

**Description:**

The `ConnectorsFolder` parameter is used to specify the directory path where connector configuration files or related resources are stored. This setting is crucial for the Pathlock Cloud GRC platform to correctly interface with external systems and applications, ensuring secure and efficient data exchange and processing.

**Business Impact:**

Proper configuration of the `ConnectorsFolder` ensures that the Pathlock platform can seamlessly connect to, interact with, and manage data from various external sources and services. This impacts the organization's ability to enforce GRC (Governance, Risk Management, and Compliance) policies across different applications and platforms, thereby maintaining security standards and compliance requirements.

**Technical Impact when configured:**

Once configured, the platform utilizes the specified folder to access necessary files for connector operations. This can include connector configuration files, scripts, or any other data essential for the integration with external systems. Incorrect or improper configuration may lead to integration issues, affecting data integrity and the performance of GRC tasks.

**Example Scenario:**

For instance, an organization uses the Pathlock platform to integrate SAP system data. The `ConnectorsFolder` is configured to point to a network directory that contains all SAP connector configuration files. This setup allows for streamlined data exchange between the Pathlock platform and the SAP system, enabling real-time compliance monitoring and risk management.

**Related Settings:**

- `SapUserName`
- `SapPassword`

**Best Practices:** 

- Configure the `ConnectorsFolder` upon initial setup of the Pathlock platform, ensuring that the path specified is correct and accessible by the system.
- Avoid changing the `ConnectorsFolder` path frequently to prevent disruptions in data exchange and integrations with external systems.