# Impact Analysis Show Controls From Combination Only

**Technical Name:** ImpactAnalysisShowControlsFromCombinationOnly

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This setting controls the visibility of specific workflow controls based on the assessment of risks associated with forbidden combinations of roles or permissions. When enabled, only the controls relevant to identified risky combinations are displayed, streamlining the user experience and focusing attention on critical concerns.

**Business Impact:**

Enabling this parameter ensures that risk management processes are more focused and efficient. By highlighting only the controls relevant to the combinations deemed risky, organizations can prioritize their remediation efforts, reduce the potential for oversight, and enhance overall compliance and security postures.

**Technical Impact when configured:**

Upon configuration, this parameter affects the user interface by hiding or displaying controls in the workflow associated with risk analysis. It dynamically adjusts the visibility of elements based on the presence of forbidden combinations, thus directly influencing the ease and effectiveness of risk management tasks performed by users.

**Examples Scenario:**

Consider a scenario where an organization has identified certain combinations of roles in their ERP system that pose a high risk for segregation of duties (SOD) violations. Upon configuring this parameter, only the controls related to these combinations are displayed to the user performing the impact analysis. This targeted approach helps the user to quickly understand which areas require immediate attention, enhancing the efficiency of risk mitigation processes.

**Related Settings:**

- `ForbiddenCombinationId`

**Best Practices:** configure when

- You have a well-defined list of risky combinations of roles or permissions.
- Your organization requires tight control and oversight over segregation of duties (SOD) violations.
- You aim to streamline the risk analysis process by focusing on high-priority issues.

avoid when

- The list of risky combinations is not defined, which could lead to confusion due to the absence of relevant controls.
- The organization's risk management process is more exploratory in nature and requires visibility into all available controls for a thorough assessment.