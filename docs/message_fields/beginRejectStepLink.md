**Field Name:** beginRejectStepLink

**Description:** The `beginRejectStepLink` field is used in email templates within the Pathlock Cloud platform to insert a hyperlink that allows users to reject a step in a workflow process. This field is part of the mechanism for handling workflow step approvals and rejections. When rendered, it provides an actionable link that a recipient can click to directly execute a rejection action on the corresponding workflow instance step.

**Usage Context:** This field is typically used in workflow-related email notifications that require user interaction to reject a workflow step. It's included in emails aimed at managers or other stakeholders who can either approve or reject requests within the workflow. The link is dynamically generated based on the current context of the workflow step and allows for immediate interaction directly from the email.

**Example:**

    Reject Request: $$beginRejectStepLink$$

    After rendering:

    Reject Request: 
    <a href="https://cloud.pathlock.com/approve?id=45321&action=2">Reject</a>