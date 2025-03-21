**Technical Name:** SkippedStepsInWorkflowFlowDocumentionNotation

**Category:** Workflow

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter is used within the Pathlock Cloud GRC platform's workflow engine to document and handle scenarios where certain steps in a process are intentionally bypassed or skipped. It ensures that the workflow can dynamically adjust to different paths based on predefined conditions, without compromising the integrity or completeness of the workflow execution.

**Business Impact:**

Implementing the SkippedStepsInWorkflowFlowDocumentionNotation parameter allows for greater flexibility in managing complex business processes. It enables organizations to streamline operations, ensure compliance by documenting deviations, and address exceptions effectively. This can lead to significant efficiency gains, risk mitigation, and enhanced auditability of processes.

**Technical Impact when configured:**

When configured, this parameter affects how workflow instances are processed. It allows the system to skip specific steps under certain conditions without stopping the entire workflow. This is crucial for maintaining the flow of tasks in situations where not all steps are applicable or necessary, thus preventing unnecessary delays and ensuring that workflows remain efficient and adaptable.

**Example Scenario:**

An example scenario where SkippedStepsInWorkflowFlowDocumentionNotation might be used is in an employee onboarding process. Suppose a new hire does not require access to a specific software due to their role. In that case, the workflow step involving access provisioning to that software can be skipped without halting the overall onboarding process. This ensures that the employee onboarding workflow can dynamically adjust to the needs of different new hires without requiring manual intervention or custom workflow creation for each unique situation.

**Related Settings:** RemediationWorkflowsSOD

**Best Practices:** 

- **Configure when:** There is a clear understanding of the workflow paths and conditions under which certain steps can be safely skipped without affecting the outcome of the overall process.
- **Avoid when:** The criteria for skipping steps are not well-defined, which could lead to skipping essential steps inadvertently, thereby compromising the process's integrity or completeness.