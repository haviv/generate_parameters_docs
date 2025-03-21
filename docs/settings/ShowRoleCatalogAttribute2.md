# Show Role Catalog Attribute2

**Technical Name:** ShowRoleCatalogAttribute2

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

Enables or disables the visibility of the "Attribute2" data field within Role Catalog entries. This setting adjusts how detailed the role catalog display is, by determining whether a secondary, customizable attribute of roles is shown in the UI.

**Business Impact:**

Adjusting this parameter can affect how information is presented to users managing or auditing roles. This can streamline role management tasks, enhance the user interface by reducing clutter, or provide additional insights by displaying more role-related data as needed.

**Technical Impact when configured:**

When enabled, users can view the "Attribute2" field for each role within the Role Catalog, allowing for more detailed information to be accessible at a glance. If disabled, the system hides this attribute, simplifying the displayed information and potentially reducing the cognitive load on users during role review or assignment processes.

**Examples Scenario:**

- **Scenario 1:** An organization wants to simplify its role catalog view for users who are not part of the security or compliance teams. By disabling "ShowRoleCatalogAttribute2," they can ensure that the role catalog view is less cluttered, focusing only on the most critical attributes.
  
- **Scenario 2:** A compliance team needs to review roles with specific attributes related to regulatory compliance. Enabling "ShowRoleCatalogAttribute2" allows these details to be visible directly within the role catalog, facilitating quicker reviews and decisions.

**Related Settings:**

- ShowRoleCatalogAttribute1

**Best Practices:** 

- **Configure when:** there is a need to display additional role-related information that can aid in role categorization, identification, or compliance checks.
  
- **Avoid when:** the user interface should remain simple for better user experience, or when the additional attribute does not provide significant value to the intended audience.