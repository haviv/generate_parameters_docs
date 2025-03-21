# Workflow Mail Include Child Requests In Approval Flow

**Technical Name:** WorkflowMailIncludeChildRequestsInApprovalFlow

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

The `WorkflowMailIncludeChildRequestsInApprovalFlow` parameter determines whether emails generated as part of the workflow approval process should include information about child requests. This setting is relevant in environments where requests can have child requests that are also pending approval, and there's a need to aggregate and display this information in the notification emails sent to approvers.

**Business Impact:**

Including child requests in approval emails provides a holistic view of related requests, enabling approvers to make more informed decisions. It potentially speeds up the approval process by reducing the need for back-and-forth communication to clarify request details. This can be particularly impactful in complex project environments or when managing extensive sets of permissions and roles within Pathlock GRC.

**Technical Impact when configured:**

When enabled, the system generates more comprehensive workflow emails that include details of both the primary request and any associated child requests. This ensures approvers have complete visibility into all items that are pending approval, potentially related to the same project or permission set changes, directly from their inbox.

**Examples Scenario:**

An organization has implemented a multi-level permission request process where each request may have dependent child requests. Enabling `WorkflowMailIncludeChildRequestsInApprovalFlow` allows the approval email for the parent request to include information about these dependent requests, ensuring that the approver understands the full context and implications of the approval decision.

**Related Settings:**

- `EnableChangeManagement`

**Best Practices:** Configure this parameter to enhance the decision-making process for approvers by providing complete visibility into all associated requests, particularly in environments with complex approval hierarchies or dependencies. Avoid enabling this feature if email simplicity is preferred or if child requests typically do not influence the approver's decision.