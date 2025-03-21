# Send Mail On Workflow Approved

**Technical Name:** SendMailOnWorkflowApproved

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This parameter controls the automation of email notifications upon approval of workflow instances within the Pathlock Cloud GRC platform. When a workflow reaches an approved state, an email is triggered to the pertinent recipients.

**Business Impact:**

Enabling this feature ensures that stakeholders are promptly informed about workflow approvals, fostering better communication and faster action on subsequent steps. It aids in maintaining transparency and efficiency in the organization's governance, risk, and compliance (GRC) processes.

**Technical Impact when configured:**

Configuring this parameter automates the distribution of email notifications to designated recipients, minimizing manual communication tasks and reducing the risk of information delays or oversights.

**Examples Scenario:**

Scenario: A user submits a request for access rights adjustment. The request undergoes review and is approved by the authorized personnel. With `SendMailOnWorkflowApproved` enabled, an email is automatically sent to the user, the request initiator, and any other stipulated parties, thereby informing them of the approval without manual intervention.

**Related Settings:** 

- `NoEmailRecipientsTemplateId`: Specifies the template used when there are no email recipients defined for a notification.

**Best Practices:** configure when critical workflow approvals need immediate notification to relevant parties; avoid when non-critical workflows do not necessitate instant communication, to reduce email clutter.