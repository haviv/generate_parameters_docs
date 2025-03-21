**Send Workflow Reminder On Days**

**Technical Name:** SendWorkflowReminderOnDays

**Category:** Workflow

**Default Value:** Not provided in the code references

**Impact Level:** Medium

**Description:**

This parameter controls the scheduling of workflow reminders, determining on which days these reminders should be sent to the respective users involved in the workflow process. It ensures timely notifications for pending actions or tasks within the Pathlock GRC platform.

**Business Impact:**

Setting up this parameter optimally ensures that all stakeholders in the GRC process remain informed about their pending tasks, leading to more efficient process completion and adherence to compliance requirements. It helps in reducing the risk of missed deadlines and enhances the overall governance, risk management, and compliance posture of the organization.

**Technical Impact when configured:**

When configured, this parameter triggers the `SendDailyMailWorkerProcess` to send out workflow reminders based on the conditions defined by the setting. It directly influences the frequency and timing of reminder notifications sent to users about their involvement in various compliance, risk, and security workflows.

**Example Scenario:**

For instance, if `SendWorkflowReminderOnDays` is set to remind users every 3 days, users involved in any pending workflow tasks will receive reminder notifications every third day until the task is completed. This ensures critical compliance tasks are not overlooked and are completed in a timely manner.

**Related Settings:**

- `ApprovalGroupTypeForAuthorizationReviewFromExcel`
- `ChangeDocumentsReadChildRecords`

**Best Practices:** 

- **Configure when:** you want to ensure that workflow tasks are completed on time by reminding the stakeholders at regular intervals. This is crucial for time-sensitive compliance and audit tasks.
  
- **Avoid when:** frequent reminders might lead to notification fatigue among users, or for tasks where deadlines are not critical.
