**Field Name:** requestType

**Description:** The `requestType` field represents the type of request being processed within a workflow. It helps categorize the nature of the workflow request, such as a general action, specific activity, or role assignment. This field is used to provide context about the workflow request in email notifications, ensuring recipients have a clear understanding of the action being taken or requested.

**Usage Context:** The `requestType` field is typically used in email templates that are part of the workflow process. It is included in notifications sent out to users, providing them with a short, descriptive label about the type of request being processed. This field is populated based on the transaction or role associated with the workflow request.

**Example:** 

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>