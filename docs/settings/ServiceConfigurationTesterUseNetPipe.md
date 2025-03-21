# Service Configuration Tester Use Net Pipe

**Technical Name:** ServiceConfigurationTesterUseNetPipe

**Category:** Configuration

**Default Value:** Not provided in the provided code references.

**Impact Level:** Medium

**Description:**

This parameter controls whether the Pathlock Cloud GRC platform's Service Configuration Tester utilizes Net Pipe binding for communication between services. Net Pipe binding is used for on-machine communication between services in a Windows environment, offering a reliable and secure channel for service interactions.

**Business Impact:**

Enabling Net Pipe significantly impacts how the GRC platform's services communicate internally, potentially increasing security and performance for on-premises configurations. It influences the efficiency and reliability of the remote testing capabilities within the GRC environment, which can indirectly affect compliance reporting, risk management operations, and security policy enforcement.

**Technical Impact when configured:**

When the `ServiceConfigurationTesterUseNetPipe` is configured to true, the platform’s remote service testing component will leverage the Net Pipe protocol for communications, which can lead to improved latency and security for internal communications. This setting is particularly relevant for environments that prioritize secure and efficient on-machine communication for GRC processes.

**Examples Scenario:**

- **Enhanced Security and Performance:** A firm aiming to boost their internal service communication security and performance for their Pathlock GRC setup could enable this setting to ensure that their service configuration tests run more reliably and securely through Net Pipe binding.
- **Internal Compliance Testing:** An organization conducting frequent compliance checks could benefit from the Net Pipe binding's swift execution, ensuring that internal audits and compliance verifications are executed efficiently.

**Related Settings:** 

- MaxRecordsForChangesLogDisplay
- MessageQueueBaseAddress (Indirectly, as it pertains to alternative communication configurations)

**Best Practices:** 

- **Configure when:** You have a requirement for enhanced security and reliability for internal service communication within the Pathlock GRC platform, particularly in environments where the infrastructure supports or benefits from Net Pipe binding.
- **Avoid when:** Your infrastructure does not support Net Pipe binding or if the majority of your service communication happens over distributed networks where Internet Information Services (IIS) binding would be more appropriate.