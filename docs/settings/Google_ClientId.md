# Google Client

**Technical Name:** Google_ClientId

**Category:** Configuration

**Default Value:** *(not specified)*

**Impact Level:** High

**Description:**

The `Google_ClientId` parameter specifies the unique identifier assigned by Google to your application. This ID enables your application to utilize Google's OAuth 2.0 authentication system for user identification and authorization, allowing users to sign in with their Google accounts.

**Business Impact:**

Using the `Google_ClientId` enhances the security and ease of use of the Pathlock Cloud GRC platform by leveraging Google's reliable authentication framework. It ensures a trustworthy and streamlined login process, reducing the risk of unauthorized access and improving user satisfaction by simplifying the sign-in procedure.

**Technical Impact when configured:**

Configuring the `Google_ClientId` correctly enables secure communication with Google's authentication services. It is essential for initiating OAuth 2.0 authorization flows, facilitating secure access to user data with Google accounts, and managing session states effectively.

**Example Scenario:**

An administrator wishes to integrate Google's authentication with Pathlock Cloud GRC to simplify login processes and enhance security. By setting the `Google_ClientId`, they enable users to sign in using their Google credentials, avoiding the need to manage separate usernames and passwords for the Pathlock platform.

**Related Settings:**

- Azure_AADInstance
- Azure_TenantId

**Best Practices:** 

- **Configure when:** you are integrating Pathlock Cloud GRC platform with Google's authentication system to simplify and secure user logins.
- **Avoid when:** there is no requirement to authenticate users through Google, or if using a different authentication provider.