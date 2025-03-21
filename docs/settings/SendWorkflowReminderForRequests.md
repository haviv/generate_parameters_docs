# Send Workflow Reminder For Requests

**Technical Name:** SendWorkflowReminderForRequests

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter `SendWorkflowReminderForRequests` is designed to trigger email reminders for pending workflow actions. It aims to notify responsible parties about outstanding tasks within the workflow, ensuring timely action on requests that are awaiting approval or any further step as part of the workflow sequence.

**Business Impact:**

Implementing reminders for workflow requests significantly enhances the operational efficiency of an organization. It ensures that workflow related tasks do not stall due to inaction, facilitating smoother operations, greater compliance, and timely decision-making which are critical in managing security, risk, and compliance within an enterprise.

**Technical Impact when configured:**

Once configured, the system automatically sends out reminder emails for any step within a workflow that has not been completed by the set deadline. This helps in reducing delays in the workflow process, improving the overall turnaround time for requests requiring approvals or any other workflow action.

**Examples Scenario:**

- **Approval Delays:** In instances where a request needs approval from a specific department head, the parameter, when enabled, sends a reminder to the approver, thus minimizing decision-making delays.
- **Compliance Deadlines:** Reminders for tasks that are critical for maintaining compliance can ensure that such tasks are prioritized and addressed within the specified timelines.

**Related Settings:**

- `SoDCheckEmployeeSoDForMultiSystemOnly`
- `SoCheckUserSoDByEmployeeAuthorizations`

**Best Practices:** 

- **Configure when:** Immediate or timely actions on requests are critical for the business workflow. Particularly useful in high-volume environments where requests can easily be overlooked.
- **Avoid when:** Processes do not have a critical time sensitivity or if frequent reminders could lead to email fatigue among users.