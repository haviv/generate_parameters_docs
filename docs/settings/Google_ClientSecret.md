# Google Client Secret

**Technical Name:** Google_ClientSecret

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The Google Client Secret is a confidential code provided by Google when you register your application with the Google Developer Console. It is used in combination with the Google Client ID to authenticate and authorize your application to access Google APIs securely.

**Business Impact:**

Misconfiguration or exposure of this secret can lead to unauthorized access to Google services and data associated with your application, posing significant security and privacy risks to your organization and its users. Proper management of this secret is crucial for maintaining the integrity and confidentiality of the application and its data.

**Technical Impact when configured:**

- Ensures secure authentication flow between your Pathlock GRC platform and Google's OAuth 2.0 servers.
- Prevents unauthorized access to Google APIs, protecting sensitive application and user data.
- Facilitates secure integration with Google services for features such as Single Sign-On (SSO), access to Google Workspace data, etc.

**Examples Scenario:**

1. Implementing Single Sign-On (SSO) using Google accounts to streamline user access to the Pathlock GRC platform.
2. Automating the import of audit logs or user activities from Google Workspace into the Pathlock GRC platform for enhanced visibility and compliance tracking.

**Related Settings:**

- Azure_TenantId
- Azure_PostLogoutRedirectUri

**Best Practices:** 

- Configure when initializing OAuth2.0-based authentication with Google services.
- Avoid when your application does not require direct integration with Google OAuth2.0 for authentication or data access. Store securely and rotate periodically to mitigate potential security risks.