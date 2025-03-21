# Sap Connector Query Domain Values

**Technical Name:** SapConnectorQueryDomainValues

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter enables the SAP Connector to query and retrieve domain values, specifically focusing on transaction codes related to object tab names within the SAP environment. It effectively filters and consolidates descriptions for these values, ensuring that only unique entries are considered for further processing.

**Business Impact:**

By enabling precise filtering and retrieval of SAP domain values, this parameter impacts the efficiency and accuracy of data synchronization and reporting in the Pathlock platform. It ensures that governance, risk, and compliance (GRC) activities are based on accurate and relevant SAP configuration data, thus enhancing the integrity of GRC processes.

**Technical Impact when configured:**

Configuring this parameter optimizes the Pathlock platform's interaction with SAP systems by ensuring that only necessary and unique domain values are queried and processed. This reduces unnecessary load and potential errors in data processing, leading to more reliable GRC reporting and analysis.

**Examples Scenario:**

An organization wishes to streamline its GRC processes by ensuring that only relevant and unique transaction codes related to specific object tab names are considered for compliance checks and risk analysis. By configuring the `SapConnectorQueryDomainValues` parameter, the system can more efficiently identify and utilize the necessary SAP domain values, improving the accuracy and performance of the GRC platform.

**Related Settings:**

- `EnableSimulationOfRoleFromDev`: This setting, although not directly related, demonstrates an example of another configuration option within the Pathlock platform that enhances its flexibility and customization options.

**Best Practices:** Configure when setting up or modifying SAP Connector parameters to ensure efficient data synchronization and to streamline GRC processes. Avoid when unnecessary to reduce complexity and potential configuration errors.