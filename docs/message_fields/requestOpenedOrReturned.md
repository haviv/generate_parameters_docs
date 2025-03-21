**Field Name:** requestOpenedOrReturned

**Description:** The `requestOpenedOrReturned` field is used within email templates to indicate the status of a workflow request. Specifically, it is intended to convey whether a request has been newly opened or has been returned in the course of a workflow process.

**Usage Context:** This field is typically used in email notifications sent to users involved in workflow processes. The specific context in which this field is employed includes scenarios where a request is either first initiated or returned to a previous step in the process. The field helps to inform the recipient of the current status of the request, which is crucial for tracking and managing tasks within a workflow.

**Example:** 

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>