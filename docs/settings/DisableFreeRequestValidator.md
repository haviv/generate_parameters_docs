# Disable Free Request Validator

**Technical Name:** DisableFreeRequestValidator

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Disable Free Request Validator parameter is utilized to enhance system security and integrity by limiting unvalidated or free form requests within the Pathlock Cloud GRC platform. This setting serves as a safeguard, ensuring that only predefined and validated requests are processed, thereby minimizing potential security risks associated with arbitrary data input.

**Business Impact:**

Enabling the Disable Free Request Validator parameter can significantly reduce the risk of security vulnerabilities resulting from unchecked request data. It ensures that only authorized and validated requests are executed, which is critical in maintaining the integrity of the GRC (Governance, Risk Management, and Compliance) process. This setting is particularly beneficial in environments requiring stringent data validation to comply with internal and external audit and regulatory requirements.

**Technical Impact when configured:**

When this parameter is configured to enable the request validator, the system will reject any request not matching the predefined validation criteria. This action helps in preventing SQL injection, cross-site scripting (XSS), and other common web application security flaws. It also ensures that the application adheres to best practices for input validation, thereby supporting a stronger security posture.

**Examples Scenario:**

- **Scenario:** An organization requires to ensure that all data input through the GRC platform's web interface is validated to prevent malicious data breaches.
  - **Configuration:** The Disable Free Request Validator parameter can be enabled to ensure that only validated requests are processed. This configuration prevents attackers from exploiting any vulnerabilities by injecting malicious code or data that could compromise the security of the GRC system.

**Related Settings:**

- CustomCUASystemNumber
- CustomDomain

**Best Practices:** configure when 
- The environment requires high levels of data integrity and security.
- Compliance with specific regulatory standards mandates strict data validation.

avoid when 
- The platform is in a developmental or testing phase where free-form requests are necessary for testing purposes.