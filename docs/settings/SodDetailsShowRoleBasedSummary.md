# SoD Details Show Role Based Summary

**Technical Name:** SodDetailsShowRoleBasedSummary

**Category:** SOD

**Default Value:** False

**Impact Level:** High

**Description:** This parameter controls whether to display a summary based on roles within the segregation of duties (SoD) details section. When enabled, it allows for an aggregated view of SoD conflicts by role, rather than an individual transaction or action, facilitating a clearer understanding of systemic risk within role configurations.

**Business Impact:** Enabling this feature can significantly enhance an organization's ability to audit and review SoD conflicts at a higher level, making it easier to identify and address systemic issues rather than focusing solely on granular, transaction-level conflicts. This approach supports more strategic decision-making in the management of roles and permissions, improving overall security and compliance posture.

**Technical Impact when configured:** When configured to true, the system aggregates SoD conflicts by roles and displays them in the SoD Combination Element section. This summary view helps administrators and auditors to quickly understand which roles contribute most to SoD conflicts, streamlining the audit process and facilitating more efficient resolution of compliance issues.

**Examples Scenario:** Consider an organization that utilizes multiple roles within its Pathlock GRC platform, where certain roles have overlapping access rights leading to SoD conflicts. By enabling the SoD Details Show Role Based Summary, the compliance officer can easily review a broad summary of how each role contributes to SoD conflicts, identify high-risk roles, and prioritize remediation efforts accordingly.

**Related Settings:** 

- `ShowSystemNameForRole`
- `ShowGridForRoles`

**Best Practices:** Configure when auditing role-based access controls and addressing systemic SoD issues. Avoid when detailed, transaction-level review of SoD conflicts is necessary, as this setting provides a summarized view that may omit granular details.