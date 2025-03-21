# Request Waiting For Approval Hide Mass Approve

**Technical Name:** RequestWaitingForApprovalHideMassApprove

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of mass approval options for requests that are waiting for approval within the Pathlock Cloud GRC platform. When enabled, it hides mass approve functionality, requiring approvers to address each request individually.

**Business Impact:**

Enabling this parameter can enhance the oversight on the approval process by ensuring that each request is reviewed on its own merits. This can be particularly important in environments where compliance, auditability, and meticulous review of permissions or access rights are mandated.

**Technical Impact when configured:**

- Mass approval options for requests awaiting approval are not displayed.
- Reduces the risk of inadvertent approvals, enhancing security and compliance.
- Forces a more deliberate review process, potentially increasing the workload for approvers.

**Examples Scenario:**

In a scenario where an organization must adhere to strict compliance regulations regarding user access rights, the `RequestWaitingForApprovalHideMassApprove` parameter can be enabled to ensure that each request is individually reviewed and approved. This practice helps prevent unauthorized or unintended access rights from being granted as a result of bulk approvals, aligning with best practices for access control and compliance.

**Related Settings:**

- RequestWaitingForApprovalHideMassDecline

**Best Practices:** 

- Configure when: Stringent review of each request is required for compliance or security purposes.
- Avoid when: The volume of requests is high, and each request does not necessitate individual review, provided that doing so does not compromise compliance requirements.