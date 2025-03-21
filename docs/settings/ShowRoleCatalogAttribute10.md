# Show Role Catalog Attribute10

**Technical Name:** ShowRoleCatalogAttribute10

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

Enables or disables the visibility of an additional attribute (Attribute10) in the Role Catalog. This attribute can be used for further detailing roles within the catalog, providing more precise control and visibility over role properties.

**Business Impact:**

Activating this attribute can enhance the granularity of role descriptions in the catalog, potentially improving role governance and clarity for GRC processes. It may affect how roles are classified, searched, and filtered within the platform, impacting role assignment and compliance activities.

**Technical Impact when configured:**

When enabled, Attribute10 will be visible and configurable within the Role Catalog. This increases the data points available for roles, allowing for more detailed categorization, reporting, and analysis.

**Examples Scenario:**

A company wishes to add a custom attribute to their roles in the Role Catalog that specifies if a role is considered critical for audit purposes. By enabling ShowRoleCatalogAttribute10, they can add this information directly within the platform, making it easier to filter and identify critical roles during audit preparation.

**Related Settings:** 

- `ShowRoleCatalogAttribute9`

**Best Practices:** 

- Configure when detailed role categorization is needed beyond the default attributes.
- Avoid when additional role attributes are unnecessary, to keep the Role Catalog interface simplified.