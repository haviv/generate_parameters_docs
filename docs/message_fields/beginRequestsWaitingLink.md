**Field Name:** beginRequestsWaitingLink

**Description:** This field serves as a placeholder for inserting a hyperlink in email templates. The hyperlink directs the workflow participant to a page where they can view all their pending requests awaiting approval. The link provides a convenient entry point for users to manage and track their workflow activities within the Pathlock Cloud platform.

**Usage Context:** The `beginRequestsWaitingLink` field is used in email templates sent during workflow processes, particularly in notifications related to request status updates. It's typically included in emails that inform users about action items waiting for their attention, such as tasks they need to approve as part of the workflow process.

**Example:** 

    Review pending requests: $$beginRequestsWaitingLink$$

    After rendering:

    Review pending requests:  
    <a href="https://cloud.pathlock.com/requests?id=currentUserId">Pending Requests</a>