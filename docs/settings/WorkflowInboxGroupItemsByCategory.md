# Workflow Inbox Group Items By Category

**Technical Name:** WorkflowInboxGroupItemsByCategory

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether items in the workflow inbox are grouped by their categories. When enabled, it organizes the workflow inbox items into distinct categories based on the type of workflow they belong to, enhancing the user’s ability to prioritize and manage tasks efficiently.

**Business Impact:**

Grouping items by category can significantly improve the management and oversight of various workflow items. It allows users to quickly identify and access workflows of a particular type, improving response times and overall efficiency in handling approvals, reviews, and other workflow actions.

**Technical Impact when configured:**

When enabled, this configuration affects how items are displayed in the Workflow Inbox, grouping them by their respective categories as defined in the workflow settings. This may impact load times and how users interact with their inboxes, potentially improving user experience by making navigation and task prioritization more intuitive.

**Examples Scenario:**

- **Approval Processes:** In an organization where multiple approval workflows are in place (e.g., for expense approvals, time-off requests, and access requests), enabling this setting will help approvers see all pending requests categorized, thus helping them to process similar requests in batches, improving efficiency.
- **Review Processes:** For reviews that occur on a periodic basis (e.g., document reviews, compliance checks), grouping items by category can streamline the review process by consolidating similar review items together.

**Related Settings:**

- WorkflowStep.CanMoveForwaredByAdmin
- WorkflowInstanceSteps.IsApproved

**Best Practices:** configure when you have a significant volume of workflow items and multiple categories of workflows to manage. Avoid when the workflow inbox typically contains a small number of items or when workflows don’t benefit from being categorized.