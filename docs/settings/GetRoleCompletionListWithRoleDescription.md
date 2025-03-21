# Get Role Completion List With Role Description

**Technical Name:** GetRoleCompletionListWithRoleDescription

**Category:** User Management

**Default Value:** Not applicable

**Impact Level:** Medium

**Description:**

This parameter controls the functionality for auto-suggesting roles along with their descriptions in user interfaces where roles can be assigned or modified. It is primarily used to enhance user experience by providing more context when selecting roles in the system.

**Business Impact:**

Improving the role selection process by including descriptions can significantly enhance the accuracy of role assignments, reduce the risk of incorrect role attribution, and save time during user setup or modification processes. It directly impacts the efficiency of managing access rights and permissions, thus contributing to overall security and compliance postures.

**Technical Impact: when configured **

When enabled, the system will perform additional queries to fetch and display role descriptions alongside the role names in auto-complete or drop-down lists in the user interface. This could potentially increase database access load but is designed to provide a balance between usability and performance.

**Examples Scenario:**

A system administrator wants to assign roles to new users imported into the Pathlock Cloud GRC platform. Instead of navigating away from the assignment screen to look up role specifics, the admin directly sees a list populated with both role names and their descriptions, simplifying the decision-making process.

**Related Settings:**

- AuthorizationDescription: Might be used in conjunction with this parameter to standardize the descriptions across different settings.

**Best Practices:** Configure this parameter in environments where role management is frequent, and accurate role assignments are critical. Avoid or carefully manage in scenarios where database performance is a concern due to the possibly increased load from fetching descriptions.