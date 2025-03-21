# Cloud Client Encrypt Parameters

**Technical Name:** CloudClientEncryptParameters

**Category:** Security

**Default Value:** Not specified

**Impact Level:** High

**Description:**

The `CloudClientEncryptParameters` setting enables encryption for parameters transmitted between the client and the cloud within the Pathlock Cloud GRC platform. When enabled, this feature encrypts sensitive data in transit, enhancing the security of data exchanges by mitigating the risk of interception or unauthorized access.

**Business Impact:**

Enabling this parameter is crucial for organizations aiming to protect sensitive and proprietary information from potential cyber threats. It ensures confidentiality and integrity of the data exchanged between the client and cloud services, aligning with compliance requirements regarding data protection and privacy.

**Technical Impact when configured:**

When configured, all parameter transmissions involved in the communication between the client interfaces and the cloud services are encrypted. This encryption applies to any data sent over the network, preventing unauthorized entities from deciphering the contents of the communication.

**Examples Scenario:**

Consider a scenario where an organization transmits sensitive compliance data, such as audit logs or user access details, between its on-premise client and the Pathlock cloud platform. With `CloudClientEncryptParameters` enabled, this data is encrypted, thus safeguarding against potential eavesdropping attacks or breaches.

**Related Settings:**

- `ForceHttpsForSiteRedirect` 

**Best Practices:** configure when handling sensitive or regulated data to ensure secure data transmission across network boundaries; avoid when encryption may significantly degrade system performance or when operating within a fully trusted and secure internal network.