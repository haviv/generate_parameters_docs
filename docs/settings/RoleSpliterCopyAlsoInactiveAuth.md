# Role Splitter Copy Also Inactive Auth

**Technical Name:** RoleSpliterCopyAlsoInactiveAuth

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls whether the role splitter functionality within the Pathlock Cloud GRC platform should also copy inactive authorizations when duplicating roles. In the context of SAP connector operations, it specifically dictates if the copying process should include authorizations that are not currently active for a user role.

**Business Impact:**

Setting this parameter affects how comprehensive the role duplication process is concerning inactive authorizations. When enabled, it ensures that all aspects of the original role, including those authorizations that are inactive at the time of copying, are replicated. This can be crucial for maintaining a complete history or preparing for future activations without redoing the permissions setup.

**Technical Impact when configured:**

If configured to include inactive authorizations, the system will carry over all permissions from the original role to the new one, regardless of their active status. This could lead to a more extensive permissions set in the newly created role, requiring additional review to ensure compliance and security standards are met.

**Examples Scenario:**

- **Preparation for Audit Reviews:** An organization may decide to copy roles including inactive authorizations before an audit to prepare for potential questions about historical permissions or to quickly reactivate certain permissions if needed without going through the setup process again.
  
- **System Upgrade Preparation:** Before a system upgrade, an admin may duplicate roles to test new features or changes without affecting the current setup, ensuring that even permissions not currently in use are available for testing.

**Related Settings:** 

- `RoleReDesginMode`

**Best Practices:** configure when planning major system updates or pre-audit preparations to ensure a comprehensive role setup is available. Avoid when simple role duplication is needed without the overhead of managing inactive authorizations to streamline role management and reduce complexity.