# No Email Recipients Template

**Technical Name:** NoEmailRecipientsTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The 'No Email Recipients Template' parameter is designed to handle scenarios where email sending for workflow actions is disabled. This parameter specifies a template identifier used for logging attempts to send emails when the 'Send Workflow Mails' setting is turned off. Instead of sending emails, the system records an attempt with details about the recipients, subject, and a temporary log file. This functionality ensures that there is an audit trail for email notifications that would have been sent, aiding in troubleshooting and monitoring email-related configurations and policies.

**Business Impact:**

Having a clear record of emails that were prevented from sending can help in identifying issues with email notifications in workflow processes. It ensures transparency and aids in regulatory compliance by providing evidence of how notification attempts are handled when the email sending feature is toggled off, contributing to internal and external audit requirements.

**Technical Impact when configured:**

When configured, any attempt to send an email as part of a workflow action with email notifications disabled results in the creation of a log entry. This entry includes the intended recipients, the subject of the missed email, and a reference to a temporary log file capturing the event. This mechanism allows administrators to review what notifications would have been sent out, thereby enabling analysis and adjustments to communication policies or workflows as necessary.

**Examples Scenario:**

- **Compliance Auditing**: In scenarios where an organization needs to prove that particular notifications were generated (even if not sent), this parameter helps by logging each email attempt. For example, in a compliance audit, it can show that notifications for approval workflows were generated according to policy, but not sent due to configuration settings.
- **Troubleshooting**: Helps IT and GRC managers understand which emails were not sent when diagnosing issues related to users not receiving expected notifications from the Pathlock Cloud GRC system.

**Related Settings:**

- `Send Workflow Mails` in Advanced Configuration

**Best Practices:** configure when the organization decides to disable email sending temporarily or permanently for auditing and monitoring purposes; avoid when full email functionality is required for all system workflows.