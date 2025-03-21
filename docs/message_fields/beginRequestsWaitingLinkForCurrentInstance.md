**Field Name:** beginRequestsWaitingLinkForCurrentInstance

**Description:** The `beginRequestsWaitingLinkForCurrentInstance` field is used to create a hyperlink in email templates that directs the recipient to a page where they can view all waiting requests for a specific workflow instance. This field helps in providing a direct access link to the relevant section of Pathlock Cloud where the waiting requests are listed.

**Usage Context:** This field is typically used in workflow-related email notifications when it's necessary to inform a user about pending requests awaiting their attention for a specific instance. It is primarily employed in scenarios related to process management and needs for immediate action or review by the recipient.

**Example:** 

    View all pending requests: $$beginRequestsWaitingLinkForCurrentInstance$$

    After rendering:

    View all pending requests:  
    <a href="https://cloud.pathlock.com/requests-waiting?id=12345">View Requests</a>