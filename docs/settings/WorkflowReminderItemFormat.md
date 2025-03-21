# Workflow Reminder Item Format

**Technical Name:** WorkflowReminderItemFormat

**Category:** Workflow

**Default Value:** Not explicitly mentioned in the code references. Defaults are typically determined by system configuration or initial setup.

**Impact Level:** Medium

**Description:**

Specifies the format used for items within workflow reminders. This parameter determines the structure and presentation of reminder items sent to users as part of workflow actions, ensuring that essential details are communicated effectively and in a consistent manner.

**Business Impact:**

Proper configuration of the WorkflowReminderItemFormat is crucial for maintaining clear communication with users involved in a workflow. It directly influences the efficiency of workflow progression by affecting how reminders are perceived and acted upon by the recipients. The clarity and relevance of the format can reduce delays in workflow steps, enhancing overall process efficiency.

**Technical Impact when configured:**

When configured, the WorkflowReminderItemFormat governs how information related to pending workflow instances is formatted and displayed in reminder notifications. This could include steps awaiting action, summaries of open requests, or reminders about certification processes. A well-defined format ensures that users receive coherent and actionable reminders, which in turn can lead to more timely responses and actions within the workflow.

**Examples Scenario:**

An organization has implemented a multi-step approval process for access requests within the Pathlock Cloud GRC platform. To ensure timely processing, the system sends out daily reminders to managers with pending requests awaiting their approval. By configuring the WorkflowReminderItemFormat, the reminders can be structured to highlight critical information such as the requester’s name, request date, and action required, thereby enabling managers to quickly identify and act on pending requests.

**Related Settings:**

- CommonSettings.Default.WorkflowReminderContainer
- SendMailOnStepStarted
- SendMailOnWorkflowApproved
- SendMailOnWorkflowDeclined

**Best Practices:** 

Configure when establishing or refining workflow processes to ensure reminders are clear, informative, and aligned with the organization’s operational standards. 

Avoid when there is inadequate understanding of the workflow’s information requirements, as poorly configured reminder formats can lead to confusion or oversight.