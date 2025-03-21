# Authorization Request Maximum Number Of Multiple Rows

**Technical Name:** AuthorizationRequestMaximumNumberOfMultipleRows

**Category:** Workflow UI

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the maximum number of rows that can be included in a single authorization request within the Pathlock Cloud GRC platform.

**Business Impact:**

Limiting the number of rows per authorization request helps manage system load and ensures efficient processing of requests. It impacts how granularly permissions can be requested and reviewed within a workflow, directly affecting operational efficiency and security posture.

**Technical Impact when configured:**

Configuring this parameter can significantly impact the workflow execution by controlling the bulk size of data each authorization request can handle. It prevents potential system overload scenarios by limiting the scope of each request, ensuring stable and predictable system performance.

**Example Scenario:**

An organization has set the Authorization Request Maximum Number Of Multiple Rows to 100. This means when users submit a request for bulk access rights changes, each submission can include up to 100 individual item changes. If a department needs to change access for 300 users, this will require at least three separate authorization requests.

**Related Settings:**

- WorkflowInstanceID
- WorkflowType

**Best Practices:** Configure the Authorization Request Maximum Number Of Multiple Rows based on your organization's typical operational requirements and system capacity. Avoid setting it too high to prevent system performance issues or too low, which could lead to operational inefficiencies.