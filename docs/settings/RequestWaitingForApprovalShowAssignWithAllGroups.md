# Request Waiting For Approval Show Assign With All Groups

**Technical Name:** RequestWaitingForApprovalShowAssignWithAllGroups

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `RequestWaitingForApprovalShowAssignWithAllGroups` parameter controls whether users with workflow administration privileges can view and interact with all group assignments during the approval process of requests. This configuration affects the visibility and actions available in the workflow inbox and requests waiting for approval pages.

**Business Impact:**

Enabling this feature ensures that workflow administrators have the oversight and capability to manage requests across all groups, facilitating a more streamlined and comprehensive workflow management process. It aids in preventing potential bottlenecks and ensures that no request remains unattended due to group assignment limitations.

**Technical Impact when configured:**

When configured, this parameter enhances the workflow administration by:

- Allowing visibility of all group assignments in the workflow, broadening the scope of request management.
- Providing the capability to assign, approve, or decline requests across different groups, which contributes to a more efficient handling of workflows.
- Reducing the risk of delays in the approval process by ensuring that workflow administrators can intervene in any pending requests irrespective of the group assignment.

**Example Scenario:**

A workflow administrator needs to manage a surge in leave request approvals towards the end of the year. Many of these requests are assigned to different groups based on departmental structures. With `RequestWaitingForApprovalShowAssignWithAllGroups` enabled, the administrator can view and act on all these requests from a centralized interface, without the need to switch contexts or miss out on any request due to restricted group visibility.

**Related Settings:**

`DisableDeclineForInstanceSteps`, `DisableDeclineForWorkflowSteps`

**Best Practices:** configure when

- There is a need for comprehensive oversight and management of requests across multiple groups.
- Workflow administrators are tasked with managing high volumes of requests that may span across various departments or groups.

avoid when

- The organization prefers to maintain strict separation and visibility of requests based on group assignments without cross-group intervention by administrators.