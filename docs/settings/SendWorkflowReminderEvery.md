# Send Workflow Reminder Every

**Technical Name:** SendWorkflowReminderEvery

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `SendWorkflowReminderEvery` parameter is designed to control the frequency of workflow reminders for steps that require attention or action. It ensures that users are regularly prompted to complete workflow steps, facilitating smoother and more efficient workflow progression.

**Business Impact:**

Implementing this parameter can significantly reduce the time taken for workflows to be completed by reminding users to take necessary actions on pending items. It helps in maintaining continuous progress in tasks, which is crucial for time-sensitive workflows. This is especially important in governance, risk management, and compliance (GRC) contexts, where delays can result in non-compliance issues, security breaches, or unmitigated risks.

**Technical Impact when configured:**

When configured, `SendWorkflowReminderEvery` actively checks each workflow step to determine if a reminder needs to be sent based on the start of the step and the configured reminder frequency. If a reminder is due, it triggers the sending process for only those steps that meet the criteria, thereby ensuring that users receive timely reminders without being overwhelmed by unnecessary notifications.

**Examples Scenario:**

A user might be part of a workflow where they are required to review access rights assigned to new employees within the organization. If the `SendWorkflowReminderEvery` parameter is set to remind every 2 days, the user will receive reminders every 2 days for each step in the workflow that hasn't been completed. This ensures that the task of reviewing and approving access rights is conducted in a timely manner, maintaining security and compliance standards within the organization.

**Related Settings:** Not provided based on the given references.

**Best Practices:** configure when

- There are critical workflows that require timely attention and completion.
- Users have a track record of overlooking or delaying certain workflow steps which could lead to compliance issues or operational delays.

avoid when

- Workflows are non-critical and can afford flexibility in completion time without significant consequences.
- Users are already receiving too many notifications, to avoid desensitization to reminders that might lead to ignoring important reminders.