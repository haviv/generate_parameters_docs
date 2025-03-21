# Invalid Approver Text

**Technical Name:** InvalidApproverText

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

The Invalid Approver Text parameter is used within the workflow engine to manage communication and error handling when an approver within a given process does not have the necessary authority or accreditation to approve a step. This parameter ensures clear communication and redirection in the approval process, contributing to maintaining the integrity and security of process approvals in the Pathlock Cloud GRC platform.

**Business Impact:**

Improper handling or misidentification of approvers can lead to unauthorized access, process delays, and potential compliance risks. Configuring the Invalid Approver Text correctly ensures that workflow processes are streamlined, compliant, and secure by providing immediate feedback when an invalid approval attempt occurs, thereby mitigating risks associated with improper access control.

**Technical Impact when configured:**

- Enhances the clarity of workflow processes by notifying participants of invalid approvals.
- Prevents process stagnation by redirecting or informing invalid approvers promptly.
- Supports compliance with internal and external audit requirements by ensuring that only designated approvers can execute approval tasks.

**Examples Scenario:**

- In a workflow designed for emergency access approval, if an employee who lacks the necessary clearance tries to approve a request, the Invalid Approver Text parameter can trigger a notification advising them of their insufficient permissions and simultaneously alert a system administrator or a higher authority for further action.

**Related Settings:**
- WorkflowTypeForProcessVerification
- MinimumTimeDiffBetweenToUsesOfTheSameTransactionByTheSameUserInMinutes

**Best Practices:** 
- **Configure when:** setting up or updating workflow processes that involve several approval steps, especially in sensitive areas such as financial approvals, access rights management, or emergency actions.
- **Avoid when:** there is no clear hierarchy or delineation of approval authorities within the organization’s process framework, to prevent confusion or miscommunication.