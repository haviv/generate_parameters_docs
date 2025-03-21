# Show Role Catalog Attribute8

**Technical Name:** ShowRoleCatalogAttribute8

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

Enables or disables the visibility of the Attribute8 field within the Role Catalog section of the Pathlock Cloud GRC platform. This setting is user-specific and allows for a customizable view of role-related data across the system.

**Business Impact:**

Adjusting this setting can affect how users interact with role data, potentially simplifying user interfaces for certain roles or focusing users' attention on more relevant role attributes for their specific workflow needs.

**Technical Impact when configured:**

When enabled, this configuration adds an additional column or data field related to Attribute8 within the Role Catalog, which could include custom or organization-specific role information essential for governance, risk management, and compliance activities.

**Examples Scenario:**

An organization decides that for certain users, understanding a role's specific attribute (Attribute8, which might relate to a proprietary categorization system) is crucial for compliance reporting. Enabling ShowRoleCatalogAttribute8 for these users would allow them to view and interact with this data directly within the Role Catalog, enhancing their ability to make informed decisions and reports.

**Related Settings:**

- ShowRoleCatalogAttribute7

**Best Practices:** configure when users require detailed role-related information for compliance or governance purposes; avoid when it is unnecessary for users to see this information, to maintain a cleaner, more user-friendly interface.