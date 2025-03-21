# Enable Simulation Of Role From Dev

**Technical Name:** EnableSimulationOfRoleFromDev

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This configuration parameter allows administrators to simulate role changes directly from the development environment before applying them to production. When enabled, it restricts certain UI panels related to role assignment and authorization object management, ensuring that simulation activities are isolated from production workflows.

**Business Impact:**

Enabling this feature can significantly reduce the risk associated with role modifications by providing a sandbox environment for testing. It ensures that any changes made to roles do not adversely affect user access or system security in the live environment, thus maintaining the integrity of access controls and compliance with security policies.

**Technical Impact when configured:**

- Disables visibility for Action to User, Role to User, Role to Employee, and Action to Role panels in the UI.
- Allows administrators to simulate the impact of role changes in a development or sandbox environment without affecting live user data or permissions.

**Examples Scenario:**

An organization wants to revise a role that grants access to sensitive financial reports. To ensure that the revision does not inadvertently revoke necessary access or extend excessive permissions, the administrator enables this feature to assess the impact of the changes in a controlled environment before rolling them out to the production users.

**Related Settings:**

- `EnableServiceNowOpenSubTicketForEachWorkflow`

**Best Practices:** 

- **Configure when**: Testing role changes or updates to ensure they do not disrupt user access or system security.
- **Avoid when**: Directly applying changes to production environments or in systems where role changes do not require prior testing.