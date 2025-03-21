# UICulture

**Technical Name:** UICulture

**Category:** Configuration

**Default Value:** (No default value provided in the code references)

**Impact Level:** Medium

**Description:**

The `UICulture` parameter is used to define the locale for the user interface, ensuring that text, formats, and other localized resources match the chosen language and cultural norms. It is essential for adapting the software interface to meet the needs of users in different geographical regions.

**Business Impact:**

By correctly setting the `UICulture` parameter, organizations can enhance user experience, improve accessibility, and ensure that the Pathlock Cloud GRC platform is more intuitive for users worldwide. This contributes to better compliance management, risk assessment, and adherence to global standards by presenting information in a familiar context.

**Technical Impact when configured:**

Configuring the `UICulture` parameter impacts how localized resources are loaded within the application. This includes the display of text strings, date and number formats, and other cultural-specific information across different modules of the Pathlock Cloud GRC platform, leading to a customized user experience based on the selected locale.

**Examples Scenario:**

An organization with offices in France and Japan may set the `UICulture` to "fr-FR" for their French-speaking users and "ja-JP" for their Japanese-speaking users. This ensures that each user sees the interface in their local language, including error messages, compliance guidelines, and navigation elements.

**Related Settings:**

- Locale
- DateFormat

**Best Practices:** configure when the Pathlock Cloud GRC platform is being used by a diverse group of users from different linguistic backgrounds. Avoid when all users share the same language preferences, where a global setting may suffice.