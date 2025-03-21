# Extended Request Time Hours

**Technical Name:** ExtendedRequestTimeHours

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to extend the time allowed for a specific step in the workflow process related to authorization requests. It adjusts the deadline for the step completion by adding additional hours, thus providing flexibility in cases where the standard processing time is insufficient.

**Business Impact:**

This setting is particularly important for ensuring that critical business processes are not delayed due to workflow constraints. For example, if a user needs immediate access to a system for a time-sensitive project but the standard approval process would take too long, the ExtendedRequestTimeHours can be utilized to expedite the process, thus avoiding potential delays in project execution.

**Technical Impact when configured:**

- Extends the deadline for workflow step completion.
- Helps in preventing bottlenecks in the approval process by allowing additional time for approvers to take action.
- Can be adjusted to match the urgency and importance of the request.

**Example Scenario:**

Consider a scenario where an employee needs urgent access to a financial system for closing the quarterly accounts. The standard workflow approval process takes 24 hours, but due to the quarter-end time constraints, the process needs to be expedited. By configuring the `ExtendedRequestTimeHours`, the workflow can accommodate this urgent request by extending the approval time window, ensuring that the employee gains necessary access in time to complete the financial closure process.

**Related Settings:**

- `ShowWorkflowWaitingForApproversSeparator`

**Best Practices:** 

- **Configure when:** There are foreseeable delays or urgent requests that necessitate deviation from standard workflow timings.
- **Avoid when:** Standard workflow timings are sufficient for most processes, to prevent unnecessary deviations that could lead to inconsistencies.