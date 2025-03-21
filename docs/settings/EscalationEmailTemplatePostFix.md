# Escalation Email Template Post Fix

**Technical Name:** EscalationEmailTemplatePostFix

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Escalation Email Template Post Fix parameter is used to define a specific postfix that is appended to the email template name used in workflow escalations. This allows for the customization of escalation emails depending on the workflow step or type, providing flexibility in how notifications are communicated to users or managers during the approval process.

**Business Impact:**

Customizing escalation emails with a postfix allows for more targeted communication during the workflow process, ensuring that the recipient receives all necessary information relevant to the action required from them. This customization can improve the efficiency of the approval process and enhance the clarity of communication within organizational procedures.

**Technical Impact when configured:**

When the Escalation Email Template Post Fix is configured, the system will look for an email template that matches the base template name concatenated with the postfix value. This enables the deployment of more specific email templates without altering the basic workflow configuration, thereby facilitating finer control over the content and format of messages sent during various escalation scenarios.

**Examples Scenario:**

If the base email template for a manager's approval step is named "ApprovalRequest" and the Escalation Email Template Post Fix is set to "_Urgent," the system will attempt to use the "ApprovalRequest_Urgent" email template for escalations in this context, allowing for a distinct and possibly more urgent messaging style compared to standard approval requests.

**Related Settings:**

- WorkflowType.EmailMessageTemplate3

**Best Practices:** 

configure when:

- Different stages or types of escalations in workflows require distinctly formatted communications.
- There is a need to enhance clarity and actionability of email communication during specific workflow steps.

avoid when:

- There is insufficient differentiation between workflow steps or types to necessitate unique email templates.
- The complexity introduced by using multiple postfixes outweighs the benefits in communication clarity or process efficiency.