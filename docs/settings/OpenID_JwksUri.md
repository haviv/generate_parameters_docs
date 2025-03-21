# Open ID Jwks Uri

**Technical Name:** OpenID_JwksUri

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:** The Open ID Jwks Uri parameter specifies the location (URL) of the JSON Web Key Set (JWKS) used by an OpenID provider. The JWKS is a set of keys containing the cryptographic keys used for validating the identity of the OpenID provider and for securing the communication between the client and the OpenID provider.

**Business Impact:** Configuring the Open ID Jwks Uri correctly is critical for the security of the authentication process in applications integrated with an OpenID Connect provider. It ensures that the identity provider can be trusted and that the tokens issued by the provider can be verified accurately.

**Technical Impact when configured:** When properly configured, this parameter enables the secure validation of tokens issued by the OpenID Connect provider. It helps to prevent unauthorized access and ensures that the communication between the application and the provider is secure.

**Examples Scenario:** 
- An organization integrating their Pathlock GRC platform with an Azure Active Directory (AAD) for Single Sign-On (SSO) would need to configure the Open ID Jwks Uri parameter to point to AAD's JWKS URL. This ensures that the SSO process is secure and that the tokens issued by AAD can be verified by the Pathlock GRC platform.

**Related Settings:** 
- OpenID_AuthorizationEndpoint
- OpenID_ResponseMode

**Best Practices:** 
- **Configure when** setting up Single Sign-On (SSO) or any form of secure authentication with an OpenID Connect provider to ensure the integrity and security of the authentication process.
- **Avoid when** the application does not use OpenID Connect for authentication or when the JWKS URL is not available or valid, as this could compromise security.