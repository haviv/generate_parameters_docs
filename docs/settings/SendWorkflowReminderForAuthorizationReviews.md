# Send Workflow Reminder For Authorization Reviews

**Technical Name:** SendWorkflowReminderForAuthorizationReviews

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Send Workflow Reminder for Authorization Reviews parameter triggers reminder notifications for ongoing or pending authorization review processes in workflows where an authorization step has not been completed. These reminders are essential for ensuring timely responses from approvers or participants in the authorization reviews.

**Business Impact:**

Timely reminders contribute significantly to maintaining compliance and oversight in authorization processes. Delays in authorization can lead to operational inefficiencies, increased risk of non-compliance with internal and external policies, and could potentially expose the organization to security vulnerabilities due to unauthorized access.

**Technical Impact when configured:**

When configured, this feature actively monitors authorization steps within workflows for any delays or inactions. It sends out reminders to the responsible parties, prompting them to take the necessary action to move the process forward. This ensures that authorization reviews are conducted within the expected timelines, aiding in the timely management of access rights and compliance measures.

**Examples Scenario:**

A company uses Pathlock Cloud GRC platform to automate their user access review process. The Send Workflow Reminder For Authorization Reviews parameter is configured to send reminders if an authorization review has not been actioned within a week. As a result, when an authorization review step is pending, the designated approver receives an automatic reminder email, prompting them to complete the review. This helps in preventing undue delays in the access review cycle, ensuring regulatory compliance and minimizing potential security risks.

**Related Settings:**

- ConnectUsersToEmployee_ByEmail
- SoCheckUserSoDByEmployeeAuthorizations

**Applicable Workflows Actions:** 

**Best Practices:** 

- Configure when: Timely reminders are critical for keeping authorization reviews on track, especially in environments with strict compliance requirements.
  
- Avoid when: If the workflow process is very short or the organization has a policy against excessive notifications, which might lead to notification fatigue among users.