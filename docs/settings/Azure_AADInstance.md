# Azure AADInstance

**Technical Name:** Azure_AADInstance

**Category:** Configuration

**Default Value:** 

**Impact Level:** High

**Description:** 

The Azure AADInstance parameter specifies the Azure Active Directory (AAD) instance used for authentication in the Pathlock Cloud GRC platform. This setting is crucial for ensuring that the application can correctly interact with Azure AD to authenticate users and services.

**Business Impact:**

Correct configuration of the Azure AADInstance ensures seamless authentication and authorization processes, providing secure access to the platform's features. It impacts user experience, security posture, and compliance with regulatory requirements regarding access control and data protection.

**Technical Impact when configured:**

When properly configured, the Azure AADInstance allows the Pathlock Cloud GRC platform to leverage Azure AD for managing user identities and access rights, enforcing authentication policies, and integrating with other security features like multi-factor authentication (MFA) and conditional access policies.

**Examples Scenario:**

- **Scenario 1:** An organization needs to ensure that only authenticated users can access specific GRC platform functionalities. By setting the Azure AADInstance to their Azure AD tenant, they can leverage Azure's robust authentication services.
- **Scenario 2:** A company uses multi-factor authentication (MFA) to add an additional layer of security. Configuring the Azure AADInstance parameter allows the GRC platform to require MFA, ensuring that users are who they claim to be.

**Related Settings:** 

- ForceHttpsForSiteRedirect
- CloudClientEncryptParameters

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for use within an organization that utilizes Azure Active Directory for user management and authentication.
- **Avoid when:** The organization does not use Azure Active Directory, or there is a need to use an alternative identity provider for authentication.