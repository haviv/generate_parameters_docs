# Request Waiting For Approval Show Step Name In Requested Object

**Technical Name:** RequestWaitingForApprovalShowStepNameInRequestedObject

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether the step name of a workflow action awaiting approval is displayed in the details of the requested item on the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature enhances the transparency and traceability of the approval process by providing approvers with clear context about the stage at which the request is currently pending. This could potentially expedite decision-making processes and improve audit trails by making the approval workflows more transparent.

**Technical Impact when configured:**

When enabled, it appends the step name in the display text for requests that are waiting for approval, thereby offering additional details to the approver directly within the request information itself.

**Examples Scenario:**

- In a typical approval process for access rights within an IT department, an administrator who oversees the approval process might need to understand at which stage of the approval workflow the request is stalled. Enabling this parameter allows the admin to see not just the request but also what approval step the request is awaiting, thus facilitating more informed decision-making.

**Related Settings:**

- None

**Best Practices:** configure when transparency in the approval process is needed, avoid when unnecessary to minimize information overload.