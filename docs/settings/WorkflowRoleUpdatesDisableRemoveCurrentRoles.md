# Workflow Role Updates Disable Remove Current Roles

**Technical Name:** WorkflowRoleUpdatesDisableRemoveCurrentRoles

**Category:** Workflow Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The `WorkflowRoleUpdatesDisableRemoveCurrentRoles` parameter is configured within the Pathlock Cloud GRC platform to manage how role updates within workflow processes handle existing roles assigned to users or entities. When enabled, this setting prevents the automatic removal of current roles during the update process within specific workflow actions. 

**Business Impact:**

Enabling this parameter can significantly reduce the risk of inadvertently removing essential roles from users, which could potentially interrupt access to critical applications or data within an organization. It aids in maintaining consistent access controls during the workflow-based role update process, ensuring that operational continuity is preserved.

**Technical Impact when configured:**

- Prevents the workflow engine from automatically removing existing roles from a user or entity during role update processes in workflows.
- Ensures existing access permissions are not unintentionally revoked, which could lead to business process interruptions or security vulnerabilities.

**Examples Scenario:**

Consider a scenario in which an employee is undergoing a department transfer and requires updated access permissions. If the `WorkflowRoleUpdatesDisableRemoveCurrentRoles` parameter is enabled, the employee's existing roles that are still relevant will not be removed during the workflow process of updating their access permissions to reflect their new departmental role, preventing accidental loss of necessary access.

**Related Settings:**

- WorkflowRemainderEmailTemplateId
- ForceWorkflowRoleUpdateDisplay

**Best Practices:** 

- **Configure when:** There's a high business impact related to the accidental removal of roles during workflow processes, or when workflows are heavily utilized for role management within sensitive environments.
- **Avoid when:** Role update processes are tightly controlled, and there's confidence in the existing mechanisms to manage role additions and removals accurately without the need for additional safeguards.