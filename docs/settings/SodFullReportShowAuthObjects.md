# SoD Full Report Show Auth Objects

**Technical Name:** SodFullReportShowAuthObjects

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:**

The parameter `SodFullReportShowAuthObjects` controls the inclusion of authorization objects in the Separation of Duties (SoD) full report. When enabled, this setting allows the report to display detailed authorization objects associated with SoD violations, providing deeper insight into the specific permissions or access rights that contribute to the violation.

**Business Impact:**

Enabling this parameter enhances the understanding of SoD violations by showcasing the underlying authorization objects that trigger these violations. This detailed visibility is crucial for auditors and compliance managers to pinpoint and address security risks, ensuring that appropriate access controls are in place and regulatory compliance is maintained.

**Technical Impact when configured:**

When configured, reports will include a comprehensive breakdown of authorization objects (e.g., transaction codes, system privileges) related to each SoD violation, facilitating targeted remediation efforts and improved audit trails.

**Examples Scenario:**

A company's internal audit team is conducting a routine security review and utilizes the SoD full report to identify potential violations. By having the `SodFullReportShowAuthObjects` parameter enabled, the report reveals that a significant SoD violation was caused by overlapping transaction codes granted to a user in the finance department. With this information, the team can take specific actions to segregate duties appropriately and mitigate the identified risk.

**Related Settings:**

N/A

**Best Practices:** Configure when conducting detailed security audits and compliance reviews to ensure comprehensive visibility into SoD violations and their root causes. Avoid when superficial reporting is sufficient or to reduce report complexity for non-technical stakeholders.