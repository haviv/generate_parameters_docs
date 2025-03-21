# Display auto-complete missing decisions window:

**Technical Name:** ShowIsApprovedOnPageStart

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:** 

Enables the auto-display of a window on page start, which prompts users with decisions on missing approvals within their workflows. This feature is particularly useful in maintaining efficient progression of tasks and ensuring that important approval steps are not overlooked in the completion of workflows.

**Business Impact:** 

By enabling this parameter, organizations can proactively manage workflow approvals, reducing the chance of process delays and enhancing the overall compliance and efficiency of workflow management. This ensures that critical business processes are not hindered by missing approvals, supporting a more streamlined operation.

**Technical Impact when configured:** 

Upon configuration, the system will automatically prompt users with a decision window for any outstanding approvals at the start of their session. This aims to bring immediate attention to pending tasks that require user intervention, thereby facilitating a quicker response to action items.

**Examples Scenario:** 

Consider a scenario in an HR department where several vacation requests need approval. With this parameter enabled, as soon as the approver logs into the system, they will be greeted with a window listing all vacation requests pending approval. This immediate prompt can help in faster processing of requests, ensuring timely responses and reducing bottlenecks in vacation planning.

**Related Settings:** 

- ServerDiscrepanyEmailAstriskRemark
- ServerDiscrepancyNotInSystem

**Best Practices:** configure when, avoid when 

- Configure when: Your organization's workflow process relies heavily on approvals for moving forward, and there is a need to address bottlenecks caused by missed or delayed approvals.
- Avoid when: Most of your workflows are automated or do not require frequent user approvals, or if such prompts could disrupt the user experience without providing significant benefit.