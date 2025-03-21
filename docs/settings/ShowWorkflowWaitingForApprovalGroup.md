# Show Workflow Waiting For Approval Group

**Technical Name:** ShowWorkflowWaitingForApprovalGroup

**Category:** Workflow

**Default Value:** 0

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the "Handled By" column in workflow approval processes, indicating which user or group the workflow is currently awaiting approval from.

**Business Impact:**

Enabling this feature provides clear visibility into the approval process, aiding in the identification of potential bottlenecks or delays in the workflow. It facilitates smoother operations and enhances accountability within the workflow management process.

**Technical Impact when configured:**

When enabled, the "Handled By" column will be visible, showing the user or group responsible for the next action in the workflow. This adjustment allows for better tracking and management of workflow instances.

**Examples Scenario:**

- **Scenario:** An organization wants to improve its tracking of approval workflows to identify where requests are getting held up. By enabling the ShowWorkflowWaitingForApprovalGroup parameter, they can see at a glance which user or group an approval request is waiting on, thereby identifying any patterns of delay or bottleneck.
  
**Related Settings:**

- ReportRunTimeOutInSeconds

**Best Practices:** Configure this parameter to improve transparency and accountability in the workflow process, especially in complex environments with multiple approval stages. Avoid enabling it in scenarios where workflow process visibility is not essential or could lead to privacy concerns.