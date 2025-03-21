**Field Name:** stepTargetEndTime

**Description:** The `stepTargetEndTime` field represents the target end time for a step in a workflow process. It indicates when a particular step is expected to be automatically approved or concluded if it is not completed before this time.

**Usage Context:** This field is typically used in email templates related to workflow processes. It is relevant in contexts where the automatic transition or conclusion of a workflow step is involved, such as in emergency access reporting. It provides the recipients with information on the deadline by which a workflow step is expected to be automatically processed.

**Example:**

    Approve directly: $$stepTargetEndTime$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>