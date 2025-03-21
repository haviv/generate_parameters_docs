# Show Role Catalog Attribute5

**Technical Name:** ShowRoleCatalogAttribute5

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of an additional attribute within the role catalog. When enabled, it allows users to see and potentially interact with an extra layer of information pertinent to roles within the Pathlock GRC platform.

**Business Impact:**

Enabling this attribute can enhance user understanding of roles by providing more detailed information, which could aid in better security and compliance management. It might also improve decision-making processes related to role assignment and management.

**Technical Impact when configured:**

Upon activation, the specific attribute becomes visible and actionable within the role catalog interface. This may impact load times slightly due to the additional data being processed but primarily enhances information availability and granularity.

**Examples Scenario:**

An organization wants to provide its GRC platform users with more context about the roles being assigned within its environment. By enabling ShowRoleCatalogAttribute5, they can include a new dimension of data such as "Business Unit" related information directly visible within the role catalog. This helps in making more informed decisions when assigning roles.

**Related Settings:**

- ShowRoleCatalogAttribute4

**Best Practices:** Configure this parameter when there is a clear business or operational need to expose additional attributes within the role catalog for enhanced role management. Avoid enabling it if the extra information adds no value or unnecessarily complicates the role assignment process.