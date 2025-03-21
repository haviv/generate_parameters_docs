# Enable Advanced Workflow Trace

**Technical Name:** EnableAdvancedWorkflowTrace

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**  
Enables detailed tracing of workflow actions to aid in debugging and enhancing the performance of workflow-related processes.

**Business Impact:**  
Activating this parameter helps in identifying issues in workflow actions much more efficiently, leading to decreased downtime and smoother operations within Pathlock's cloud GRC platform. This can significantly impact an organization's ability to maintain tight security, risk management, and compliance processes.

**Technical Impact when configured:**  
When enabled, the system begins to log detailed information about the execution of specific workflow actions such as file uploads, role assignments, and user creations. This includes data on the user performing the action, the specific files or roles being processed, and any errors or anomalies encountered during the action's execution.

**Examples Scenario:**  
A company notices irregularities in the permissions being assigned through workflow actions. By enabling the advanced workflow trace, administrators can pinpoint the exact step where the discrepancies occur, making it easier to implement fixes and ensure proper compliance and security postures are maintained.

**Related Settings:**  

- ListGroupTemplate
- ListGroupOU
- PermissionGroupTemplate
- PermissionGroupOU
- ListGroupPrefix

**Best Practices:** configure when troubleshooting complex workflow issues to identify and resolve inefficiencies or errors; avoid when in regular operation mode to reduce unnecessary system load.