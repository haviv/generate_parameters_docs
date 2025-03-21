# Open ID Issuer

**Technical Name:** OpenID_Issuer

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**  
The Open ID Issuer parameter is used to specify the unique identifier of the OpenID Provider (OP) that will be used for authenticating users. This is a crucial setting in the integration of OpenID Connect authentication within the Pathlock Cloud GRC platform, enabling secure and streamlined user authentication processes.

**Business Impact:**  
Configuring the Open ID Issuer correctly is essential for ensuring that authentication services operate smoothly, directly impacting user access control, security measures, and overall system integrity. Incorrect configuration may result in authentication failures or security vulnerabilities.

**Technical Impact when configured:**  
Proper configuration ensures that the system can communicate effectively with the OpenID Provider, facilitating secure user authentication and authorization processes. It allows the system to decode and validate JWT tokens, and access user information from the OpenID Provider, necessary for user authentication and authorization.

**Examples Scenario:**  
- **Scenario 1:** To integrate Azure Active Directory (Azure AD) as an OpenID Provider, the Open ID Issuer parameter would require the issuer URL provided by Azure AD. This ensures that authentication requests are directed appropriately to Azure AD for user authentication.
  
- **Scenario 2:** If a company is using Google as their OpenID Connect provider, they would set the Open ID Issuer to Google's issuer URL. This setup mandates that the Pathlock Cloud GRC platform delegates user authentication to Google, harnessing Google's security protocols for user identity verification.

**Related Settings:**  
- `OpenID_ResponseMode`

**Best Practices:** 
- **Configure when:** Setting up third-party authentication services for the first time or when changing identity providers.
- **Avoid when:** If not using OpenID Connect for authentication or if unsure about the issuer's information. Always verify the issuer URL before applying the settings to avoid disruptions in authentication services.