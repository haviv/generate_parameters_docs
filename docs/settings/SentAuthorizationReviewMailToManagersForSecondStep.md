# Sent Authorization Review Mail To Managers For Second Step

**Technical Name:** SentAuthorizationReviewMailToManagersForSecondStep

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter controls whether an authorization review email is sent to managers during the second step of the certification process. It is part of the authorization certification workflow actions to ensure managers are notified and can take the necessary actions in the workflow approval process.

**Business Impact:** Enabling this parameter ensures that managers are promptly informed about pending approval requests, facilitating quicker response times and aiding in maintaining compliance with internal and external audit requirements.

**Technical Impact when configured:** Upon setting this parameter to true, it triggers the system to automatically send a notification email to managers when there is an item ready for their review and approval in the second step of the authorization certification process. This helps streamline the workflow by ensuring timely approvals and minimizes delays in the access certification lifecycle.

**Examples Scenario:** 

- In a scenario where a company has a policy that all user access requests must be reviewed by a manager before final approval, this parameter ensures that managers receive an email notification about the review request as soon as it reaches the second step in the certification process. This prompt notification can lead to quicker decision-making, affecting how fast employees can gain necessary access to perform their duties.

**Related Settings:** 

- SendWorkflowReminder
- SendWorkflowReminderEvery

**Best Practices:** 

- **Configure when:** You want to ensure managers are actively involved in the second step of the authorization review process by receiving direct email notifications for actions requiring their approval. This is especially useful in environments where prompt access decisions are crucial.
  
- **Avoid when:** If your organization’s workflow does not require manager intervention in the second step or if email notifications could lead to notification fatigue due to high volume, it may be beneficial to disable this setting to reduce unnecessary emails.