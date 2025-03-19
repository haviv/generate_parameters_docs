# NewUserAccountHeader Documentation

## Category
Email Notification

## Default Value
"Your New Account"

## Impact Level
Moderate

## Description
The `NewUserAccountHeader` parameter is used to configure the subject line for emails sent to new users as part of their account creation process. It serves as the first impression to new users and is critical for setting the tone of their initial interaction with the Pathlock Cloud GRC platform.

## Business Impact
A well-crafted header can enhance the user's initial perception of the organization, establish trust, and encourage them to engage more readily with the platform. It impacts how quickly and effectively new users begin interacting with the system, thereby affecting their overall compliance and security posture from the start.

## Technical Impact when configured
When this parameter is configured, all outgoing emails to new users will utilize this setting for the email subject line. This ensures consistency in communication and reinforces brand identity. It directly influences the rate at which new users open and engage with the email, thus affecting the speed of their onboarding process.

## Example Scenario
- **Scenario:** An organization wants to ensure that new user onboarding emails are immediately recognizable and reflect the organization's culture.
- **Implementation:** They customize the `NewUserAccountHeader` to "Welcome to Your New Security Dashboard!" to make the email stand out and to underline the importance of security from day one.
- **Outcome:** New users recognize the importance placed on security by the organization, leading to higher email open rates and faster engagement with the platform.

## Related Settings
- **Email Body Customization:** Parameters that allow for the customization of the email's body content.
- **Email Server Configurations:** Settings related to the email delivery system such as SMTP server details.

## Best Practices
- **Configure when:** You wish to customize the onboarding experience for new users or when you need to align the email communications with branding guidelines.
- **Avoid when:** The default value suffices for your organization's needs or in situations where consistency with existing user communication is not prioritized.

By thoughtfully configuring the `NewUserAccountHeader`, organizations can significantly enhance the initial user experience, promoting a smoother transition to using the Pathlock Cloud GRC platform and reinforcing the importance of compliance and security from the start.