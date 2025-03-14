# SendPasswordViewMail Parameter Documentation

## Category:
Security and Notifications

## Default Value:
The default setting for `SendPasswordViewMail` is derived from `CommonSettings`. It is not explicitly stated, but it is suggested that it defaults to either true or false based on organizational security policies.

## Impact Level:
Medium to High

## Description:
The `SendPasswordViewMail` parameter controls whether a newly created user or a user with updated authorization receives an automatic email containing their password or password reset link. This setting is crucial for initial account access and subsequent secure operations within the Pathlock Cloud GRC platform.

## Business Impact:
- Ensuring that new users or users with newly granted authorizations can securely access their accounts without delay.
- Enhances user experience by streamlining the account setup and access process.
- Mitigates the risk of unauthorized account access by directly sending sensitive information to the verified email of the user.
- May be subject to compliance with organizational or regulatory policies regarding the transmission of sensitive information via email.

## Technical Impact when configured:
- Activating this setting entails the automatic generation and dispatch of emails containing sensitive information, requiring robust email security protocols.
- Requires the system to have accurate and secure email addresses for users to prevent data breaches.
- Could increase the server workload and necessitate careful management of email sending quotas and rates to avoid being blacklisted by email service providers.

## Example Scenario:
**Situation:** A new employee joins the organization and requires immediate access to the Pathlock Cloud GRC platform to begin their training and compliance tasks.
**Without `SendPasswordViewMail` enabled:** The process to manually communicate login credentials can be slow, error-prone, and insecure, delaying the onboarding process.
**With `SendPasswordViewMail` enabled:** The system automatically sends the new employee their password or password reset link, allowing for a swift and secure onboarding process.

## Related Settings:
- `new_user_creation_notification_disable`: This setting, if enabled, can override the `SendPasswordViewMail` parameter, preventing the automatic email dispatch.
- CustomParameters: Specific to individual workflows, where unique parameters can further refine when and how emails are sent to users.

## Best Practices:
- **Configure when:** Immediate and secure user access is a priority, and the organization has robust email security measures in place.
- **Avoid when:** The organization lacks secure email protocols, or there are strict regulations against sending sensitive information via email. In such cases, alternative secure credential sharing mechanisms should be employed.

In conclusion, the `SendPasswordViewMail` parameter plays a significant role in the security and operational efficiency of the Pathlock Cloud GRC platform, influencing both user experience and compliance with security policies. Its configuration should be carefully considered within the context of an organization's overall security strategy and regulatory obligations.