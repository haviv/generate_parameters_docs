# Show Role Owners In Role Query

**Technical Name:** ShowRoleOwnersInRoleQuery

**Category:** Reporting

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

This parameter controls whether the owners of roles are displayed in the roles query results within the Pathlock Cloud GRC platform. Enabling this setting can provide additional context in reports by associating roles with their respective owners, enhancing visibility into role management and ownership.

**Business Impact:**

Including role owners in reporting can aid in accountability and transparency within an organization's GRC processes. It enables users to quickly identify who is responsible for specific roles, facilitating easier communication and management of access permissions. This is particularly useful in audits, where understanding role ownership is crucial.

**Technical Impact: when configured**

Enabling this setting will modify the output of roles reports by adding a column or detail that identifies the owner of each role. It can affect the performance of report generation due to the additional lookup or join that may be required to retrieve the owner information.

**Examples Scenario:**

- **Audit Preparation:** An organization preparing for an audit can enable this parameter to include role owners in their roles report. This helps auditors easily verify that each role is assigned a responsible owner and cross-reference with compliance requirements.
  
- **Security Review:** During a routine security review, security teams can utilize reports generated with this parameter to ensure that roles are not orphaned and that all roles have a designated owner, aligning with best practices for access control.

**Related Settings:** 

- RoleSearch:Search
- ShowRoleAdvancedFilter

**Best Practices:** configure when role accountability and transparency are required within reports. Avoid when the addition of role owner information to reports is unnecessary or could introduce performance issues.