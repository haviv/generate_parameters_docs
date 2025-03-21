# Impact Analysis Show Controls Selection

**Technical Name:** ImpactAnalysisShowControlsSelection

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter determines whether selection controls for impact analysis are shown to the user during workflow processes. It enables or disables the visibility of specific controls related to the assessment of risk impact in various steps of a workflow.

**Business Impact:**

Enabling this setting enhances the granularity of risk analysis by allowing users to select or unselect controls as part of their impact assessment. This can lead to more accurate risk management decisions, ensuring that only relevant risks are addressed, reducing unnecessary workload and focusing efforts efficiently.

**Technical Impact when configured:**

When enabled, users will see additional options to include or exclude controls in their risk impact analysis during workflow processes. This facilitates a more detailed and tailored approach to risk management within the Pathlock GRC platform.

**Examples Scenario:**

1. **Risk Assessment Workflows:** In a situation where an organization wants to streamline their risk assessment process by including only the most relevant controls, enabling this parameter would allow assessors to select exactly which controls to consider for a given risk analysis.
   
2. **Compliance Reviews:** During compliance review processes, enabling this parameter can help compliance officers focus on controls that are pertinent to specific regulations, ignoring others that may not apply, thus making the review process more efficient.

**Related Settings:** 

- `WorkflowRisk_UseRiskTag`: This setting might influence which controls are available for selection when the Impact Analysis Show Controls Selection parameter is enabled, by filtering controls based on associated risk tags.

**Best Practices:** 

- **Configure when:** Detailed, control-specific risk impact analysis is necessary for your organization's workflow processes, and you need the ability to tailor controls selection on a per-analysis basis.
  
- **Avoid when:** Your organization's risk management process is streamlined and does not require the selection of individual controls, or if the added decision points may unnecessarily complicate or prolong the workflow.