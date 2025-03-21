# Notify Approver Workflow Approved Template

**Technical Name:** NotifyApproverWorkflowApprovedTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `NotifyApproverWorkflowApprovedTemplateId` parameter is used to specify the template ID for the notification email sent to approvers once a workflow has been approved. This helps in customizing the communication sent to approvers, ensuring clarity and consistency in workflow management notifications.

**Business Impact:**

Proper configuration of this parameter ensures that approvers are promptly and correctly informed about the approval of workflows, facilitating smoother operational processes and enhancing the efficiency of decision-making within the platform's governance, risk management, and compliance (GRC) functions.

**Technical Impact when configured:**

- Enhances the clarity of communication by allowing customization of the approval notification emails sent to approvers.
- Supports operational efficiency by ensuring approvers are well-informed of workflow approvals, enabling them to take necessary subsequent actions without delay.
- Aids in the standardization of email notifications related to workflow approvals, contributing to a more structured workflow management process.

**Example Scenario:**

An organization implements a new process requiring managerial approval for access to certain sensitive systems. By configuring the `NotifyApproverWorkflowApprovedTemplateId` parameter, the GRC team can customize the notification message sent to managers, informing them when their approval is needed and once it has been successfully processed, including specific information relevant to the access request.

**Related Settings:**

- `MailServerSettings.Default.FromMail`
- `MailServerSettings.Default.SmtpClient`

**Best Practices:** 

- **Configure when:** You need to standardize and customize the notification messages sent to approvers upon workflow approval to enhance clarity and consistency in communication.
- **Avoid when:** Default notification settings suffice for your organizational workflow management and communication requirements.