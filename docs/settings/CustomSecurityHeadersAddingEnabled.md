# Custom Security Headers Adding Enabled

**Technical Name:** CustomSecurityHeadersAddingEnabled

**Category:** Security

**Default Value:** Not Provided

**Impact Level:** High

**Description:**

The parameter `CustomSecurityHeadersAddingEnabled` controls whether custom security headers are added to HTTP responses by the Pathlock GRC platform. When enabled, it applies several security-related headers that enhance the overall security posture by specifying default source lists for different content types and restricting the URLs which can be loaded using script interfaces.

**Business Impact:**

Enabling custom security headers can significantly reduce the risk of content injection attacks such as Cross-Site Scripting (XSS) and data theft through man-in-the-middle (MITM) attacks. By specifying allowed sources for scripts, images, and connect sources, organizations can ensure that only trusted content is executed and loaded, thereby protecting the integrity and confidentiality of their data on the Pathlock GRC platform.

**Technical Impact when configured:**

- `default-src 'self' 'unsafe-inline'`: Serves as a fallback for other Content Security Policy (CSP) fetch directives, enhancing the default security level.
- `connect-src 'self'`: Restricts the URLs which can be loaded using script interfaces to the same origin, mitigating data exfiltration and minimizing MITM attack risks.
- `img-src 'self' 'unsafe-inline'`: Ensures that images and favicons are only loaded from the same origin or inline definitions, thereby preventing the loading of potentially malicious external resources.

**Examples Scenario:**

An organization wants to enhance its web application security on the Pathlock GRC platform. By enabling `CustomSecurityHeadersAddingEnabled`, they can:
1. Prevent unauthorized JavaScript from running, which might have been injected via XSS.
2. Ensure that images, scripts, and connect sources are only loaded from their own domain, avoiding the risk associated with external malicious resources.

**Related Settings:** 

- `UrlValidationRegularExpressionBasePattern`: This setting defines the base pattern used for validating URLs within the platform, which complements the security headers by ensuring only appropriately formatted URLs are considered valid.

**Best Practices:** 

- **Configure when:** You are looking to enhance the security of your Pathlock GRC platform by ensuring that web content sources are controlled and external script or image injections are prevented.
- **Avoid when:** If your organization utilizes a variety of external scripts and image sources not covered under 'self' or specific safe domains, extensive testing should be performed to ensure functionality isn't adversely affected. Adjustments to the policy might be required to accommodate legitimate external resources.