# Force Https For Site Redirect

**Technical Name:** ForceHttpsForSiteRedirect

**Category:** Security

**Default Value:** Not provided in the code references.

**Impact Level:** High

**Description:** This setting enforces HTTPS protocol for all site redirects, enhancing the security by ensuring that all data transmitted between the client and the server is encrypted.

**Business Impact:** Implementing this parameter helps in protecting sensitive information from being intercepted during the transmission. This is crucial for compliance with data protection regulations and maintaining the trust of users and stakeholders.

**Technical Impact when configured:** When enabled, this setting redirects all HTTP requests to HTTPS, effectively mitigating the risk of man-in-the-middle (MITM) attacks and ensuring that the communication between the client and the server is secured.

**Examples Scenario:** If a user attempts to access a webpage via HTTP, the server will automatically redirect the request to the HTTPS version of the webpage, ensuring that the data transmitted is encrypted.

**Related Settings:** Not mentioned in the provided code references.

**Best Practices:** Configure this setting for all web-based applications dealing with sensitive or confidential information to ensure data integrity and confidentiality. Avoid enabling this setting without first ensuring that your server is properly configured for HTTPS, to prevent access issues or downtime.