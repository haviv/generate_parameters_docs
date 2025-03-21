# Log Workflow Requests From Email Accounts

**Technical Name:** LogWorkflowRequestsFromEmailAccounts

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to enable the logging of workflow requests that are initiated through email accounts. It facilitates the tracking and auditing of actions initiated via email, ensuring that all workflow requests are logged and accessible for review.

**Business Impact:**

Enabling this feature supports stronger governance by providing transparency and accountability for actions initiated via email, a common entry point for various workflow requests. It aids in compliance with internal policies and external regulations by ensuring that all such requests are documented and auditable.

**Technical Impact when configured:**

Once configured, the system will start logging all workflow requests that originated from email accounts. This includes capturing details about the request, the requester's email account, and the specific actions taken in response to the email. This information is crucial for audit trails and for analyzing workflow efficiency and security.

**Examples Scenario:**

A user sends an email to request access to a specific application. The system, having the LogWorkflowRequestsFromEmailAccounts parameter enabled, logs this request along with the details of the email sender and the actions taken by the workflow system in response to this request.

**Related Settings:**

- WorkflowEmailAccount
- _minutesIntervalToReadMail

**Best Practices:** Configure when you need detailed audit trails of workflow actions initiated via email. Avoid enabling this feature if your organization does not use email to initiate workflow requests or if logging such requests would violate privacy policies or regulations.