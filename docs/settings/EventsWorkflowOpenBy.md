# Initiator name for workflow triggered by event

**Technical Name:** EventsWorkflowOpenBy

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `EventsWorkflowOpenBy` parameter specifies the user who initiates a workflow process in response to a particular event. Workflows can be triggered by various system or user events, indicating a change or an action that requires further processes or approvals within the Pathlock Cloud GRC platform.

**Business Impact:**

Proper configuration of this parameter ensures that workflows related to critical business functions such as compliance checks, security incident responses, and risk management tasks are initiated by the appropriate user or system account. This can help in ensuring accountability, timely response to events, and adherence to internal policies and external regulations.

**Technical Impact when configured:**

Upon configuration, the `EventsWorkflowOpenBy` parameter ensures that the correct initiator is recorded for audit and compliance purposes whenever a workflow is started in response to an event. This aids in tracking the flow of actions in the system, thus improving security and operational efficiency.

**Examples Scenario:**

- **Event Trigger:** An employee's job title is changed in the HR system.
- **Workflow:** A compliance check workflow is initiated to verify if the new job title aligns with the employee's access rights in the IT systems.
- **Initiator:** The `EventsWorkflowOpenBy` parameter is set to the system account monitoring HR changes, which automatically initiates the workflow when the event occurs.

**Related Settings:**

- EventOnEmployeeJobTitleChange
- EventOnEmployeePositionCodeChange

**Best Practices:** 

- **Configure when:** It is clear which user or system account should be responsible for initiating workflows in response to specific events. This is usually determined by the organization's internal control framework and compliance requirements.
- **Avoid when:** The initiator cannot be clearly defined or when the initiation of workflows should not be attributed to a specific user or system account, to prevent confusion or misattribution of actions.