# Enable SNC

**Technical Name:** EnableSNC

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

Enables Secure Network Communications (SNC) to enhance security for data exchange between systems. When enabled, it ensures encrypted and authenticated communication within the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling SNC helps protect sensitive data from eavesdropping and tampering threats, thus ensuring compliance with data protection regulations and policies. It significantly reduces the risk of data breaches and unauthorized access, preserving the integrity and confidentiality of the exchanged data.

**Technical Impact: when configured**

Provides an encryption layer for all communications, ensuring that data is transmitted securely over the network. This setting requires specifying a partner name (SncPartnerName) and mode (SncMode) for configuring the secure session parameters.

**Examples Scenario:**

An organization needs to ensure that all communication with the Pathlock Cloud GRC platform is encrypted to meet strict industry compliance standards. By enabling SNC and configuring the respective partner name and mode, they can securely exchange data with the assurance that it is protected against unauthorized access and breaches.

**Related Settings:**

- `SncPartnerName`
- `SncMode`

**Best Practices:** 

- **configure when:** Implementing in environments where data security and privacy are paramount, especially in sectors like finance, healthcare, and public services.
- **avoid when:** Running non-sensitive environments where setup and operational complexities can be minimized. However, always consider regulatory compliance and organizational policies.