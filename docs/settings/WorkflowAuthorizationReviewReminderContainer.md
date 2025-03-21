# Workflow Authorization Review Reminder Container

**Technical Name:** WorkflowAuthorizationReviewReminderContainer

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** The Workflow Authorization Review Reminder Container parameter is responsible for managing email notifications sent as reminders for ongoing workflow authorization reviews. This parameter plays a crucial role in ensuring that workflow managers and participants are reminded of pending reviews, fostering timely action and decision-making to maintain workflow efficiency and compliance.

**Business Impact:** Timely completion of authorization reviews is critical to maintaining security and compliance within organizational processes. Delays in review completion can lead to bottlenecks in workflow progression, increased risk exposure, and potential non-compliance with regulatory requirements. This parameter helps mitigate such risks by automating the reminder process, ensuring individuals involved in the workflow are aware of outstanding tasks that require their attention.

**Technical Impact when configured:** When configured, this parameter triggers the sending of reminder emails to managers or designated approvers involved in a workflow authorization review. This ensures that all participants are alerted about pending reviews, potentially speeding up the workflow process and aiding in the maintenance of a streamlined operation.

**Example Scenario:** A user part of a workflow authorization review process has not completed their review task within the expected timeframe. The Workflow Authorization Review Reminder Container parameter is configured to send reminders every 24 hours after the initial deadline has passed. As a result, the user receives a reminder email the next day, prompting them to complete their review task, thereby avoiding delays in the workflow.

**Related Settings:**
- WorkflowReminderItemBullet
- WorkflowReminderAuthoirizationCertificationFormat

**Best Practices:** configure when reminders are necessary to maintain workflow progress and compliance, avoid when continuous reminders could lead to notification fatigue among participants.