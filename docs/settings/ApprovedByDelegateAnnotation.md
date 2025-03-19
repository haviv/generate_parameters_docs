# Approved By Delegate Annotation

**Technical Name:** ApprovedByDelegateAnnotation

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter determines whether a delegate or proxy has the necessary privileges to approve a request within a given workflow step. When configured, it checks if the action taken by a delegate meets the authorization requirements set for the workflow step.

**Business Impact:**

Enabling delegates to approve requests can streamline workflow processes by ensuring that tasks are not stalled due to the unavailability of the primary approver. However, it must be managed carefully to maintain the integrity of the approval process, avoiding unauthorized access or unintended approval escalations.

**Technical Impact when configured:**

When this parameter is set, the system will validate that the delegate acting on behalf of the primary approver has the appropriate permissions to approve the request. This helps in maintaining proper authorization controls within the workflow, making sure that only designated and authorized individuals can make approvals.

**Examples Scenario:**

- A primary approver is out of office, and a delegate needs to approve a critical workflow to ensure continuous operations. The `ApprovedByDelegateAnnotation` parameter allows this action, after checking the delegate's permissions, ensuring that business processes are not delayed.

**Related Settings:** 

- `EmergencyAccessRequestsEnabledForAnyone`

**Best Practices:** configure when a well-established delegation process is in place, avoid when there is no clear policy or controls around delegation of approval authority.