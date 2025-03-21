# Sap Connector Is Remove All Roles Supported

**Technical Name:** SapConnectorIsRemoveAllRolesSupported

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

This setting determines whether the SAP Connector supports the functionality to remove all roles from users in bulk. When enabled, it allows for a more streamlined approach to managing user roles within an SAP environment, providing administrators with the capability to efficiently revoke all assigned roles from a user or a group of users at once. 

**Business Impact:**

Enabling this feature significantly impacts the administration of user roles within SAP, enhancing security by allowing rapid response to compliance requirements or security threats. It facilitates easier user role management and cleanup, especially beneficial in scenarios requiring quick revocation of access rights across the board.

**Technical Impact when configured:**

When configured, this parameter allows administrative actions within the Pathlock platform that directly interacts with SAP systems to bulk remove user roles. This can lead to a substantial decrease in the time and effort required for role management and compliance activities.

**Examples Scenario:**

- **Auditing and Compliance:** In the scenario where a compliance audit identifies several users with access rights no longer necessary for their current role, the administrator can quickly revoke all roles from these users to ensure compliance.
  
- **Security Incident:** In the event of a security breach or when a user's credentials are compromised, the administrator can immediately remove all roles assigned to the suspicious account, effectively mitigating potential threats.

**Related Settings:** 

- `UserManagementBulkActions`: Enables bulk actions for user management tasks.
- `SAPRoleRevocationProcess`: Defines the process for revoking SAP roles from users.

**Best Practices:** configure when -

- You have a large user base within your SAP environment, and need to streamline the process of role management.
- Compliance requirements dictate frequent review and adjustment of user roles and access.
  
avoid when -

- Your organization's SAP environment is small, or role assignments do not frequently change, as the risk of inadvertently removing all roles may outweigh the benefits.