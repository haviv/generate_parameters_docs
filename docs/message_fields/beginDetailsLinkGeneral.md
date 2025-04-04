**Field Name:** beginDetailsLinkGeneral

**Description:** The `beginDetailsLinkGeneral` field is used to insert a hyperlink in email templates that directs the recipient to the general details page of a specific workflow request. This field is typically used to enable email recipients to access more information about a workflow instance.

**Usage Context:** This field is used in email notifications sent during various stages of workflow processes in Pathlock Cloud. The link generated by this field allows workflow participants to review details pertaining to the workflow instance, helping them make informed decisions or take necessary actions.

**Example:**

    View details: $$beginDetailsLinkGeneral$$

    After rendering:

    View details: 
    <a href="https://cloud.pathlock.com/details?id=12345&p2=emailRecipientId&p3=hashValue">Details</a>