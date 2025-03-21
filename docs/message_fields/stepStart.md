**Field Name:** stepStart

**Description:** The `stepStart` field represents the starting time of a specific step within a workflow process in Pathlock Cloud. It is a DateTime value captured at the initiation of a step and is used as a parameter in email templates to convey timing information related to the workflow steps.

**Usage Context:** This field is typically used when sending email notifications as part of the workflow process to provide details about when a particular step in the workflow was started. The `stepStart` field can be included in various email notifications for different workflow scenarios, aiding recipients to understand the timeline and state of the workflow action.

**Example:**

    Workflow step started at: $$stepStart$$

    After rendering:

    Workflow step started at:  
    2023-10-19T14:30:00Z
