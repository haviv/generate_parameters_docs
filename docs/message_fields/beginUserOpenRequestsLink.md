**Field Name:** beginUserOpenRequestsLink

**Description:** The `beginUserOpenRequestsLink` field serves as a placeholder in email templates, which is replaced by a hyperlink directing users to a page listing their open requests within the Pathlock Cloud platform.

**Usage Context:** This field is utilized in email templates associated with workflow processes. It is generally included in notifications to allow users easy access to view and manage their pending or active requests.

**Example:**

    View your open requests: $$beginUserOpenRequestsLink$$

    After rendering:

    View your open requests:  
    <a href="https://cloud.pathlock.com/openrequests">Open Requests</a>