# Use Default Workflow Mail Templates

**Technical Name:** UseDefaultWorkflowMailTemplates

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `UseDefaultWorkflowMailTemplates` parameter controls whether a workflow uses the platform's default email templates for notifications or allows for custom email message templates defined within individual workflow steps. 

**Business Impact:**

Using the default workflow mail templates ensures a standardized communication format across all workflow notifications, promoting consistency in message delivery and branding. Customization, on the other hand, allows for targeting specific information needs or tones suited to particular steps or processes within the workflow.

**Technical Impact when configured:**

Enabling this setting applies the default mail templates for all workflow notifications, impacting how users receive and perceive workflow-related communications. Any predefined customizations in email templates at the workflow step level will be overridden by the default template specified in the platform settings.

**Examples Scenario:**

- **Scenario 1:** A company wants to ensure all approval request emails have a uniform appearance and information structure to avoid confusion amongst approvers. They would enable `UseDefaultWorkflowMailTemplates` to use the platform's standard email template for all workflow notifications.
  
- **Scenario 2:** In a situation where a specific workflow requires detailed instructions or legal disclaimers sent out with every notification, the company might choose to disable `UseDefaultWorkflowMailTemplates` for that workflow, allowing for customized messaging tailored to the workflow's requirements.

**Related Settings:** 

- `EscalationEmailTemplatePostFix`: Defines the naming convention for escalation templates that can be targeted by the workflow manager when escalation is needed.

**Best Practices:** 

- **Configure when:** Uniformity in workflow communication is necessary across the board, or when the default templates meet all communication requirements for simplicity and efficiency.
  
- **Avoid when:** Specific workflows require tailored communication that differs significantly from the standard template, needing customization to include additional details, branding, or tone adjustments.