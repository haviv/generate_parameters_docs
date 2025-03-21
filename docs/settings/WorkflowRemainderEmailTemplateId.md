# Workflow Reminder Email Template

**Technical Name:** WorkflowRemainderEmailTemplateId

**Category:** Workflow Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `WorkflowRemainderEmailTemplateId` is a parameter configured within the Pathlock Cloud GRC platform to identify the specific email template used for sending reminders related to workflow actions. This configuration is crucial for ensuring that the right communication is cascaded to users at various stages of the workflow process.

**Business Impact:**

Configuring the correct `WorkflowRemainderEmailTemplateId` impacts how users are notified about pending actions, deadlines, and approvals within the workflow. It ensures that reminders are clear, reflect the corporate branding and messaging standards, and contain the necessary information for users to take timely actions. This can significantly affect the efficiency of workflow processes, user compliance, and overall system governance.

**Technical Impact when configured:**

- Ensures that the appropriate email template is used for workflow reminders, enhancing communication clarity and effectiveness.
- Allows for customization and personalization of reminder emails, improving user engagement and response rates.
- Supports compliance and audit requirements by ensuring that notifications meet organizational and regulatory standards for communication.

**Example Scenario:**

A company has configured the Pathlock GRC platform to manage access requests and approvals for their ERP system. The `WorkflowRemainderEmailTemplateId` is set to utilize a custom email template designed for access request workflows. When a user's request for access remains pending approval beyond a specified period, the system sends a reminder email using the configured template to nudge the approver. This reminder includes the access request details, the urgency of the request based on the impact on business operations, and a direct link for the approver to review and act on the request.

**Related Settings:**

- WorkflowRoleUpdatesDisableRemoveCurrentRoles

**Best Practices:** 

- **Configure when:** You have a clear understanding of the workflow stages and the associated communication strategy. Use a template that reflects the necessary actions and provides clear instructions to the recipient.
- **Avoid when:** Default notifications suffice for your organizational needs, or if you have not developed a template that meets all communication requirements and compliance standards.