# Custom Role For Auto Complete

**Technical Name:** CustomRoleForAutoComplete

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CustomRoleForAutoComplete` parameter is utilized within the Pathlock Cloud GRC platform to enhance the efficiency and accuracy of auto-completing workflow steps based on custom role definitions. By leveraging this parameter, organizations can streamline their workflow creation processes, ensuring that steps are auto-filled with appropriate roles, thus reducing manual entry errors and improving workflow setup time.

**Business Impact:**

Implementing the `CustomRoleForAutoComplete` parameter directly impacts the operational efficiency of setting up and managing workflows in the Pathlock platform. It plays a crucial role in the governance, risk management, and compliance (GRC) process by enabling quicker setup of workflows with reduced chances of error, which in turn helps organizations remain compliant and manage their risks more effectively.

**Technical Impact when configured:**

Once configured, this parameter automatically suggests the most relevant roles for each step in a workflow based on predefined custom roles. This capability significantly decreases the time required to configure workflows, improves accuracy by minimizing manual input, and ensures that workflow steps are aligned with organizational roles and responsibilities.

**Example Scenario:**

Consider an organization that frequently updates its workflows in response to evolving compliance requirements. Manually searching and entering roles for each step can be time-consuming and prone to errors. By configuring `CustomRoleForAutoComplete`, when a workflow step is being created or edited, the system automatically suggests roles that are best suited for that step, based on the historical data and predefined criteria, thus streamlining the workflow creation process.

**Related Settings:** `WorkflowInboxGroupItemsByCategory`

**Best Practices:** configure when setting up new workflows to leverage historical role data for auto-completion, avoid when workflows require highly specialized roles not encompassed by the system’s historical data.