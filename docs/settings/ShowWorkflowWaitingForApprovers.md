# Show Workflow Waiting For Approvers

**Technical Name:** ShowWorkflowWaitingForApprovers

**Category:** Workflow

**Default Value:** Not explicitly specified in the provided references.

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of workflow steps that are awaiting approval within various reports and interfaces in the Pathlock Cloud GRC platform. When enabled, it allows users to view specific stages of the workflow that require approvals, enhancing transparency and oversight within the governance, risk, and compliance processes.

**Business Impact:**

Enabling this parameter can significantly improve the workflow management by providing real-time insight into where each request stands in the approval chain. It aids in identifying bottlenecks and ensures timely follow-up, ultimately enhancing the efficiency and accountability of the approval process.

**Technical Impact when configured:**

- Enhances report detail by showing waiting phases in workflow processes.
- Improves oversight on requests requiring approval.
- Aids in audit and compliance by providing detailed tracking of the approval process.

**Examples Scenario:**

An auditor requires a comprehensive view of all requests within a certain period that are pending approval to evaluate the efficiency of the workflow process and ensure compliance with internal policies. Enabling `ShowWorkflowWaitingForApprovers` will populate the reports with the necessary data, facilitating a thorough audit and compliance check.

**Related Settings:**

- ShowWorkflowStepEnd
- ShowApprovedRequests

**Best Practices:** 

- Configure `ShowWorkflowWaitingForApprovers` in reporting modules to enhance transparency and tracking of approval workflows.
- Avoid enabling this setting if there is no need for detailed tracking of each waiting step in the workflow process to maintain report readability.