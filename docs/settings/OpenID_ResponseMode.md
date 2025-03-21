# Open ID Response Mode

**Technical Name:** OpenID_ResponseMode

**Category:** Security

**Default Value:** None provided

**Impact Level:** High

**Description:** The Open ID Response Mode parameter influences how the response from an OpenID provider is sent back to the client. It is a crucial part of the authentication process, affecting the security and functionality of the authentication flow within the Pathlock Cloud GRC platform.

**Business Impact:** Proper configuration of this parameter ensures that authentication responses are handled securely and efficiently, enhancing the overall security posture of the organization. Misconfiguration can lead to potential vulnerabilities, exposing sensitive information and jeopardizing the integrity of the GRC platform.

**Technical Impact when configured:** When correctly configured, the Open ID Response Mode parameter ensures that the authentication responses from the OpenID provider are transmitted in a manner that aligns with the security requirements of the Pathlock Cloud GRC platform. This may involve specifying how responses are encoded, transported, and received, which directly impacts the robustness of the authentication mechanism.

**Examples Scenario:** A large corporation requires that all authentication responses from their OpenID provider be transmitted via the fragment response mode to enhance security by preventing URLs from being logged by web servers. By configuring the Open ID Response Mode parameter accordingly, they can ensure that sensitive information in the authentication response is adequately protected against potential interception and logging vulnerabilities.

**Related Settings:** Azure_AADInstance, Azure_ClientId, Azure_ClientSecret

**Best Practices:** 
- Configure when: It is essential to meet specific security requirements dictated by the organization's security policy or compliance standards.
- Avoid when: The default response mode meets the platform's security and functionality needs without any modifications.