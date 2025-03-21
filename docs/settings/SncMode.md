# Snc Mode

**Technical Name:** SncMode

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**
The SncMode parameter is used to configure the Secure Network Communication (SNC) within the Pathlock Cloud GRC platform, particularly in scenarios involving SAP system connections. It determines the security mode for communications between the Pathlock platform and SAP systems, ensuring data transmitted in these interactions is secured.

**Business Impact:**
Setting the SncMode correctly is crucial for maintaining the confidentiality and integrity of sensitive business data during transmission. Misconfiguration can result in data breaches, unauthorized system access, or data corruption, potentially leading to significant financial and reputational damages.

**Technical Impact when configured:**
When correctly configured, SncMode enables secure and encrypted communication channels between Pathlock and SAP systems, leveraging industry-standard encryption protocols to protect data in transit. This helps in complying with various regulatory requirements and internal security policies by minimizing the risk of data interception and unauthorized access.

**Examples Scenario:**
- **Scenario 1:** An organization needs to ensure that any data exchanged between its compliance software and SAP systems is encrypted to meet GDPR compliance requirements. Setting up SncMode to a secure setting would enable encrypted communication, safeguarding personal data against breaches.
- **Scenario 2:** A company operating in a highly regulated industry requires all system interactions to be conducted over secure channels to prevent corporate espionage. Configuring the SncMode to use high-security protocols ensures that all communications are encrypted, thereby protecting corporate secrets.

**Related Settings:** 
- RfcConfigParameters.AppServerHost
- RfcConfigParameters.SystemNumber

**Best Practices:** 
- **Configure when:** Setting up the Pathlock platform for initial use or when integrating new SAP systems into the GRC landscape to ensure secure communication from the start.
- **Avoid when:** There is insufficient infrastructure to support high-level encryption, or it's unnecessary for internal, isolated systems where security is not a concern due to other mitigating controls.