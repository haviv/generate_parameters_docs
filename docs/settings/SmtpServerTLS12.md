**Technical Name:** SmtpServerTLS12

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**  
This setting configures the SMTP (Simple Mail Transfer Protocol) server to use TLS version 1.2 for encrypted email transmission, enhancing the security of email communications within the Pathlock Cloud GRC platform.

**Business Impact:**  
Enabling TLS 1.2 for SMTP communications ensures that all email messages sent from the platform are encrypted during transit, reducing the risk of interception and unauthorized access to sensitive information contained within these messages. This is crucial for protecting confidential corporate data, compliance-related communication, and any sensitive information shared via email.

**Technical Impact when configured:**  
- Guarantees that emails sent from the platform use TLS 1.2, providing a secure channel for email communication.
- Helps in complying with industry standards and regulations that mandate the use of secure communication protocols for transmitting sensitive information.
- May prevent email communications from being sent or received if the configured SMTP server does not support TLS 1.2.

**Examples Scenario:**  
A financial institution using the Pathlock Cloud GRC platform for risk management decides to enforce the highest security standards for all their email communications. By configuring the SmtpServerTLS12 parameter to enforce TLS 1.2, they ensure that audit reports, compliance notifications, and sensitive action items are securely transmitted to the intended recipients, safeguarding against potential cyber threats.

**Related Settings:**  
- CustomConnectionStringForTransactionHistory

**Best Practices:**  
- **Configure when:** You require the highest security for email communications, especially when handling sensitive information that must be protected according to compliance standards.
- **Avoid when:** The SMTP server in use does not support TLS 1.2, as this will prevent emails from being sent or received.
