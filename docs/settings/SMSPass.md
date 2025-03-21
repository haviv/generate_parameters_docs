# SMS Pass

**Technical Name:** SMSPass

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The SMS Pass parameter is used within the Pathlock Cloud GRC platform to facilitate secure SMS message transmission. It acts as a key component in confirming and managing user identities by leveraging a second factor of authentication through SMS messages.

**Business Impact:**

Incorporating the SMS Pass parameter enhances the security of sensitive business operations by adding an additional layer of verification. This is particularly crucial in preventing unauthorized access and ensuring that operations related to security, risk, and compliance management are executed by authenticated users only.

**Technical Impact when configured:**

When configured, the SMS Pass parameter enables secure communication between Pathlock’s server and the SMS service provider. This setup ensures that SMS messages containing sensitive information or prompts for secondary authentication are delivered in a secure manner, directly contributing to the platform's overall security posture.

**Examples Scenario:**

- **Two-Factor Authentication:** When a user attempts to log into the Pathlock platform, an SMS message is sent to their mobile device containing a unique code. The user must enter this code along with their password to gain access, thereby providing a dual layer of security.
  
**Related Settings:**

- SMSUser

**Best Practices:** 

- **Configure when:** Implementing or strengthening the two-factor authentication system within your organization to ensure that access to sensitive information and critical systems is securely managed.
  
- **Avoid when:** If SMS-based communication is not possible or if an alternative form of secure authentication is preferred that better suits organizational needs or infrastructure.