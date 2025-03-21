# Workflow Links Target

**Technical Name:** WorkflowLinksTarget

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `WorkflowLinksTarget` parameter controls the target context in which workflow-related links are opened. This can influence how users interact with workflow tasks, approvals, and notifications within the Pathlock Cloud GRC platform.

**Business Impact:**

Adjusting the `WorkflowLinksTarget` parameter can streamline the process of reviewing and approving requests by adjusting where links within the workflow are opened. This can lead to more efficient navigation and task management, directly impacting the speed and efficiency of decision-making processes.

**Technical Impact when configured:**

When configured, the parameter alters the default behavior of clicking on workflow-related links, possibly opening them in a new tab, window, or in the existing window. This modification can aid in optimizing user work patterns and focus, reducing the risk of disorientation and improving task completion rates.

**Example Scenario:**

- A user is in the workflow inbox and clicks on a link to review a detailed request. Depending on the configuration of `WorkflowLinksTarget`, this request detail can open in a new tab, allowing the user to review without navigating away from the inbox, thereby streamlining the review process.

**Related Settings:**

- WorkflowDebugMode
- EnableDigitalSignForWorkflow
- InvalidApproverText

**Best Practices:** configure when you need to streamline workflow task management or improve navigation efficiency; avoid when users are accustomed to the default link behavior to prevent confusion.