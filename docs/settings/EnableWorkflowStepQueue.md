**Enable Workflow Step Queue**

**Technical Name:** EnableWorkflowStepQueue

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter enables or disables the queueing of workflow steps in the Pathlock Cloud GRC platform. When enabled, it allows for managing the workflow steps more efficiently by queuing them for processing.

**Business Impact:**

Enabling the Workflow Step Queue can significantly streamline business processes by ensuring that workflow steps are executed in an orderly and efficient manner. This can improve the overall response time for completing workflows, thereby enhancing operational efficiency and productivity.

**Technical Impact: when configured**

When configured, this parameter affects how workflow steps are managed within the system. It changes the execution flow to a queued process, potentially leading to more predictable processing times and reducing the likelihood of steps being overlooked or executed out of sequence.

**Examples Scenario:**

A typical use case would be in managing approval processes for financial transactions. By enabling the Workflow Step Queue, each step in the approval process is queued and processed sequentially, ensuring that each approval is obtained in the correct order and within the desired timeframe.

**Related Settings:** 

- AutoRefreshUserInforamationForEmergencyAccessStep
- WorkflowRisksSimpleMode

**Best Practices:** configure when, avoid when

- **Configure when:** The workflow process involves multiple steps that must be completed in a specific order, or when there's a high volume of workflows that need to be processed efficiently.
- **Avoid when:** The workflow process is simple and does not benefit from the added complexity of queueing, or when workflow step execution needs to remain flexible without strict ordering.