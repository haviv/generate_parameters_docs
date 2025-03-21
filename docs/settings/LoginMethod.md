**Login Method**

**Technical Name:** LoginMethod

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `LoginMethod` parameter specifies the authentication mechanism that users must utilize to access the Pathlock Cloud GRC platform. It determines how users prove their identity and gain access to the system, ensuring that only authorized individuals can access sensitive compliance, risk, and security management functionalities.

**Business Impact:**

Using the right login method is crucial for maintaining the security integrity of the GRC platform. It affects who can access the system and how securely they can interact with sensitive data. By configuring it properly, organizations can ensure that their GRC practices comply with relevant security standards and regulations, thereby mitigating potential risks associated with unauthorized access or data breaches.

**Technical Impact when configured:**

When configured, the `LoginMethod` parameter enforces a specific authentication protocol, changing how users are validated before granted access to the platform. Depending on the chosen method, it might require additional setup, such as configuring external authentication services or managing security tokens.

**Examples Scenario:**

For example, an organization may decide to switch from simple username and password authentication to a more secure OpenID Connect based login method. This change would significantly enhance security by reducing the risk of password-related breaches and enabling additional features like multi-factor authentication (MFA).

**Related Settings:**

- MinimalMode (in relation to how the UI is rendered post-login)
- Api_OpenBy (pertaining to API-triggered actions post-authentication)

**Best Practices:** 

- Configure the login method to use robust authentication mechanisms (like SAML, OpenID Connect) especially if handling sensitive data.
- Avoid using simple, less secure login methods for environments where security and data integrity are paramount.