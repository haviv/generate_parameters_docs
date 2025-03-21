# Enable Collapse Composite Roles View

**Technical Name:** EnableCollapseCompositeRolesView

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls whether the composite roles are displayed in a collapsed view by default in the roles management interface.

**Business Impact:** Enabling this view helps in managing large numbers of composite roles by reducing the overall complexity and improving readability, making it easier for administrators to navigate and manage roles efficiently.

**Technical Impact when configured:** When enabled, this setting collapses the view of composite roles in the management interface, simplifying the display of roles and potentially improving load times and user experience for administrators.

**Examples Scenario:** In an organization where there are hundreds of composite roles, navigating and managing these roles becomes cumbersome. By enabling the collapse view, administrators can more easily find and manage specific roles, leading to a more efficient administration process.

**Related Settings:** No specific related settings found in the provided code references.

**Best Practices:** Configure this setting to "True" in environments with a large number of composite roles to improve manageability. Avoid enabling this in environments where the depth and hierarchy of composite roles need to be visible at all times for compliance or management reasons.