# Documentation for `ApplicationSignoutUrl` Parameter

## Category:
Security Configuration

## Default Value:
"~/ApplicationSignout.aspx"

## Impact Level:
Medium

## Description:
The `ApplicationSignoutUrl` parameter specifies the URL to which a user is redirected upon signing out of the Pathlock Cloud GRC platform. This URL is used to ensure that users are directed to a designated page that can provide further instructions, confirm sign out, or offer additional resources post-signout. By default, the system redirects users to a page named `ApplicationSignout.aspx` located in the root directory.

## Business Impact:
Proper configuration of the `ApplicationSignoutUrl` ensures that users experience a seamless transition when signing out of the Pathlock Cloud GRC platform, enhancing user experience and maintaining the security posture by directing users away from potentially sensitive areas upon logout. It can also be used for tracking logout activities when integrated with web analytics.

## Technical Impact when configured:
When configured, this setting:
- Redirects users to a predefined page after logout, preventing unauthorized access to the last accessed page due to browser caching.
- Enables customization of the logout experience, allowing organizations to provide specific messages or actions post-logout.
- Can be utilized to enhance security by directing users to a page that automatically clears browser cache or provides security reminders.

## Example Scenario:
An organization wishes to direct its users to a custom "Logout Successful" page that includes links to helpdesk information, user survey, and a login page for users to sign back into the platform. By setting the `ApplicationSignoutUrl` to the URL of this custom page (e.g., "~/CustomLogout.aspx"), organizations can enhance user experience and gather feedback from users post-logout.

## Related Settings:
- `SessionTimeoutUrl`: Specifies the URL to redirect users in case of session timeout.
- `LoginPageUrl`: URL for the custom login page.

## Best Practices:
- **Configure when**:
  - Customization of the logout page is needed to improve user experience, provide specific logout confirmations, or offer additional resources.
  - Enhanced security measures are desired to clear session data or display security reminders upon logout.
- **Avoid when**:
  - Default signout behavior and redirection to the `ApplicationSignout.aspx` page meets organizational requirements and user expectations.

By customizing the `ApplicationSignoutUrl`, organizations can tailor the logout process to meet their specific needs, reinforcing both security practices and user engagement.