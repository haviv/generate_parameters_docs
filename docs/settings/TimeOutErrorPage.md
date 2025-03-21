# Time Out Error Page

**Technical Name:** TimeOutErrorPage

**Category:** Configuration

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

The Time Out Error Page parameter is used to specify a custom web page that users are redirected to when a session times out due to inactivity. This is particularly useful for enhancing user experience by providing a more informative or branded error page instead of a generic browser error message.

**Business Impact:**

Customizing the Time Out Error Page can significantly improve the user interface and user experience within the Pathlock Cloud GRC platform. It enables organizations to maintain their branding consistency, reduces user frustration by clearly informing them of the session timeout, and guides them on what steps to follow next, potentially reducing support ticket volumes.

**Technical Impact when configured:**

Upon configuration, any session timeout will redirect users to the specified error page rather than the default error message or page. This allows for a more graceful handling of session expirations and can be used to provide users with context-specific information or actions (e.g., a login link or support contact information).

**Example Scenario:**

An organization configures the Time Out Error Page to redirect users to a custom-branded page with a message "Your session has expired due to inactivity. Please click here to log in again." This improves the user experience by clearly explaining why they were logged out and offering an immediate way to log back in.

**Related Settings:** Not applicable based on the provided code references.

**Best Practices:** Configure when you want to improve the user experience by replacing the default timeout message with a more informative and visually consistent error page. Avoid custom configurations that could confuse users about their session state or how to return to their workflow.