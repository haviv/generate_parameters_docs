# Requests Waiting For Approval Get Data From Stored Procedure

**Technical Name:** RequestsWaitingForApprovalGetDataFromStoredProcedure

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls how data is retrieved for viewing requests that are waiting for approval in the Workflow Inbox and similar interfaces. When enabled, it fetches the data from a configured stored procedure.

**Business Impact:**

Enabling this parameter can significantly influence the efficiency and responsiveness of the Workflow Inbox, as it directly impacts how quickly and effectively users can review and manage pending requests. It ensures data consistency and potentially improves system performance by optimizing data retrieval processes.

**Technical Impact when configured:**

- Alters the source from which data for pending workflow approvals is fetched, switching it to a pre-defined stored procedure.
- May affect system performance depending on the complexity and optimization of the stored procedure.

**Examples Scenario:**

- **To Improve Data Fetching Efficiency:** For organizations with a high volume of approval requests, enabling this parameter and configuring an optimized stored procedure can reduce data fetching times, thus improving user experience for approvers.
- **Custom Data Retrieval Logic:** When specific business logic needs to be applied to the data before it is presented to the approvers, this parameter enables such customizations by allowing data to be fetched through a stored procedure.

**Related Settings:**

- `DisableApprovalForWorkflowSteps`
- `DisableApprovalForInstanceSteps`
- `DisableDeclineForWorkflowSteps`
- `DisableDeclineForInstanceSteps`

**Best Practices:** 
- **Configure when:**
  - The default data fetching mechanism is not meeting performance expectations.
  - Custom business rules need to be applied to the data before presentation in the Workflow Inbox.
- **Avoid when:**
  - The stored procedure is not optimized for performance, as it could negatively impact the user experience.
  - There is not a clear requirement for custom data processing before approval.