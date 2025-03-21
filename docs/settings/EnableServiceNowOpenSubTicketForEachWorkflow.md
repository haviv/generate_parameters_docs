**Enable Service Now Open Sub Ticket For Each Workflow**

**Technical Name:** EnableServiceNowOpenSubTicketForEachWorkflow

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the automatic generation of sub-tickets in Service Now for each action within a workflow. When enabled, the Pathlock Cloud GRC platform creates a dedicated Service Now ticket for individual tasks or actions that are part of a larger workflow process.

**Business Impact:**

Enabling this feature ensures that each step of a workflow is tracked individually in Service Now, enhancing the auditability and traceability of processes. This can lead to improved response times to issues and tighter integration between GRC processes and IT service management.

**Technical Impact when configured:**

Upon configuration, the system will make API calls to Service Now to create sub-tickets for each action within a workflow, ensuring that all workflow actions are logged and can be individually tracked and managed in Service Now. This can increase the number of API calls and may require additional configuration within Service Now to handle these tickets appropriately.

**Example Scenario:**

For instance, during a risk assessment workflow, separate sub-tickets may be created for the identification, analysis, and mitigation steps. This allows each team responsible for these steps to manage their tasks directly in Service Now, facilitating clearer communication and responsibility delineation.

**Related Settings:**

- ServiceNowIntegrationEnabled
- WorkflowInstanceManagementSettings

**Best Practices:** configure when the organization requires granular tracking and accountability of workflow actions within Service Now. Avoid when the organization has a simplified workflow that does not benefit from the overhead of managing multiple sub-tickets.