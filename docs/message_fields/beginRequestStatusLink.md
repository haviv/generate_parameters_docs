**Field Name:** beginRequestStatusLink

**Description:** The field `beginRequestStatusLink` is a placeholder used in email templates to insert a hyperlink. This link directs the user to a webpage where they can view the status of a specific workflow request. It is used to provide users with a direct and convenient way to access request status information within workflow-related email notifications.

**Usage Context:** This field is typically used in email templates that notify users about actions taken on their workflow requests, such as approvals, rejections, or when a request has been received. It's particularly used to enhance communication in workflow processes by providing direct access to detailed request status.

**Example:**

    Check request status: $$beginRequestStatusLink$$

    After rendering:

    Check request status:  
    <a href="https://cloud.pathlock.com/requestStatus?id=45321&p2=&p3=">Request Status</a>