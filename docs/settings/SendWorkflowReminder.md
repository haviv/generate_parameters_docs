# Send Workflow Reminder

**Technical Name:** SendWorkflowReminder

**Category:** Workflow

**Default Value:** None

**Impact Level:** Medium

**Description:**

The SendWorkflowReminder parameter is used to initiate the sending of reminder notifications for workflow steps that have not been completed within a specified time frame. This ensures timely action on workflows essential for managing security, risk, compliance, and other GRC-related activities within the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling reminders for workflow steps significantly impacts ensuring tasks are completed on time, thus maintaining compliance and adhering to internal and external regulations and policies. It helps prevent bottlenecks in workflows, facilitating smoother operation and better governance, risk, and compliance management.

**Technical Impact when configured:**

When configured, SendWorkflowReminder triggers reminder notifications for pending workflow steps. This ensures that responsible personnel are alerted to take necessary action, contributing to efficient process flow and compliance management.

**Examples Scenario:**

A compliance workflow requiring multiple approvals is pending due to one uncompleted step. The SendWorkflowReminder parameter ensures a reminder is sent to the approver(s), prompting them to complete their review and approval, thus moving the process forward without unnecessary delays.

**Related Settings:**

- CommonSettings.Default.SystemWideSystemId
- CommonSettings.Default.ProductKeyExperisionWarningDays

**Best Practices:** 

- **configure when**: It's crucial to configure SendWorkflowReminder in workflows that are critical to compliance and operational efficiency, where timely actions are necessary.
  
- **avoid when**: It is advisable to avoid setting reminders for workflows where tasks do not have strict completion timelines, to reduce notification fatigue among users.