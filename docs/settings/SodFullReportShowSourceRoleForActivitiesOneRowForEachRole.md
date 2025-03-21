# SoD Full Report Show Source Role For Activities One Row For Each Role

**Technical Name:** SodFullReportShowSourceRoleForActivitiesOneRowForEachRole

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:** 

This parameter controls the granularity of the Segregation of Duties (SoD) violations report, affecting how source roles tied to potentially conflicting activities are displayed. When enabled, the report generates one row for each role involved in SoD violations instead of aggregating them. This detailed view facilitates a more granular analysis of the roles causing the violations.

**Business Impact:**

Enabling this feature provides organizations with an enhanced capability to pinpoint and remediate specific roles responsible for SoD violations, thereby improving internal controls and regulatory compliance. It is particularly beneficial in environments where roles are closely managed, and precise accountability for SoD violations is required.

**Technical Impact: when configured**

Upon configuration, the SoD violations report will display each violation with distinct rows for every source role involved. This increases the report's length but significantly improves the granularity and usability of the report for audit and compliance purposes.

**Examples Scenario:**

An organization needs to identify specific roles that contribute to SoD violations within their financial systems. By enabling this parameter, their SoD report will list violations with individual rows for each role involved, making it easier for the compliance team to identify and take corrective action on each role, rather than deciphering aggregated roles.

**Related Settings:** 

- `SoDToEmployees`
- `matrix_SodViolations`

**Best Practices:** configure when detailed analysis and role-level accountability for SoD violations are required; avoid when a high-level overview is sufficient or when report performance and size are a concern.