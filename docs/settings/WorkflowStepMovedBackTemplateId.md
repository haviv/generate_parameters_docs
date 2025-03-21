# Workflow Step Moved Back Template

**Technical Name:** WorkflowStepMovedBackTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Workflow Step Moved Back Template ID parameter specifies the template used for generating emails when a workflow step is moved back. This assists in notifying relevant stakeholders of the change and ensures that actions required to correct or review the workflow step are communicated effectively.

**Business Impact:**

Configuring the Workflow Step Moved Back Template ID has a direct impact on how changes in the workflow are communicated within the organization. Proper configuration ensures that the right personnel are informed immediately of any steps moved back, which is vital for maintaining the integrity and efficiency of business processes. This timely communication helps in quick resolution and reduces the risk of process delays or errors.

**Technical Impact when configured:**

When configured, this parameter triggers an automated process to send out notifications using the specified email template whenever a workflow step is moved back. This automation enhances communication flow, reduces manual intervention, and ensures consistent messaging across the platform.

**Examples Scenario:**

- **Scenario 1:** A workflow step in a financial approval process is moved back due to insufficient documentation. The configured template sends an automated email to the submitter and the finance team, detailing the reason for the move back and requesting the necessary documentation.
  
- **Scenario 2:** In the user access review workflow, if a step is moved back to re-evaluate the access rights of a high-risk permission, the system sends out an email to the security and compliance team using the specified template, highlighting the action needed and the urgency of the review.

**Related Settings:**

- WorkflowHeaderDirectionLTR
- Workflow_EmployeeCard
- WorkflowRequestForwardOnDateTechnicalName

**Best Practices:** configure when a clear, transparent communication channel is necessary for workflow adjustments. Avoid when unnecessary to reduce email clutter or if the step movement does not significantly impact the process outcome.