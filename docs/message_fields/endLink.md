**Field Name:** endLink

**Description:** The `endLink` field is used to denote the closure point of a hyperlink in email templates. It functions as a placeholder in templates that are formatted using a specific email template system within Pathlock Cloud. Once rendered, it typically translates to the closing anchor tag in HTML, completing an actionable link in the email content.

**Usage Context:** This field is typically used in email templates that are part of workflow processes where it's essential to provide recipients with direct, actionable links pertaining to their tasks or notifications. Common scenarios involve approving requests or accessing specific pages within the platform. This ensures that emails can include dynamic links directed towards specific recipients or actions.

**Example:**

    Link to Approver Page: $$beginApproveStepLink$$

    endLink

    After rendering:

    Link to Approver Page:  
    <a href="https://cloud.pathlock.com/approvedetail?id=45321">Here</a>