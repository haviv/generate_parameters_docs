**Field Name:** requestId

**Description:** The `requestId` field represents the unique identifier of the workflow instance. It is used in email templates to reference specific requests within the Pathlock Cloud system. This field helps recipients and workflow participants identify and track specific workflow requests in email communications.

**Usage Context:** The `requestId` field is typically used in email templates related to workflow processes. It appears in emails to indicate the ID of a particular request that is pending approval, has been approved, denied, or requires some action within a workflow.

**Example:**

    Approve directly: $$requestId$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/request?id=12345">Request Details</a>