**Field Name:** previousApprover

**Description:** The `previousApprover` field represents the user or group that was responsible for handling the last step in a workflow process before the current one. It is used to provide context about who previously managed the request, allowing recipients of the email to understand who last handled the approval.

**Usage Context:** The `previousApprover` field is typically used in email templates sent during workflow processes, especially when a step in the workflow is reverted or moved back, and users need to know who previously managed the request. It provides transparency and continuity by indicating the last handling authority when notifications are sent out about workflow updates.

**Example:**

    Approver Information: $$previousApprover$$

    After rendering:

    Approver Information: John Doe