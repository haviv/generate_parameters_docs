**Technical Name:** WorkflowReminderItemBullet

**Category:** Workflow

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The WorkflowReminderItemBullet parameter is utilized within the Pathlock Cloud GRC platform to control how reminders for workflow items are presented or formatted in notifications sent to users. This parameter particularly pertains to bullet or list formatting within reminder emails or messages, ensuring clear and structured communication.

**Business Impact:**

The configuration of this parameter directly impacts the clarity and effectiveness of reminder notifications sent to managers or users regarding pending workflow items. Well-formatted reminders can enhance the efficiency of workflow management by ensuring that pending tasks are clearly communicated and thus, can be acted upon more promptly. This can lead to improved compliance, timely execution of tasks, and better overall workflow management within an organization.

**Technical Impact when configured:**

When properly configured, the WorkflowReminderItemBullet parameter ensures that reminders for workflow actions such as review, approval, or certification tasks are clearly listed or bulleted in notifications. This can prevent misunderstandings and overlooked tasks by providing a visually organized reminder structure, making it easier for users to identify and act on pending items.

**Example Scenario:**

Consider a scenario where a manager is responsible for reviewing and approving various compliances and authorization certifications. If the WorkflowReminderItemBullet parameter is correctly utilized, the manager receives reminder emails with a well-structured list of pending approvals. This clarity allows for quicker action on pending items, reducing bottlenecks and improving the overall speed of compliance and authorization processes.

**Related Settings:**

- WorkflowInstance.CertificationProcessId
- WorkflowInstance.AuthorizationCertification.IsActive

**Best Practices:** 

- Configure when: You aim to enhance the clarity and effectiveness of workflow reminder notifications to ensure prompt action on pending tasks.
- Avoid when: If over-customization could lead to confusion or if the default notification structure meets the organization's needs without modification.