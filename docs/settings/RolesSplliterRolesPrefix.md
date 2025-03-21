# Roles Splitter Roles Prefix

**Technical Name:** RolesSplliterRolesPrefix

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** Medium

**Description:** A configuration parameter utilized within the Pathlock GRC platform to format and generate unique role names, primarily by appending a counter to child role names to ensure uniqueness across the system.

**Business Impact:** Ensures that roles within the system remain unique, aiding in the clear identification and assignment of permissions without confusion. This is crucial in environments where role-based access controls are complex and granular, such as in large ERP systems like SAP.

**Technical Impact when configured:** Dynamically generates unique role identifiers by attaching a numeric suffix to the base role name, ensuring that even similar or templated roles can be distinguished from one another, thus preventing role name collisions and aiding in smoother role provisioning and management workflows.

**Examples Scenario:** In an ERP system where multiple child roles derive from a parent role with similar baseline permissions but slight variations, `RolesSplliterRolesPrefix` ensures each child role is assigned a unique identifier by appending a numeric suffix, facilitating easy tracking and assignment.

**Related Settings:** N/A

**Best Practices:** Configure when deploying in environments with complex role hierarchies and numerous child roles to prevent role name collisions. Avoid when the environment has simple, non-repetitive role naming conventions where the likelihood of name collision is minimal.