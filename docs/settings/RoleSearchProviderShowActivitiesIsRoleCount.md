# Role Search Provider Show Activities Is Role Count

**Technical Name:** RoleSearchProviderShowActivitiesIsRoleCount

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:** Controls whether the Role Search Provider includes a count of activities within each role in the search results.

**Business Impact:** Enhancing the visibility of how many activities each role encompasses can aid in assessing the complexity and scope of roles within the organization. This can support better planning and auditing of roles for compliance and security management.

**Technical Impact when configured:** Enabling this feature can potentially impact the performance of role search operations due to the additional computation required to count activities per role.

**Examples Scenario:** When an auditor wishes to review roles within the system to ensure they are properly defined and not overly permissive, enabling this setting could provide a quick overview of roles with an unusually high number of activities, which may indicate overly broad access rights.

**Related Settings:** Not applicable based on provided code references.

**Best Practices:** Configure when an in-depth analysis of roles is necessary, particularly in complex environments with many granular activities. Avoid when performance is a concern or if activity counts per role are not relevant to your organization's GRC objectives.