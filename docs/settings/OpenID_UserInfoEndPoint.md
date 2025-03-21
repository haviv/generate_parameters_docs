**Open ID User Info End Point**

**Technical Name:** OpenID_UserInfoEndPoint

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Open ID User Info End Point parameter specifies the endpoint URL where user information can be retrieved in an OpenID Connect (OIDC) compliant authentication flow. This parameter is crucial for configuring the integration with OIDC providers for identity verification and user authentication.

**Business Impact:**

Configuring the Open ID User Info End Point parameter correctly is essential for enabling secure user authentication and identity verification processes within the Pathlock Cloud GRC platform. It ensures that user credentials and identity data are handled securely, thereby maintaining the integrity and confidentiality of sensitive information.

**Technical Impact when configured:**

When configured, the Open ID User Info End Point enables the Pathlock Cloud GRC platform to retrieve user information from the OIDC provider, facilitating user authentication and identity verification. It ensures that the authentication process aligns with the organization's security and compliance requirements, leveraging OpenID Connect protocols.

**Examples Scenario:**

- **Scenario 1:** An admin configures the Open ID User Info End Point with the URL provided by their Azure Active Directory (Azure AD) instance. This setup ensures that when users log in to the Pathlock Cloud GRC platform, their identity is verified using Azure AD, aligning with the organization's security policies.

**Related Settings:**

- OpenID_TokenEndPoint
- OpenID_ResponseMode

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for single sign-on (SSO) with an OpenID Connect provider. Ensure the endpoint URL is correct and accessible from the Pathlock Cloud GRC platform.
  
- **Avoid when:** The organization does not use OpenID Connect for authentication or if the endpoint URL is not confirmed to be secure and correct by the identity provider.