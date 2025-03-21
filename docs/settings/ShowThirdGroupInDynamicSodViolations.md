# Show Third Group In Dynamic SoD Violations

**Technical Name:** ShowThirdGroupInDynamicSodViolations

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter `ShowThirdGroupInDynamicSodViolations` controls the visibility of a third grouping level in the Dynamic Segregation of Duties (SoD) Violations Report within the Pathlock Cloud GRC platform. Enabling this setting can provide additional context and granularity for identifying and resolving SoD violations.

**Business Impact:**

Utilizing this parameter allows organizations to enhance their security analysis by providing deeper insights into the context of SoD violations. This can lead to more informed decision-making regarding access control and compliance management, ultimately aiding in the mitigation of risks associated with improper access rights.

**Technical Impact when configured:**

When enabled, this parameter adds a third level of data grouping in the Dynamic SoD Violations reports, which can assist in detailed reviews and audits of SoD violations. This extra layer of detail supports comprehensive risk analysis and strengthens internal controls.

**Examples Scenario:**

For instance, in a situation where an organization needs to closely monitor and analyze SoD violations across various departments, the `ShowThirdGroupInDynamicSodViolations` parameter could be enabled to provide a third level of grouping by department or role. This would facilitate a more targeted approach in identifying and addressing SoD violations, enabling more effective compliance and risk management strategies.

**Related Settings:**

- `ScheduleMailWithReport`

**Best Practices:** configure when detailed analysis and reporting of SoD violations are necessary. Avoid when simpler reporting is sufficient to meet organizational needs.