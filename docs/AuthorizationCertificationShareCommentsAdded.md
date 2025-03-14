# AuthorizationCertificationShareCommentsAdded Parameter Documentation

## Category
Configuration

## Default Value
"Back to you !"

## Impact Level
Application Behavior

## Description
The `AuthorizationCertificationShareCommentsAdded` parameter is used within the application to define the default message sent when sharing certification comments via email upon the completion of a certification process.

## Business Impact
The utilization of this parameter directly affects the user experience by providing a customizable message encouraging interaction or acknowledgment upon sharing comments, which can potentially enhance engagement and communication efficiency during the certification review processes.

## Technical Impact when configured
When this parameter is configured:
- It alters the default message that is included in the automated email notifications sent to users who are part of a certification process when comments are added and shared.
- Ensures that communications sent out after comments have been added to a certification are in line with corporate or departmental tone and policy by allowing customization of the email message content.

## Example Scenario
In a scenario where a user has completed a certification review and added comments for consideration, setting the `AuthorizationCertificationShareCommentsAdded` parameter ensures that the recipient of these comments, upon receiving the email notification, sees a message that could be tailored to prompt specific actions or simply acknowledge receipt of the comments in a manner consistent with organizational communication standards.

## Related Settings
- Email Notification Settings
- Certification Process Configuration
- User Communication Preferences

## Best Practices
### Configure when:
- The default email message needs to reflect specific instructions, encouragement, or information aligned with the organizational tone and policy.
- Tailoring the communication to enhance user engagement and clarity regarding the shared comments is necessary.

### Avoid when:
- The default setting is sufficient for organizational needs and any change might introduce confusion or misalignment with established communication practices.

## Context
The parameter `AuthorizationCertificationShareCommentsAdded` is an integral part of the settings that influence the behavior of the application's certification review process, particularly in how users are notified and engaged through email communications. It exists within the application's common settings, allowing for a centralized configuration approach that benefits system administrators and end-users by providing clarity and consistency in application-generated communications.