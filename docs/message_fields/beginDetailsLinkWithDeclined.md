**Field Name:** beginDetailsLinkWithDeclined

**Description:** The `beginDetailsLinkWithDeclined` field is used to produce a hyperlink in an email template which directs the recipient to a page detailing a request that has been declined within a workflow process. This link provides additional context or necessary information regarding the declined request, utilizing unique identifiers to ensure a secure and direct path specific to the user's session.

**Usage Context:** This field is typically used in email templates that are triggered during workflow processes, specifically those related to notifications about declined requests. The link assists recipients in quickly accessing detailed information about the decline decision, streamlining communication and follow-up actions related to the workflow.

**Example:**

    Decline details: $$beginDetailsLinkWithDeclined$$

    After rendering:

    Decline details:  
    <a href="https://cloud.pathlock.com/request/details?id=45321&Decision=0&WaitingRequests=0&p2=user123&p3=hashvalue">View Decline Details</a>