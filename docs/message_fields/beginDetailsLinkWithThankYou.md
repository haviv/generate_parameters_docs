**Field Name:** beginDetailsLinkWithThankYou

**Description:** The `beginDetailsLinkWithThankYou` field represents a hyperlink that, when rendered in an email template, allows users to click and view details of a workflow instance step. This link is unique because it includes a "Thank You" acknowledgment as part of the URL, indicating that the user should be shown appreciation for reviewing the details.

**Usage Context:** This field is typically used in email templates sent during or after workflow processes, especially in contexts where it is important to acknowledge the user's contribution or action. It is used in situations where the email recipient is expected to review or interact with steps of a workflow, with an added note of thanks included in the interaction link.

**Example:**

    View details: $$beginDetailsLinkWithThankYou$$

    After rendering:

    View details:  
    <a href="https://cloud.pathlock.com/details?id=45321&thanks=1">View details with Thanks</a>