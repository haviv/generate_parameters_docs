# Workflow Export Include Approval Groups

**Technical Name:** WorkflowExportIncludeApprovalGroups

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether approval groups are included during the export of workflow configurations in the Pathlock Cloud GRC platform. Including approval groups can provide a comprehensive overview of the workflow structure, ensuring that all necessary permissions and approvals are correctly mapped and maintained across different environments.

**Business Impact:**

Inclusion of approval groups during workflow exports facilitates easier replication of workflow configurations across different instances or environments within the organization. This is particularly beneficial for organizations looking to maintain consistent security policies and compliance standards, as it ensures that all workflows have the appropriate approval processes in place, reducing the risk of unauthorized actions.

**Technical Impact when configured:**

When configured to include approval groups in workflow exports, the system will compile a list of all approval groups associated with the specific workflow steps and include them in the export file. This ensures that when the workflow is imported into another environment, it retains its comprehensive structure, including both the workflow logic and the necessary approval hierarchies.

**Example Scenario:**

A company operates multiple instances of Pathlock Cloud GRC for different departments. To ensure compliance, a central security team creates a standardized set of workflows, including specific approval groups necessary for sensitive actions. By enabling WorkflowExportIncludeApprovalGroups, they can export these workflows from the development instance and import them into the production instances of each department, ensuring that the necessary approval processes are enforced everywhere.

**Related Settings:**

- WorkflowRisksSimpleMode
- UsernameForExternalFileAttachments

**Best Practices:** 

- **Configure when:** You are maintaining multiple environments (development, test, production) and need to ensure consistent workflow configurations across them, especially regarding approval processes.
- **Avoid when:** Simplified workflow exports are needed for review or documentation purposes, and the inclusion of approval groups would complicate the configuration unnecessarily.