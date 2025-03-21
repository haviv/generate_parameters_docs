# Disable Analytical Views

**Technical Name:** DisableAnalyticalViews

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The DisableAnalyticalViews parameter controls the visibility and availability of analytical views within the reporting modules of the Pathlock Cloud GRC platform. When enabled, this parameter hides analytical views, which can affect how users interact with and analyze reporting data.

**Business Impact:**

Enabling the DisableAnalyticalViews parameter can streamline the user interface by hiding complex analytical views that are not required for all users. This can simplify user experience for those who need access only to standard reports, reducing information overload and focusing on essential data. However, it may limit data analysis capabilities for advanced users who rely on these views for deeper insights into GRC data.

**Technical Impact when configured:**

- Hides the analytical views and related charts from the dashboard and report pages.
- May improve page load times by reducing the amount of data processed and displayed.
- Users may need to rely on alternative methods for detailed data analysis and visualization.

**Examples Scenario:**

A company wants to ensure that its GRC platform is user-friendly and not overwhelming for new users. By disabling analytical views, they can provide a simplified interface that focuses on standard reports and essential data, making it easier for users to navigate and understand the platform.

**Related Settings:**

- `DataExceptionsBatchSize`

**Best Practices:** 

- **Configure when**: Simplification of the report interface is necessary, or when analytical views provide little to no additional value to certain user groups.
- **Avoid when**: In-depth data analysis and complex visualizations are critical for the organization’s risk management and decision-making processes.