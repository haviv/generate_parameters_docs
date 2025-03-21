**Field Name:** beginDetailsLinkWithThankYouGeneral

**Description:** This field represents a placeholder in email templates used to generate a link to the details of a workflow request. It appends a query string to include identifying information of the email recipient for personalized tracking. The link is meant to be a general link format commonly used in "Thank You" scenarios after user actions.

**Usage Context:** This field is typically utilized in scenarios where the email template requires a link pointing to details of a related workflow request. The link includes a personalized aspect, identifying the recipient in contexts where a user might be expecting a confirmation or follow-up, such as after completing a specific action within a workflow process.

**Example:** 
  
    View Details: $$beginDetailsLinkWithThankYouGeneral$$

    After rendering:

    View Details:  
    <a href="https://cloud.pathlock.com/workflowdetails?guid=abc123&action=thankyou&user=xyz">View Details</a>