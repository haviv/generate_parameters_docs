# Perform Manual Workflow Actions On Done

**Technical Name:** PerformManualWorkflowActionsOnDone

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

Allows for manual execution of workflow actions after a workflow step is marked as done. This setting enables administrators to configure additional, custom actions that should be taken when a workflow process reaches a certain completion point.

**Business Impact:**

Enabling this parameter can significantly enhance operational efficiency by automating follow-up tasks that would otherwise require manual intervention. It ensures that all necessary actions are taken upon the completion of a workflow step, reducing the risk of human error and ensuring that key processes are executed in a timely manner.

**Technical Impact when configured:**

When enabled, this parameter allows the system to perform designated actions automatically at the completion of workflow steps. This can include sending notifications, updating status in other systems, or triggering additional workflows. This reduces the need for manual intervention and ensures consistent execution of follow-up steps.

**Examples Scenario:**

- Upon approval of a new vendor, triggering a workflow that automatically sends out welcome emails and initiates onboarding processes.
- After a risk assessment workflow is completed, automatically updating the risk status in the GRC platform and notifying relevant stakeholders.
- Automatically generating and sending compliance reports to auditors once a compliance workflow is marked as done.

**Related Settings:** 

- SapDownloadDataButtons
- IsCloud

**Best Practices:** 

- **Configure when:** there is a clear understanding of all actions that need to be performed after a workflow step is completed to automate repetitive tasks and ensure nothing is missed.
  
- **Avoid when:** the actions that need to be taken are not well-defined or when manual oversight is preferred to ensure accuracy before proceeding to the next step.