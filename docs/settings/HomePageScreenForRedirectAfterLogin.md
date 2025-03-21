# Home Page Screen For Redirect After Login

**Technical Name:** HomePageScreenForRedirectAfterLogin

**Category:** Configuration

**Default Value:** StartPage.aspx

**Impact Level:** Medium

**Description:**

This setting determines the initial page users are directed to immediately after logging in, providing a streamlined entry point into the Pathlock Cloud GRC platform that is relevant to the user's needs and the organization's security policies.

**Business Impact:**

Setting an appropriate home page improves user experience by providing immediate access to relevant functionalities and information, supporting efficient workflow navigation, and enforcing security policies through controlled access.

**Technical Impact when configured:**

Configuring this parameter affects the first interaction users have with the Pathlock Cloud GRC platform after login. An optimal configuration ensures that users are directed to a page that aligns with their roles, responsibilities, and security permissions within the organization.

**Examples Scenario:**

- **Enhanced User Experience**: Configuring this parameter to redirect users to a dashboard customized to their role increases efficiency and user satisfaction.
- **Security Compliance**: Directing users to a compliance checklist page right after login helps in maintaining a focus on crucial security and compliance tasks.

**Related Settings:** 

- `CommonSettings.Default.EnableModernStyle`
- `CommonSettings.Default.SiteAddress`

**Best Practices:** configure when setting up the system for the first time to ensure that users are directed to the most appropriate page based on their role within the organization, avoid when users have varied roles that do not align with a single entry point.