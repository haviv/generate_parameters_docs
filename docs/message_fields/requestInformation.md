**Field Name:** requestInformation

**Description:** The `requestInformation` field combines the type and relevant details of a user's workflow request. It's used to provide a concise description of the request within email templates. This field is part of a dictionary that holds various message parameters, forming part of the content in notification emails.

**Usage Context:** The `requestInformation` field is used in email templates associated with workflow steps in Pathlock Cloud. It captures a summary of the request, including its type (e.g., "Free Request", "Role", "Activity") and additional comments, enhancing the clarity of email communications concerning the workflow status.

**Example:**

    Request details: $$requestInformation$$

    After rendering:

    Request details:  
    Role - Administrator Access