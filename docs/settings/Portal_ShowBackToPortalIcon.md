**Technical Name:** Portal_ShowBackToPortalIcon

**Category:** Configuration

**Default Value:**

**Impact Level:** Low

**Description:**

The `Portal_ShowBackToPortalIcon` parameter controls the visibility of the "Back to Portal" icon in the Pathlock Cloud GRC platform interfaces. This icon, when displayed, provides users with a quick way to navigate back to the main portal/dashboard from various points within the application.

**Business Impact:**

Enabling this feature enhances user navigation and improves the overall user experience by providing a clear and immediate path back to the portal dashboard. It can be particularly useful for users who navigate deep into the application's module structure, ensuring they can easily return to the home page without needing to use the browser's back button or navigate through a complex menu structure.

**Technical Impact when configured:**

When enabled, the "Back to Portal" icon is made visible across various parts of the application, depending on where the user is within the Pathlock platform. If disabled, users might find it slightly more cumbersome to navigate back to the main dashboard, potentially impacting their efficiency and usage satisfaction.

**Examples Scenario:**

- A user navigates from the main portal to the detailed settings of a particular compliance report. After reviewing or modifying the settings, the user can directly click the "Back to Portal" icon to return to the main dashboard without multiple clicks or navigation steps.

**Related Settings:** 

- `PathlockLogoUrl`: Controls the URL to which the "Back to Portal" icon redirects, typically set to the home page or main dashboard of the Pathlock Cloud GRC platform.

**Best Practices:** configure when the application's navigation is deep or complex, avoid when the application has a simple structure and additional navigation aids would clutter the interface.