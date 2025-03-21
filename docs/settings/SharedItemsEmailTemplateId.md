# Shared Items Email Template

**Technical Name:** SharedItemsEmailTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** Identifies the specific email template to be utilized when sending notifications related to shared items within workflows.

**Business Impact:** Ensures that communications regarding workflow steps that have been approved or comments within a workflow are consistently formatted and contain the necessary information. This contributes to streamlined operations and enhances the clarity of communications within business processes.

**Technical Impact when configured:** Controls the formatting and content of emails sent for approved steps and workflow comments. Proper configuration of this parameter ensures that notifications are clear, contain all required information, and are presented in a manner consistent with organizational standards.

**Examples Scenario:** When a workflow step is approved, an email is generated and sent to the requester. The SharedItemsEmailTemplateId determines the template used for this email, ensuring it includes specific information pertinent to the approval and any necessary subsequent actions.

**Related Settings:**

- InformRequesterStepApprovedEmailTemplateId
- WorkflowCommentsEmailTemplateId

**Best Practices:** Configure when a customized communication is necessary for workflow-related notifications to meet business requirements and maintain a professional standard of communication. Avoid when default settings are sufficient for organizational needs and no customization is required.