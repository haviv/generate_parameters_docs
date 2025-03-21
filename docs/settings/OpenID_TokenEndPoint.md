# Open ID Token End Point

**Technical Name:** OpenID_TokenEndPoint

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Open ID Token End Point parameter is a key configuration in the Pathlock GRC platform that specifies the URL of the token endpoint in an OpenID Connect provider's configuration. This is essential for the initiation of the OAuth 2.0 authentication process, enabling secure access to user authentication and authorization.

**Business Impact:**

Proper configuration of this parameter ensures that user authentication processes are securely handled, supporting regulatory compliance and safeguarding sensitive information. Misconfiguration might lead to authentication issues, potentially jeopardizing system security and data integrity.

**Technical Impact when configured:**

When correctly configured, the system can securely communicate with the OpenID Connect provider to exchange authorization codes for tokens. This mechanism is foundational for accessing protected resources and services in a Cloud GRC platform like Pathlock.

**Examples Scenario:**

- **Scenario:** A company needs to secure access to its GRC dashboard and ensure that only authenticated users can access sensitive compliance data. By configuring the Open ID Token End Point with the URL provided by their OpenID Connect provider (e.g., Azure AD), the company ensures that authentication requests are properly routed and handled.

**Related Settings:**

- **OpenID_ResponseMode**
- **OpenID_JwksUri**
  
**Best Practices:** 

- **Configure when:** Setting up or reviewing the security configurations for your Pathlock GRC platform to ensure secure and compliant authentication workflows.
- **Avoid when:** If not using an OpenID Connect provider for authentication, ensure that default or misconfigured values do not impact other authentication mechanisms.