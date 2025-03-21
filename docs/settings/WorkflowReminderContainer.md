**Workflow Reminder Container**

**Technical Name:** WorkflowReminderContainer

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Workflow Reminder Container parameter is designed to manage and configure the sending of reminder notifications within workflow processes. It specifies how reminders should be handled, who receives them, and under what conditions they should be sent out to ensure timely reviews and approvals in workflow tasks.

**Business Impact:**

Effectively using the Workflow Reminder Container can significantly reduce the time taken for workflows to complete by ensuring participants are reminded of pending actions. This leads to more efficient process management, decreased delays in task completion, and improved overall compliance and governance within the organization.

**Technical Impact when configured:**

When configured, this parameter enables the system to send automatic reminder emails to workflow managers or approval groups about active reviews that are not yet finished. This ensures that all stakeholders are aware of the pending tasks, leading to a more streamlined and efficient workflow process.

**Examples Scenario:**

Let's say a workflow for document approval is initiated but hasn't been completed because one of the approvers has not taken action. If the Workflow Reminder Container is properly configured, it will trigger a reminder email to the approver (or group of approvers) reminding them of the pending approval. This guarantees that tasks are not forgotten and are acted upon in a timely manner.

**Related Settings:**

- CommonSettings.Default.ReminderMailIfCampaignIsActiveAndMarkedComplete
- WorkflowReminderAuthoirizationCertificationFormat

**Best Practices:** 

- **Configure when:** You have workflows that require timely action from participants. Setting up reminders can significantly reduce bottlenecks caused by delayed responses.
  
- **Avoid when:** Workflows are short and generally completed in a timely manner without the need for reminders. Over-notifying users can lead to notification fatigue, decreasing the effectiveness of the reminders.