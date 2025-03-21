**Field Name:** comment

**Description:** The `comment` field is used to insert specific messages or notes associated with a workflow instance in email templates. These comments are typically user-generated inputs or notes entered during workflow steps and are intended to provide context or additional information relevant to the workflow process.

**Usage Context:** This field is typically used in email notifications related to workflows to convey user comments or important notes that were provided during a workflow step. It is commonly included in messages that inform users or administrators about the ongoing status or details of a workflow process, such as when a request is received, awaiting approval, or completed.

**Example:**

    User Comment: $$comment$$

    After rendering:

    User Comment: The request requires additional documents before approval.