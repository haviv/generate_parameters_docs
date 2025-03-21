# Sap Connector Read SM20 For Each Application Server

**Technical Name:** SapConnectorReadSM20ForEachApplicationServer

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

This configuration parameter enables the SAP Connector to read SM20 audit log files for each application server. It specifically focuses on the retrieval and processing of security-related events recorded in the SAP SM20 audit logs, enhancing the oversight and analysis capabilities regarding the actions taken within the SAP environment.

**Business Impact:**

Enabling this parameter ensures that organizations can continuously monitor and audit security-relevant activities across all application servers in their SAP landscape. It plays a critical role in identifying unauthorized access attempts, potential security breaches, and ensuring compliance with internal and external audit requirements.

**Technical Impact when configured:**

When activated, this parameter initiates comprehensive log reading processes, significantly increasing the visibility into user activities and system changes. It aids in the detection of suspicious behaviors, security policy violations, and potential data breaches by thoroughly analyzing the audit logs from each application server.

**Example Scenario:**

A company must comply with strict data protection regulations requiring detailed audit trails of access and changes to sensitive financial information within their SAP system. By configuring this parameter, the organization can ensure every action is logged and auditable, thus supporting compliance efforts and enhancing data security.

**Related Settings:**

N/A

**Applicable Workflows Actions:**

N/A

**Best Practices:** 

- Configure when: You require detailed audit trails for compliance or security monitoring across all SAP application servers.
- Avoid when: Your organization does not have the infrastructure or resources to manage the increased volume of log data, or if only specific application servers are critical to audit.