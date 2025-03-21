**Role Selection Hide Master For Derive Roles With Single Child**

**Technical Name:** RoleSelectionHideMasterForDeriveRolesWithSingleChild

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of master roles in workflows where roles are derived with only a single child role. When enabled, the master role is hidden, showing only its child roles for selection. This simplification can help streamline the role selection process within specific workflows.

**Business Impact:**

Enabling this feature can significantly streamline the user experience during the role selection process in workflows by reducing confusion and simplifying choices. This is particularly relevant in scenarios where derived roles effectively replace their master role, making the master role redundant in the selection process.

**Technical Impact when configured:**

When this parameter is configured to true, the system alters the default behavior by hiding master roles in the user interface of workflows where a master role has only one child role. This can affect how users perceive and interact with role selections, especially in complex role hierarchies.

**Examples Scenario:**

A company has implemented a hierarchical role model where each master role may have one or several derived child roles. In cases where a master role has only a single child role, enabling this setting would hide the master role in applicable workflows, presenting only the child role for selection to the end user, thus making the role selection process more straightforward.

**Related Settings:** None specific to the parameter were identified based on code references.

**Applicable Workflows Actions:** RemoveRolesListElementExcludeRolesFromOtherElement

**Best Practices:** 

- Configure this parameter to true in environments where role hierarchies are deeply nested, and there are frequent cases of master roles with a single derived child role, to simplify the role selection process.
  
- Avoid enabling this setting in scenarios where the visibility of master roles, regardless of their child roles, is critical for security, audit, or compliance reasons.