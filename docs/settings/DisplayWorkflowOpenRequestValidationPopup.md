# Display Workflow Open Request Validation Popup

**Technical Name:** DisplayWorkflowOpenRequestValidationPopup

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Display Workflow Open Request Validation Popup parameter is a configurational setting within the Pathlock Cloud GRC platform that controls the visibility of a validation popup when opening a workflow request.

**Business Impact:**

Enabling this parameter enhances the user's understanding of the validation process by providing immediate, context-sensitive feedback at the moment a workflow request is initiated. This serves to preemptively address potential issues that could delay or complicate the workflow approval process, thereby streamlining operations and mitigating the risk associated with unvalidated or improper requests.

**Technical Impact when configured:**

When enabled, this setting triggers a popup to appear for further validation whenever a workflow request is opened. This ensures that all necessary checks and balances are in place before a request moves forward in the workflow process, potentially reducing the chances of errors or oversight.

**Examples Scenario:**

In a scenario where an employee requests access to sensitive financial records, enabling the Display Workflow Open Request Validation Popup ensures that when the request is initiated, a popup appears to validate the request against the company’s security policies. If the request violates a policy, the popup can inform the requester or the approver, prompting immediate correction or review.

**Related Settings:** 

- DisplayApplicationAreaOnRolesAuthorizationReview
- DisplayRisksChartView
- DisplayRoleTypeInWorkflowRoleManagement

**Best Practices:** 

- **Configure when:** It is critical to provide immediate feedback on the validity of workflow requests, especially in complex workflows or those involving sensitive information.
- **Avoid when:** Workflows are straightforward, and additional validation steps may introduce unnecessary delays.