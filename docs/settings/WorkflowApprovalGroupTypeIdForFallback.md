# Workflow Approval Group Type Id For Fallback

**Technical Name:** WorkflowApprovalGroupTypeIdForFallback

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The WorkflowApprovalGroupTypeIdForFallback parameter is designed to specify the default group type identifier to which workflow approval requests are rerouted in scenarios where the primary approval process encounters issues or is otherwise unavailable. This parameter ensures that workflow requests remain in motion, preventing process delays due to unavailable approvers.

**Business Impact:**

Setting the WorkflowApprovalGroupTypeIdForFallback parameter correctly ensures that critical approval workflows, such as permissions requests, compliance approvals, or any other governance-related processes, do not grind to a halt. This keeps business operations running smoothly and maintains compliance by ensuring that all necessary approvals are obtained, even in fallback scenarios.

**Technical Impact when configured:**

When configured, this parameter reroutes approval requests to a predefined fallback group, identified by the group type ID, if the original approvers are not available. This ensures continuity in the approval process, reducing the risk of delays in workflow progression.

**Examples Scenario:**

For instance, if the designated approver for a critical compliance approval process is out of office and unavailable, the WorkflowApprovalGroupTypeIdForFallback parameter ensures that the request is automatically rerouted to a designated fallback group, such as a compliance management team, thereby ensuring that the request is reviewed and actioned in a timely manner.

**Related Settings:**

- WorkflowManager
- WorkflowInstanceStep

**Best Practices:** Configure the WorkflowApprovalGroupTypeIdForFallback parameter for all critical approval workflows to ensure there are no bottlenecks in the workflow process. Avoid using this setting for non-critical workflows where delays in approval do not have a significant business impact.