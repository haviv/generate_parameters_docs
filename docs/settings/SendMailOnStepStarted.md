**Send Mail On Step Started**

**Technical Name:** SendMailOnStepStarted

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `SendMailOnStepStarted` parameter is designed to trigger email notifications whenever a specific workflow step begins. Its primary function is within the workflow management context, ensuring stakeholders are informed in real-time about the commencement of critical workflow steps, particularly in emergency access scenarios or role-based access changes.

**Business Impact:**

Implementing this parameter can significantly enhance communication and responsiveness within an organization's GRC (Governance, Risk Management, and Compliance) procedures. By enabling immediate notification, it supports swift decision-making and oversight, crucial in managing risk and maintaining compliance standards.

**Technical Impact when configured:**

Upon configuration, the system automatically generates and sends an email to predefined recipients or groups at the start of a workflow step. This functionality aids in monitoring workflow progress and ensures that relevant parties are aware of changes or actions required in critical processes.

**Example Scenario:**

Consider an emergency access situation where specific roles are granted temporary access to sensitive resources. By configuring `SendMailOnStepStarted`, an email alert is sent out as soon as the step granting access is initiated, informing the security team or management. This prompt notification allows for immediate scrutiny and oversight, ensuring the access is justified and within policy bounds.

**Related Settings:**

- WorkflowType.PatternSet.Name

**Applicable Workflows Actions:** 

**Best Practices:** 

- **Configure when:** Immediate notification of workflow step commencement is crucial for oversight or compliance. It is particularly useful for high-stakes processes such as emergency access management, where timing and responsiveness are critical.
  
- **Avoid when:** The workflow process does not require real-time monitoring or if excessive notifications could lead to alert fatigue among recipients.