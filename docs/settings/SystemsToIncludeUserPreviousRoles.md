# Systems To Include User Previous Roles

**Technical Name:** SystemsToIncludeUserPreviousRoles

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:** Determines whether a user's previous roles should be included in their role selections for certain workflows.

**Business Impact:** Enabling this setting can ensure that historical data isn't lost during user transitions, role revocations, or system updates. It helps in maintaining a comprehensive view of a user's role history, which is critical for audits, compliance tracking, and user management strategies.

**Technical Impact when configured:** When enabled, the system will include the roles previously assigned to the user when copying roles across systems or during role selection processes. This contributes to a more detailed and nuanced role management process, preventing the accidental omission of roles that could be relevant for the user's past or future tasks.

**Examples Scenario:** When a user is being considered for a role that requires a similar set of permissions as they had in the past, administrators can ensure that all relevant previous roles are considered and potentially re-assigned, making the process faster and more efficient.

**Related Settings:** ExcludeEmptyActivityModes

**Best Practices:** Configure this setting to true in scenarios where understanding a user's complete role history is crucial for security or compliance. Avoid enabling this setting if the organization prefers to manage roles based solely on current needs and contexts, without considering historical data.