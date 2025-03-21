# Send Password View Mail

**Technical Name:** SendPasswordViewMail

**Category:** User Management

**Default Value:** 

**Impact Level:** High

**Description:**

This configuration parameter controls whether email communication containing password views or credentials is sent out from the Pathlock Cloud GRC platform upon specific user-related workflow actions. It primarily targets scenarios involving new user creation or modifications to user authorizations where direct notification to the user is required for immediate access.

**Business Impact:**

Enabling this parameter ensures that users are promptly informed of their access credentials, facilitating swift onboarding or access modification. It enhances user experience by reducing the waiting time for access and supports secure communication of sensitive information. Conversely, improper handling or disabling of this feature could delay user access to critical applications or data, impacting productivity and potentially compromising security practices around credential distribution.

**Technical Impact when configured:**

- Automates the distribution of credentials, reducing administrative overhead.
- Ensures secure delivery of sensitive information via email, assuming adherence to email security practices.
- Directly influences the speed at which users gain access to necessary systems or data.
- Requires careful management to prevent unauthorized access, considering the sensitivity of email content.

**Examples Scenario:**

- **Onboarding a New Employee:** Upon using the CreateNewUser workflow action, the SendPasswordViewMail parameter ensures the new employee receives their system credentials via email, allowing for immediate access to required systems.
- **Authorization Update:** After applying the ApplyAuthorizationAction, a user might receive an email containing new credentials or access confirmations if changes necessitate such communication.

**Related Settings:**

- ActiveDirectoryAccountDisableOnly

**Best Practices:** 

- **Configure when:** Immediate user access upon creation or authorization update is critical for business operations. Ensure email security practices are enforced to protect the sensitive information being transmitted.
- **Avoid when:** The organization has strict policies against sending sensitive information via email or if alternative, more secure credential distribution methods are preferred.