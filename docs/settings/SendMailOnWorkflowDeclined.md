# Send Mail On Workflow Declined

**Technical Name:** SendMailOnWorkflowDeclined

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the sending of email notifications when a workflow is declined. This setting ensures that the right stakeholders are informed promptly about the decline decision, facilitating swift action or review as necessary.

**Business Impact:**

Improves communication and transparency throughout the workflow process. When workflows are declined, it can impact the operational efficiency and compliance posture of the organization. Timely notifications can help mitigate these impacts by allowing for immediate response.

**Technical Impact when configured:**

When activated, the system triggers an email notification to predefined recipients and, optionally, CC recipients, detailing the workflow instance that was declined. This can integrate with other workflow or risk management processes to provide a comprehensive control environment.

**Examples Scenario:**

- A user submits a request for access to a sensitive system. The request goes through various approval stages but is ultimately declined due to a detected segregation of duties (SoD) conflict. An email notification is automatically sent to the requester and the security administrator, informing them of the decision and the reason behind it.

**Related Settings:**

- SendMailOnWorkflowApproved
- SendMailOnStepStarted

**Best Practices:** configure when 

- Immediate notification of declined workflows is critical for maintaining operational continuity and compliance standards.
  
avoid when 

- The volume of workflow declines is high, and notifications may overwhelm recipients or when decline reasons are sensitive and require controlled communication channels.