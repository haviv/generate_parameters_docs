# Comment For Approved After Step Finished

**Technical Name:** CommentForApprovedAfterStepFinished

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to capture comments once an approval step within a workflow is completed in the Pathlock Cloud GRC platform. It enables the recording of additional information or feedback from the approver upon the successful granting of an approval, ensuring a more detailed audit trail and accountability within the approval process.

**Business Impact:**

Incorporating comments upon approval completion enhances transparency and provides insights into the decision-making process. It aids in auditing and compliance by documenting the rationale behind approvals, which is essential for internal and external audits. This practice reinforces accountability among approvers and contributes to a better understanding of the workflow decisions.

**Technical Impact when configured:**

When configured, the CommentForApprovedAfterStepFinished parameter enforces the collection of comments after an approver has completed an approval step. This ensures that each approval within the workflow is accompanied by a justification, thereby increasing the auditability of decisions and actions taken within the Pathlock Cloud GRC environment.

**Examples Scenario:**

- **Approval of Access Request:** An IT administrator approves a request for additional privileges to a sensitive system. Using this parameter, the administrator provides comments on why the request was approved, including considerations such as the requester's role compatibility and the absence of conflict with existing policies.

**Related Settings:**

- **WorkflowFormFieldTitleWidth**
- **NewUsernameForbiddenCharacters**

**Best Practices:** configure when actionable insights and accountability are required in the workflow approval process; avoid when approvals are straightforward or do not require justification.