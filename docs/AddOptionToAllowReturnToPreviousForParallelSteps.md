# Add Option To Allow Return To Previous For Parallel Steps

**Technical Name:** AddOptionToAllowReturnToPreviousForParallelSteps

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:** This parameter enables or disables the ability for users to return to previous steps in parallel workflows within the Pathlock Cloud GRC platform. When set to `True`, users can navigate back to a previous step in a workflow to review or modify their inputs or decisions before final submission. 

**Business Impact:** Allowing users to return to previous steps in parallel workflows can significantly improve the decision-making process by ensuring that all decisions are made with the most accurate and up-to-date information. This capability can reduce errors and rework, leading to a more efficient process and better overall compliance and risk management.

**Technical Impact when configured:** When enabled, this feature impacts the workflow engine by introducing potential revisits to earlier workflow steps, which may affect process time and resource consumption. System administrators should consider the complexity and length of the workflows when configuring this option to prevent potential delays or performance issues.

**Examples Scenario:** In a scenario where a user is part of a parallel approval process for a high-value transaction, enabling this feature allows the user to revisit their approval decision after reviewing new compliance reports or risk assessments provided by another user in a different parallel step. This ensures that decisions are made with the most comprehensive information available, enhancing the company's risk management practices.

**Related Settings:** N/A

**Applicable Workflows Actions:** 
- Approve
- Decline

**Best Practices:** 
- Configure when workflows involve complex decisions requiring inputs from multiple sources or when there is a high chance of receiving new information after the initial decision has been made.
- Avoid when workflows are straightforward or when revisiting decisions could cause significant delays in process completion.

**Context:** The `AddOptionToAllowReturnToPreviousForParallelSteps` parameter is crucial for businesses looking to enhance their governance, risk, and compliance (GRC) strategies by enabling more flexible and thorough decision-making processes in their workflows.