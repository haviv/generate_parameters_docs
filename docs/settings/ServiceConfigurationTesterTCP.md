**Service Configuration Tester TCP**

**Technical Name:** ServiceConfigurationTesterTCP

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The Service Configuration Tester TCP parameter is used to determine if the TCP protocol should be used for service configuration testing purposes within the Pathlock GRC platform. When enabled, this setting allows the RemoteTestingClient to establish connections using TCP. In contrast, if it's set to false or left in its default state, alternative connection methods might be used based on the system's configuration and operational mode.

**Business Impact:**

Enabling TCP for service configuration testing can enhance the reliability and performance of remote testing activities by utilizing a more robust and widely supported protocol. This setting is particularly beneficial in complex network environments where alternative protocols may face limitations or restrictions. However, it requires careful network configuration and security considerations.

**Technical Impact when configured:**

- Enables the use of TCP for remote service testing, potentially improving connectivity and test performance.
- May require additional network configuration to allow TCP traffic for the specified service tests.
- Could introduce a need for enhanced security measures to protect the TCP communication channels.

**Examples Scenario:**

Imagine a scenario where an organization has a highly segmented network with strict firewall rules. The default communication protocol for service configuration testing fails because of these restrictions. By enabling the ServiceConfigurationTesterTCP parameter and configuring the network to allow TCP traffic for the testing process, the organization can successfully perform remote service configuration tests, ensuring their security and compliance checks are comprehensive and effective.

**Related Settings:**

- ServiceConfigurationTesterUseNetPipe
- CloudMode in DatabaseConnectionSettings

**Best Practices:** 

- Configure when: You require reliable and efficient communication for remote testing within restricted or complex network infrastructures.
- Avoid when: Your network security policy restricts the use of TCP for such purposes, or if the default communication protocol meets all your connectivity and performance needs without additional configuration.