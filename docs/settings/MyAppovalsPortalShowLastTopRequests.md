# My Approvals Portal Show Last Top Requests

**Technical Name:** MyAppovalsPortalShowLastTopRequests

**Category:** Configuration

**Default Value:** 20

**Impact Level:** Medium

**Description:**

This configuration parameter determines the maximum number of approval requests displayed to a user in the My Approvals Portal. It limits the list to the most recent requests to ensure efficient navigation and management.

**Business Impact:**

Setting the appropriate value for this parameter can significantly impact how users prioritize and manage their approval workload. A lower number ensures that users are not overwhelmed by too many requests at once, allowing them to focus on the most urgent approvals. Conversely, a higher value offers a broader overview of pending approvals, which can be beneficial in environments where approvals are quickly processed or require batching.

**Technical Impact when configured:**

Configuring this parameter affects the load time of the My Approvals Portal page, user experience in terms of managing the approval requests, and can help in prioritizing the workflow based on the most recent activities.

**Examples Scenario:**

- A financial organization might configure this parameter to a lower value during end-of-month closing activities to ensure critical financial approvals are prioritized and processed timely.
- In contrast, during standard operations with fewer urgent requests, the value might be increased to ensure a comprehensive view of pending approvals.

**Related Settings:**

- `MyRequestsPortalShowLastTopRequests`

**Best Practices:** 

- **Configure when:** 
  - There is a clear understanding of the average volume of approval requests.
  - Users report issues with navigating or prioritizing approval requests.

- **Avoid when:**
  - Arbitrary changes could lead to overlooking high-priority approvals.
  - Without feedback from users about their needs and the effectiveness of the current setting.