# Enable SoD For Object Level Only Roles For Complete System Ids

**Technical Name:** EnableSoDForObjectLevelOnlyRolesForCompleteSystemIds

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

The parameter 'EnableSoDForObjectLevelOnlyRolesForCompleteSystemIds' is designed to control the enforcement of Segregation of Duties (SoD) checks at an object level, specifically for roles that are designated as "object level only" within complete system IDs. When activated, this parameter ensures a granular level of SoD compliance by focusing on the permissions attributed to individual roles rather than assessing them at a broader, system-wide level.

**Business Impact:**

Activating this setting could have significant implications for organizations looking to enforce rigorous SoD policies within their GRC (Governance, Risk Management, and Compliance) framework. By enabling this feature, companies can mitigate risk by ensuring that roles granting access at the object level do not inadvertently provide users with conflicting permissions, thereby preserving the integrity of the organization's internal controls and compliance posture.

**Technical Impact when configured:**

When configured, this parameter enforces a refined level of SoD checks, isolating the analysis to roles with permissions defined at the object level for specific system IDs. This targeted approach empowers administrators and auditors to identify and rectify potential SoD violations more efficiently, by homing in on the precise areas where risks are most acute.

**Examples Scenario:**

Consider an organization that uses SAP as its ERP system. Within this system, various roles are assigned to users to execute different business processes. If 'EnableSoDForObjectLevelOnlyRolesForCompleteSystemIds' is enabled, the system would perform SoD checks specifically for roles that have "object level only" permissions—such as roles granting access to financial transactions at a granular level—ensuring that a user does not possess multiple roles that could lead to a breach of SoD policies.

**Related Settings:**

- UseSapProfilesAsRolesReadContent
- CustomUserGroupIdForExcludedUsersFromUsageLogs

**Best Practices:** configure when the organization requires strict adherence to SoD policies at a granular level, particularly in environments with complex permissions structures. Avoid when broad, system-wide SoD checks suffice for compliance needs or when the detailed level of scrutiny could unnecessarily complicate role management and system performance.