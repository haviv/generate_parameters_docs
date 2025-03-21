**Field Name:** beginDetailsLink

**Description:** The `beginDetailsLink` field in an email template is used to insert a hyperlink for users to navigate to the detailed view of a specific workflow instance. When rendered, it generates a URL that directs the recipient to a webpage displaying all pertinent details of the workflow, allowing them to review the instance's information.

**Usage Context:** This field is typically used in email templates during the workflow communication process where providing access to detailed information is necessary. It is included in notifications where the user needs to view some aspects of the workflow to make informed decisions or to review progress.

**Example:**

    Details link: $$beginDetailsLink$$

    After rendering:

    Details link:  
    <a href="https://cloud.pathlock.com/details?id=29712">View Details</a>