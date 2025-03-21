# Saml Entity

**Technical Name:** Saml_EntityId

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The Saml_EntityId parameter is a configuration setting within the Pathlock Cloud GRC platform that specifies the unique entity identifier for the SAML (Security Assertion Markup Language) integration. This identifier is used to facilitate secure communications between the Pathlock platform and SAML identity providers.

**Business Impact:**

The correct configuration of the Saml_EntityId is critical for the seamless and secure operation of single sign-on (SSO) capabilities within organizations. It affects the integrity of the authentication process, ensuring that only authorized users gain access to the GRC platform. Misconfiguration can result in access issues, hindering compliance and risk management workflows.

**Technical Impact when configured:**

Properly configuring the Saml_EntityId ensures secure and efficient user authentication via SAML. It enables the organization to leverage SSO capabilities, reducing password fatigue among users and minimizing the potential for security breaches through compromised credentials.

**Examples Scenario:**

- **Scenario:** An organization wishes to implement SSO to streamline their login processes and enhance security. By setting up the Saml_EntityId, they can integrate their GRC platform with their identity provider, allowing users to authenticate once and gain access to all necessary systems, including the Pathlock Cloud GRC platform.

**Related Settings:**

- `Azure_AADInstance`
- `Azure_ClientId`
- `Azure_ClientSecret`
- `Azure_PostLogoutRedirectUri`

**Best Practices:** 

- **Configure when:** Setting up SSO capabilities for the first time or when changing the identity provider to ensure seamless access control and authentication.
- **Avoid when:** Not using SAML for authentication, as incorrect or unnecessary configuration can complicate or disable access to the GRC platform.