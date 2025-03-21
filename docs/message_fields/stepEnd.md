**Field Name:** stepEnd

**Description:** The `stepEnd` field represents the date and time at which a specific workflow step is completed in the Pathlock Cloud workflow process. It is used to capture and display the completion time of an action or approval step within a workflow.

**Usage Context:** The `stepEnd` field is typically used in email templates that notify users about the completion of workflow steps. It provides recipients with a timestamp for when a particular step in the workflow process is finalized, thereby helping users track the progress and history of workflow actions. This is especially useful in contexts where a timestamp of completion is critical for auditing or tracking purposes, such as in compliance or certification processes.

**Example:**

    Completion Time: $$stepEnd$$

    After rendering:

    Completion Time:  
    2023-09-21 15:30:00