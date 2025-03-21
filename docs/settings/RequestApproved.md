# Request Approved

**Technical Name:** RequestApproved

**Category:** Workflow

**Default Value:** None

**Impact Level:** High

**Description:**

The `RequestApproved` parameter is a key setting within the Pathlock Cloud GRC platform that plays a significant role in managing the approval processes of various workflows. This setting determines whether a request within a workflow has been approved or not, impacting the progression or rejection of said request based on predefined criteria or conditions.

**Business Impact:**

Enabling `RequestApproved` ensures that only authorized and validated requests proceed through the workflow, enhancing both security and compliance by enforcing a controlled review and approval process. It prevents unauthorized actions, mitigates risks associated with unapproved changes, and ensures that organizational policies and regulatory requirements are met.

**Technical Impact when configured:**

When `RequestApproved` is configured, the system either allows the progression of a request to subsequent stages of a workflow or halts it, based on the approval status. It ensures that each critical step in a workflow meets the organization's approval criteria before proceeding, thereby enforcing accountability and traceability.

**Examples Scenario:**

- In a user access review workflow, `RequestApproved` is used to either grant or deny user access requests. Only requests that have been marked as approved are processed for access provisioning.
  
- For change management workflows, `RequestApproved` dictates whether changes to critical system configurations are applied or rejected. This ensures that all changes are reviewed and approved by authorized personnel before implementation.

**Related Settings:**

- `DisableUserNameSelection`
- `WorkflowApprovalGroup`
- `EnableChooseRequestType`

**Best Practices:** 

- **Configure when:** there is a need to strictly enforce approval processes within workflows to ensure compliance and security policies are adhered to. This is particularly important in sensitive areas such as financial transactions, user access control, and critical system changes.
  
- **Avoid when:** workflows are meant to be completely automated without human intervention. In such scenarios, requiring manual approvals could introduce unnecessary delays.