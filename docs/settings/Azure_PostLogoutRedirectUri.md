# Azure Post Logout Redirect Uri

**Technical Name:** Azure_PostLogoutRedirectUri

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the URL to which a user will be redirected after successfully logging out from the application. It is essential for maintaining a seamless user experience and ensuring that users are directed to a safe and intended destination after logout.

**Business Impact:**

Properly setting the Azure Post Logout Redirect Uri ensures that users are navigated to a preferred page or application upon logout, enhancing the user experience and maintaining the flow of interaction with your platform or applications. It also aids in security by directing users away from sensitive sessions.

**Technical Impact when configured:**

When configured, this setting ensures that authentication flows are correctly managed and users are redirected to an authorized URL post logout. This can prevent exposure to open redirect vulnerabilities, which could be exploited by attackers to redirect users to malicious sites after logout.

**Examples Scenario:**

A financial organization uses the Pathlock Cloud GRC platform for managing its GRC processes. They configure the Azure Post Logout Redirect Uri to redirect users to the company’s internal homepage after logging out, ensuring that users return to a secure, familiar environment and can quickly access other company resources if needed.

**Related Settings:**

- Azure_ClientId
- Azure_AADInstance

**Best Practices:** configure when setting up or updating your authentication mechanisms to provide a fluid and secure user experience; avoid when you do not have a specific post-logout destination in mind or when the default behavior aligns with your security policies.