# Roles Spllitter Roles Child Role Objects Only Role Flag

**Technical Name:** RolesSplliterRolesChildRoleObjectsOnlyRoleFlag

**Category:** Configuration

**Default Value:** S

**Impact Level:** Medium

**Description:**

This parameter specifically controls how child roles are identified and handled during role splitting operations. When enabled, the system focuses on processing child roles based exclusively on role objects, ensuring a more targeted and efficient role split.

**Business Impact:**

Optimizing this setting can significantly improve system performance during role split operations by reducing unnecessary processing. It helps in maintaining a streamlined and effective role management process, making it easier for administrators to manage roles within the Pathlock GRC platform.

**Technical Impact: when configured**

When configured, this flag ensures that only those roles that are directly associated with specific role objects are considered during the role split process. This can lead to a more precise role hierarchy and efficient access control management, minimizing potential security risks and enhancing compliance with organizational policies.

**Examples Scenario:**

- When a large organization needs to restructure its role model due to changes in compliance requirements, ensuring that only relevant child roles are considered during the split can save time and reduce errors.
- In cases where role bloat has become a problem, using this parameter can help simplify roles based solely on the required role objects, enhancing system performance and user access clarity.

**Related Settings:**

- RolesSplliterRolesChildRoleSingleRoleFlag

**Best Practices:** 

- Configure when performing role splits in large systems with extensive role hierarchies to improve performance and accuracy.
- Avoid when every role, regardless of its object associations, needs to be reviewed or modified during a split, as it may exclude relevant roles from the process.