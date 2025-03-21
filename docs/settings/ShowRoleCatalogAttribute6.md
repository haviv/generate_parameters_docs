# Show Role Catalog Attribute6

**Technical Name:** ShowRoleCatalogAttribute6

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

Enables or disables the visibility of the sixth attribute in the role catalog within the Pathlock Cloud GRC platform. This attribute is configurable to enhance or reduce the detail level in role catalog views based on organizational requirements.

**Business Impact:**

Controlling the visibility of this attribute can impact how role information is consumed by users and administrators. When enabled, it provides additional context or categorization that might be critical for decision-making processes related to role assignments, security policies, and compliance audits. When disabled, it simplifies the view, potentially improving usability for users who require less detail.

**Technical Impact: when configured**

When configured to show (true), the role catalog's detail level increases, potentially adding value to role analysis and audit processes by displaying additional attribute data. Conversely, setting this configuration to hide (false), simplifies the interface, which might benefit users needing fewer details for their tasks.

**Examples Scenario:**

- An organization requires that roles within its GRC platform are categorized not only by their business unit and role category but also by a specific attribute like project code or confidentiality level. Enabling `ShowRoleCatalogAttribute6` would allow this additional information to be displayed in the role catalog, assisting in more informed role management decisions.

**Related Settings:**

- ShowRoleCatalogAttribute5

**Best Practices:** configure when needing additional attribute visibility for comprehensive role categorization or audit purposes, avoid when simplicity in role catalog views is preferred.