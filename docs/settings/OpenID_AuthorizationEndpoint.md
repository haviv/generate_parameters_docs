# Open ID Authorization Endpoint

**Technical Name:** OpenID_AuthorizationEndpoint

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Open ID Authorization Endpoint parameter specifies the URL endpoint used to authenticate users through OpenID Connect protocol. It is a critical setting for applications using OpenID for user authentication, ensuring secure login and access control.

**Business Impact:**

Configuring the Open ID Authorization Endpoint correctly is crucial for maintaining secure access to the Pathlock Cloud GRC platform. It enables secure user authentication and authorization, preventing unauthorized access and thereby protecting sensitive compliance and risk management data.

**Technical Impact when configured:**

When the Open ID Authorization Endpoint is properly configured, the system securely communicates with the designated OpenID provider. This setup ensures that authentication requests are properly redirected to the OpenID provider, and only authenticated users can access the application.

**Examples Scenario:**

If an organization uses Microsoft Azure Active Directory as their identity provider, the Open ID Authorization Endpoint would be configured to point to the Azure AD authorization endpoint URL, enabling users to authenticate with their Azure AD credentials when accessing the Pathlock Cloud GRC platform.

**Related Settings:**

- OpenID_Issuer
- OpenID_ResponseMode

**Best Practices:** 

- Configure the Open ID Authorization Endpoint at the initial setup stage of the Pathlock Cloud GRC platform to ensure that user authentication processes are secure from the start.
- Avoid hard-coding the endpoint in the application; instead, use a configuration setting that can be easily updated if the endpoint changes.