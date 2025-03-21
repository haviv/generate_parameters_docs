# Notify Approver Workflow Declined Template

**Technical Name:** NotifyApproverWorkflowDeclinedTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The NotifyApproverWorkflowDeclinedTemplate parameter is utilized by the Pathlock Cloud GRC platform within the workflow mail system. It refers to the specific email template ID used to notify approvers when a workflow has been declined. Configuring this template allows for customized communication, ensuring that approvers are promptly and accurately informed about the status of workflows they're involved in.

**Business Impact:**

Setting this parameter with an appropriate template ID can significantly enhance the workflow's accountability and transparency. By providing clear notifications, businesses can better manage task assignments, review processes, and overall compliance monitoring, thereby reducing bottlenecks and improving operational efficiency.

**Technical Impact when configured:**

Once configured, the specified email template is triggered automatically upon the decline of a workflow action. This affects how and when approvers receive notifications, potentially speeding up resolution times for pending tasks and maintaining smooth process flows across departments.

**Examples Scenario:**

An approver declines a request for access to sensitive financial data due to insufficient documentation. The NotifyApproverWorkflowDeclinedTemplate parameter ensures that a well-crafted email is sent to the requester, detailing the reason for declination and guiding them on the next steps, like providing additional documents or clarifications, to expedite the approval process.

**Related Settings:**

- MailServerSettings.Default.FromMail
- MailServerSettings.Default.SmtpClientHost

**Best Practices:** configure when,

- You aim to streamline communication and improve awareness among workflow participants about the status of their requests or tasks.
  
avoid when,

- The default notification settings suffice for your organization’s workflow communication needs. Customizing templates without a clear strategy can lead to confusion or information overload for approvers.