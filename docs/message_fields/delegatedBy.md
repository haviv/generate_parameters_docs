**Field Name:** delegatedBy

**Description:** The `delegatedBy` field indicates the individual who delegated a particular task or responsibility. This field is used to identify when an action within a workflow has been delegated to another user, and it provides the name or identification of the person who performed the delegation.

**Usage Context:** The `delegatedBy` field is typically used in email templates related to workflow processes, specifically those that involve delegation actions. It is included in email notifications to inform recipients about the original authority or approver who delegated the task to them as part of the workflow execution. This is often relevant in steps where tasks can be assigned or passed to other personnel for approval or action.

**Example:**

    Delegated by: $$delegatedBy$$

    After rendering:

    Delegated by: John Doe