# Custom Role For Usage

**Technical Name:** CustomRoleForUsage

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `CustomRoleForUsage` parameter is designed to specify a custom role within the Pathlock Cloud GRC platform that targets specific user operations in the context of Central Users Administration and General UI settings. It plays a significant role in tailoring access and permissions for users, ensuring that administrative tasks are handled securely and efficiently.

**Business Impact:**

Configuring the `CustomRoleForUsage` parameter enables organizations to refine their governance models by creating roles that are closely aligned with their operational requirements and risk management strategies. This customization facilitates precise control over user permissions, minimizing the risk of unauthorized access or actions within the system.

**Technical Impact when configured:**

Upon configuring the `CustomRoleForUsage` parameter, the system enforces the specified role's permissions across the platform. This directly impacts user access levels, available actions in the user interface, and how workflows involving user data and permissions are managed. It ensures that users can only perform actions within their designated permissions, enhancing the overall security posture.

**Examples Scenario:**

A company needs to create a custom role for their HR department to allow them to only view and edit employee records without accessing financial or audit logs. By setting up `CustomRoleForUsage` with permissions tailored to these requirements, the HR department can efficiently manage employee data while adhering to the principle of least privilege.

**Related Settings:**

- CustomCUASystemNumber
- CustomDomain

**Best Practices:** configure when you need to enforce specific control over user actions and permissions within Pathlock Cloud GRC. Avoid using generic roles where specific role-based access control is necessary to mitigate risks associated with broad permissions.