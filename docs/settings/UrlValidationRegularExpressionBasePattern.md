**Technical Name:** UrlValidationRegularExpressionBasePattern

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The `UrlValidationRegularExpressionBasePattern` parameter is used to define the base regular expression pattern for validating URLs within the Pathlock Cloud GRC platform. This setting ensures that only URLs that match the specified pattern are considered valid, adding a layer of security by preventing the use of potentially malicious or inappropriate URLs.

**Business Impact:**

Implementing a rigorous URL validation pattern helps in mitigating the risk of XSS (Cross-Site Scripting), SQL Injection, and other injection attacks that could exploit vulnerabilities in the application through malicious URLs. It ensures that only URLs adhering to the defined safe pattern are allowed, thereby protecting the organization’s data and the integrity of the GRC platform.

**Technical Impact when configured:**

- Enhances security by limiting the scope of acceptable URLs, denying any that could potentially lead to security vulnerabilities.
- Reduces the risk of injection attacks by enforcing a strict validation pattern that malicious URLs cannot bypass.
- Aids in compliance with security best practices and policies by enforcing the use of predefined URL formats.

**Examples Scenario:**

An organization configures the `UrlValidationRegularExpressionBasePattern` to only accept URLs that start with "https://" and include the organization's domain name. This prevents users from inadvertently or maliciously entering URLs that could lead to phishing sites, external malicious content, or utilize insecure connections.

**Related Settings:**

- FileManagerUploadForbiddenFileTypes

**Best Practices:** 

- **Configure when:** Setting up security measures for URL inputs within the Pathlock Cloud GRC platform. It’s especially critical when the organization wants to enforce strict guidelines on what constitutes a valid URL as part of their security policy.
  
- **Avoid when:** Precise configuration or understanding of URL patterns that meet the organization's security requirements is not established, as incorrect patterns could block legitimate URLs or open up vulnerabilities.