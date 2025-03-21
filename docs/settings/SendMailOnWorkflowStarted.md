# Send Mail On Workflow Started

**Technical Name:** SendMailOnWorkflowStarted

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The SendMailOnWorkflowStarted parameter enables the automatic sending of an email notification when a workflow is initiated within the Pathlock Cloud GRC platform. This feature is crucial for keeping relevant stakeholders informed about the initiation of key workflows, enhancing communication and oversight across GRC processes.

**Business Impact:**

Enabling this parameter ensures that project managers, compliance officers, and other relevant stakeholders are immediately notified when specific workflows are started, promoting timely responses and actions. It supports both operational efficiency and compliance by ensuring that all involved parties are kept in the loop, facilitating quicker decision-making and reducing the risk of oversight.

**Technical Impact when configured:**

When this parameter is configured, an email notification is generated and sent to predefined recipients whenever a supported workflow is initiated. The email includes details such as the type of workflow started and the workflow instance ID, along with a list of recipients and, if applicable, CC'd parties. It utilizes the platform's email template settings to format the message.

**Examples Scenario:**

- **Scenario:** A compliance review workflow is initiated within the Pathlock platform. The SendMailOnWorkflowStarted parameter is enabled.
  - **Outcome:** All configured recipients, including the compliance team and project managers, receive an email notification. This notification informs them that the compliance review workflow has started, allowing them to take any necessary actions or prepare for upcoming tasks in the workflow.

**Related Settings:**

- RequestRecievedTemplateId

**Best Practices:** 

- **Configure when:** Immediate notification of workflow initiation is critical for compliance, oversight, or coordination purposes. It is especially useful for workflows that have significant business implications or require timely input from various stakeholders.
- **Avoid when:** Workflows are too frequent or of low significance, which might lead to email overload or desensitization to important notifications.