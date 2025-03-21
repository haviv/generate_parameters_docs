# Show Forget Password Link In Login Page

**Technical Name:** ShowForgetPasswordLinkInLoginPage

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the "Forget Password" link on the login page of the Pathlock Cloud GRC platform. When enabled, it allows users to initiate the password reset process directly from the login page, enhancing user experience by providing an easy way to recover access in case of forgotten passwords.

**Business Impact:**

Enabling this feature improves user autonomy by allowing them to reset forgotten passwords without the need to contact the support team, thereby reducing the support team's workload. It also minimizes downtime for users who have forgotten their passwords, ensuring they can regain access to the platform promptly, which is crucial for maintaining operational efficiency.

**Technical Impact when configured:**

When this setting is configured to show the "Forget Password" link, the login page dynamically includes a link that directs users to the password reset process. This could potentially increase the workload on the system managing password resets and email notifications, but it significantly enhances user experience by streamlining access recovery.

**Examples Scenario:**

A user attempts to log in to the Pathlock Cloud GRC platform but realizes they have forgotten their password. Instead of reaching out to the support team and waiting for assistance, the user clicks on the "Forget Password" link available on the login page. They are then guided through the steps to reset their password, allowing for a quick and efficient resolution to their access issue.

**Related Settings:** ResetPasswordWelcomeLabel2Text

**Best Practices:** configure when user management policies support self-service password reset practices to enhance user experience and reduce support team workload; avoid when there is a policy or security concern that restricts users from independently reseting their passwords.