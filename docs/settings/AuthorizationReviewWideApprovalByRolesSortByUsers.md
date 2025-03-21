# Authorization Review Wide Approval By Roles Sort By Users

**Technical Name:** AuthorizationReviewWideApprovalByRolesSortByUsers

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures whether the authorization review process will sort approval tasks by users within roles. When enabled, it affects how approval tasks are aggregated and displayed during the review process, potentially streamlining the approval workflow by grouping approvals by user, thus providing a clearer overview for those involved in the review process.

**Business Impact:**

Facilitates a more efficient review process by enabling approvers to focus on user-centric approval tasks. This can lead to faster decision-making and a reduction in the time to complete the authorization review process, positively impacting compliance deadlines and operational efficiency.

**Technical Impact when configured:**

Configuration of this parameter can lead to changes in how approval tasks are visualized and managed in the workflow, affecting the user experience for approvers by potentially reducing the complexity and duration of the approval process.

**Examples Scenario:**

In an organization undergoing a compliance audit, configuring this parameter to sort approval tasks by users ensures that an approver assigned to multiple roles sees a consolidated list of approval tasks organized by user, not scattered throughout the process. This can significantly speed up the review process by enabling approvers to focus on completing all approvals for a single user before moving on to the next, ensuring a more organized and efficient workflow.

**Related Settings:**

- StepExtensionMaxRequests
- StepExtensionFailed

**Best Practices:** configure when the review process involves multiple roles and users, and there is a need to streamline the approval workflow for efficiency. Avoid configuring this setting in simpler approval processes where it might introduce unnecessary complexity.