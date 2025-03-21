**Technical Name:** RolesRegistryNodes

**Category:** Configuration

**Default Value:** (Not provided in the code references)

**Impact Level:** Medium

**Description:**

This parameter specifies the registry node locations where role configurations for site map nodes are stored. It is utilized within the Pathlock Cloud GRC platform to dynamically adjust UI and feature access based on the roles defined in the registry settings.

**Business Impact:**

The correct configuration of this parameter is crucial for ensuring that the Pathlock GRC platform's navigation and accessible features align with the organization's governance, risk, and compliance (GRC) policies. Improper settings could lead to unauthorized access or visibility into sensitive areas of the application, impacting audit compliance and operational security.

**Technical Impact when configured:**

Once configured, the `RolesRegistryNodes` parameter directly affects how the application determines role-based access and visibility. It influences the generation of the dynamic site map used throughout the Pathlock GRC platform, ensuring that users see and interact only with the elements that their roles permit.

**Examples Scenario:**

- A company wants to limit access to advanced configuration settings to only IT administrators. By adjusting the `RolesRegistryNodes` settings, they can ensure that only users granted the specific IT administrator role in the registry have visibility and access to these settings.

**Related Settings:** CommonSettings.Default

**Best Practices:** configure when you need to align the platform's UI and feature access with specific role-based access control policies; avoid when not familiar with the registry settings structure or without testing in a non-production environment.