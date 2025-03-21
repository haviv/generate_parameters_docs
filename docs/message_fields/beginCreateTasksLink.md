**Field Name:** beginCreateTasksLink

**Description:** The `beginCreateTasksLink` field represents the starting HTML anchor tag for linking to the tasks associated with a specific workflow step in Pathlock Cloud. Its purpose is to provide recipients with direct access to the task page for creating or managing tasks related to the current workflow step within an email template.

**Usage Context:** This field is typically used in email templates that are part of Pathlock Cloud's workflow process notifications. It is particularly relevant when an email notification is sent out to inform a user or administrator about tasks that need to be created or managed for a given workflow instance. The field dynamically generates a link, which is injected into the email, allowing recipients to easily navigate to pertinent task information within the Pathlock Cloud platform.

**Example:**

    Create tasks directly: $$beginCreateTasksLink$$

    After rendering:
    
    Create tasks directly: 
    <a href='https://cloud.pathlock.com/Portal/WorkflowName/InstanceGuid/OpenTasks.aspx'>