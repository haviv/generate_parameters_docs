# SMS Provider Use TLS12

**Technical Name:** SMSProviderUseTLS12

**Category:** Security

**Default Value:** False

**Impact Level:** High

**Description:**

The `SMSProviderUseTLS12` parameter configures the SMS service to utilize TLS 1.2 protocol for securing SMS notifications sent by the Pathlock Cloud GRC platform. This setting ensures that the communication between the Pathlock platform and the SMS provider is encrypted using TLS 1.2, enhancing the security of SMS transmissions.

**Business Impact:**

Enabling TLS 1.2 for SMS notifications ensures compliance with industry standards for data security and privacy. It protects against eavesdropping and man-in-the-middle attacks, securing sensitive information contained in SMS messages from unauthorized access. This is crucial for enterprises that use SMS messages for sending confidential data such as one-time passwords (OTPs), compliance notifications, or operational alerts.

**Technical Impact when configured:**

When the `SMSProviderUseTLS12` parameter is enabled, all outbound SMS messages from the Pathlock Cloud GRC platform are transmitted over a secure channel using TLS 1.2 protocol. This may require ensuring that the SMS service provider supports TLS 1.2 and that any intermediate network appliances or firewalls are configured to allow TLS 1.2 traffic.

**Example Scenario:**

An organization needs to comply with financial regulations requiring all communication channels to use secure transmission protocols. By enabling `SMSProviderUseTLS12`, the organization ensures that all SMS notifications sent for transactional approvals, security alerts, and user verification are transmitted securely, helping to meet the compliance requirements.

**Related Settings:**

Not applicable.

**Best Practices:** 

- **Configure when:** You need to ensure secure transmission of SMS notifications per industry compliance standards or internal security policies.
- **Avoid when:** The SMS provider or your current infrastructure does not support TLS 1.2, in which case, ensure necessary upgrades or validations are performed before enabling this setting.