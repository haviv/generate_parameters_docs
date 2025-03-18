# Add Option To Allow Return To Previous For Parallel Steps

**Technical Name:** AddOptionToAllowReturnToPreviousForParallelSteps

**Category:** Workflow

**Default Value:** Not Applicable

**Impact Level:** Medium

**Description:**

This setting enables a workflow configuration where users can return to previous steps in parallel workflows. Specifically, it allows users in a decision-making position, such as approvers, the flexibility to revisit and potentially revise their decisions before the final execution of the workflow.

**Business Impact:**

Implementing this feature can significantly enhance the decision-making process in critical business operations by introducing a level of review and revision that was not previously possible. It supports thorough governance by allowing decision-makers to reconsider their actions, ensuring that all decisions are made with the greatest amount of available information and oversight.

**Technical Impact when configured:**

Once enabled, workflow processes that involve parallel steps will have the capability for users to move backwards to a previous step. This adds a layer of complexity to the workflow management, as the system must now handle the state management and data consistency across these reversible actions.

**Examples Scenario:**

An example scenario involves a multi-department approval process for financial expenditure. With this feature enabled, if an approver realizes additional information or context is needed after moving past their decision point, they can return to their previous decision step to re-evaluate their choice in light of new information.

**Related Settings:** Not Applicable

**Best Practices:** Configure this option in workflows where decisions have significant impact and may require revision. Avoid using in workflows where decisions are straightforward or do not benefit from revisitation to streamline the process and reduce complexity.