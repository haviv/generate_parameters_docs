# Post Login Home Page Screen Admin Roles

**Technical Name:** PostLoginHomePageScreenAdminRoles

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

Specifies the roles that are allowed to access the post-login homepage screen when using the modern style interface in Pathlock Cloud GRC platform.

**Business Impact:**

Controls access to critical features and information available right after login, ensuring that only authorized users with specified roles can view and interact with the designated home page content. This helps in enforcing role-based access control, reducing the risk of unauthorized access to sensitive information and features.

**Technical Impact when configured:**

Restricts the post-login homepage screen access to users having specified admin roles. This is crucial for maintaining a secure and organized user interface, where only the users with necessary roles are granted access to the system's functionalities right after login.

**Examples Scenario:**

- If the organization wants to ensure that only IT administrators and compliance managers can view certain dashboard widgets or reports available on the post-login homepage, the `PostLoginHomePageScreenAdminRoles` parameter can be configured to include just these roles.

**Related Settings:** EnableModernStyle, SiteAddress

**Best Practices:** configure when you need to restrict access to the post-login homepage to certain roles to enhance security and user experience, avoid when all users require equal access to the post-login homepage features.