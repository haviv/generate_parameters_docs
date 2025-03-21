**Technical Name:** DefaultMenuIcon

**Category:** Configuration

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

This parameter controls the default icon used for menu items within the Pathlock Cloud GRC platform interface. It ensures a consistent user experience by providing a standard visual cue across various parts of the application.

**Business Impact:**

Using a default menu icon helps in maintaining a uniform look and feel across the application, enhancing the user's ability to navigate and use the platform efficiently. A well-chosen icon can also aid in faster recognition of menu functions, improving overall user satisfaction and productivity.

**Technical Impact when configured:**

When the DefaultMenuIcon parameter is configured, all new menu items that are created without a specifically assigned icon will automatically use this default icon. This helps in keeping the user interface consistent and intuitive.

**Examples Scenario:**

- **Improving Navigation:** A company could set a generic icon for all menu items related to report generation. This way, users can quickly identify all reporting-related functions, enhancing navigation speed.
- **Brand Consistency:** An organization can use a branded icon as the default menu icon to maintain brand consistency throughout the user interface. 

**Related Settings:**

- `SiteSmallIcon` - Controls the icon used for site map nodes in navigation.

**Best Practices:** 

- **Configure when:** Developing a new module or adding new menu items to ensure consistency across the application without specifying icons for each item.
- **Avoid when:** Individual menu items require unique icons to differentiate their functions significantly.