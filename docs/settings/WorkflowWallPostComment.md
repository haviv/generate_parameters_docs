# Workflow Wall Post Comment

**Technical Name:** WorkflowWallPostComment

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `WorkflowWallPostComment` parameter is used within the Pathlock Cloud GRC platform to manage comments on workflow wall posts. This parameter is crucial for keeping track of communication and decisions made during the workflow approval process. 

**Business Impact:**

Enabling clear and effective communication among approvers and participants in the workflow process ensures that each decision is made with full awareness and context. This can significantly impact the efficiency and transparency of approval processes, directly influencing the organization's ability to manage risk, compliance, and governance policies effectively.

**Technical Impact when configured:**

Configuring the `WorkflowWallPostComment` influences how notifications and comments are managed and displayed to the recipients during the workflow process. Proper configuration ensures that the relevant stakeholders are informed and can contribute effectively to the process, improving decision-making and accountability.

**Examples Scenario:**

- **Scenario:** An organization utilizes the Workflow Wall Post Comment feature to facilitate the discussion around access request approvals. The requester can add additional context to their request, and approvers can ask clarifying questions or explain their decisions directly within the workflow.
  
  **Benefit:** This streamlined communication reduces the time taken to approve requests and improves the auditability of decisions made during the workflow process.

**Related Settings:**

- `SendMailOnWorkflowApproved`
- `SendMailOnWorkflowDeclined`
- `SendMailOnWorkflowStarted`
- `RunSoDCheck`

**Best Practices:** configure when

- There is a need for enhanced communication between approvers and the requester within a workflow.
- Audit trails of comments and decisions are required for compliance purposes.

avoid when

- The workflow process is meant to be automated without the need for manual comments or interventions.
- The organization prefers to use external communication tools outside of the Pathlock platform for workflow discussions.