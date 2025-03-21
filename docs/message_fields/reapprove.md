**Field Name:** reapprove

**Description:** The `reapprove` field is a placeholder used in email templates to generate a link that enables users to reapprove a previously denied or modified request within a workflow. This link is essential for workflows where requests can be returned for reapproval due to changes or additional information.

**Usage Context:** The `reapprove` field is typically used in email templates for informing approvers when a request requires reapproval. This happens in scenarios where a request has been returned to a previous step in the workflow, and the original decision needs to be reassessed.

**Example:**

    Reapprove this request: $$reapprove$$

    After rendering:

    Reapprove this request:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=4">Reapprove</a>