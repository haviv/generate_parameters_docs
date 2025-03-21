# Workflow Actions Notifier Worker Process Open On

**Technical Name:** WorkflowActionsNotifierWorkerProcess_OpenOn

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to control the activation or triggering of workflow-related notifications in the Pathlock Cloud GRC platform. It primarily pertains to the configuration within the Workflow User Interface (UI) settings, determining how and when email notifications related to workflow actions are dispatched to users.

**Business Impact:**

Configuring this parameter optimizes the communication flow for workflow actions, ensuring timely updates are sent. It plays a crucial role in facilitating the efficiency of workflow management by notifying the relevant parties about pending actions or updates, which directly impacts the organization's compliance and risk management processes.

**Technical Impact when configured:**

Once set, this parameter activates the process responsible for sending out notifications related to workflow actions. It ensures that users are informed of required actions in their workflow tasks, enabling faster decision-making and action completion.

**Examples Scenario:**

A user sets the `WorkflowActionsNotifierWorkerProcess_OpenOn` parameter to enable notifications for a specific type of workflow action. Consequently, whenever this workflow action is initiated, all relevant users receive an email detailing the action required, including any relevant workflow instance IDs and usernames associated with the task. This ensures all stakeholders are promptly informed and can take necessary action without delay.

**Related Settings:**

- `WorkflowActionIncludeWorkflowTypeInDetailsMail`

**Best Practices:** 

configure when:
- There is a need to improve the responsiveness of users to workflow tasks.
- The organization aims to enhance its compliance and risk management processes through better communication.

avoid when:
- The organization prefers not to send out automated notifications for workflow actions.
- Users experience notification fatigue, and critical actions might be overlooked.