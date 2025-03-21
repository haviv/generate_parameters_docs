# SMS New User Account Password

**Technical Name:** SMSNewUserAccountPassword

**Category:** User Management

**Default Value:** True

**Impact Level:** Medium

**Description:** A parameter that enables the sending of new user account passwords via SMS.

**Business Impact:** Facilitates secure and immediate delivery of new account credentials directly to the user's mobile device, enhancing user onboarding experience and security.

**Technical Impact when configured:** When enabled, new user account passwords are sent via SMS to the user's registered mobile number. This ensures that the user can securely receive and use their new account credentials without relying on email delivery, which can be slower or less secure.

**Example Scenario:** A new employee is added to the organization's GRC platform. Upon creation of their user account, the system automatically generates a secure password and sends it to the new user's mobile phone via SMS, allowing immediate and secure access to the system.

**Related Settings:** 

- SendPasswordViewSMS

**Best Practices:** 

- **Configure when:** Immediate and secure delivery of new account passwords is required, especially in environments where email delivery is unreliable or considered less secure.
  
- **Avoid when:** Users do not have access to a mobile device or in regions where SMS services are unreliable.