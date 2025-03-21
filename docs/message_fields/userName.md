**Field Name:** userName

**Description:** The `userName` field represents the full name of the user associated with a particular workflow instance. It is inserted into email templates to personalize messages by identifying the recipient or subject of the workflow action.

**Usage Context:** This field is typically used in email templates related to workflow processes, such as notifications for approval requests, request statuses, and other workflow actions. It helps identify the user for whom the workflow action is relevant, ensuring the email communication is clear and personalized.

**Example:**

    Hi $$userName$$, your request is being processed.

    After rendering:

    Hi John Doe, your request is being processed.