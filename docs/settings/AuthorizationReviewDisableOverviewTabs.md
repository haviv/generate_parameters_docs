# Authorization Review Disable Overview Tabs

**Technical Name:** AuthorizationReviewDisableOverviewTabs

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewDisableOverviewTabs` parameter controls the visibility of overview tabs in the authorization review process. Enabling this setting hides certain UI elements related to the overview of user rights and permissions, streamlining the review process by focusing on specific details.

**Business Impact:**

The visibility of overview tabs can significantly impact the user experience during the authorization review process. Disabling these tabs can make the review process more efficient for organizations with a well-defined review strategy, reducing the time and resources needed for authorization reviews. However, it might also limit the ability to perform a comprehensive review of all user permissions at a glance, potentially increasing the risk of missed unauthorized access points.

**Technical Impact when configured:**

- Hides overview tabs within the authorization certification process.
- Simplifies the user interface, potentially reducing the cognitive load on reviewers.
- Can lead to a more streamlined review process, focusing on individual changes or high-risk areas.

**Examples Scenario:**

A company is conducting a quarterly review of its user access rights and decides to disable the overview tabs to expedite the review process. Reviewers focus solely on assessing high-risk permissions without the distraction of overarching summaries. This approach is particularly useful in tightly controlled environments where changes in permissions are rare and closely monitored.

**Related Settings:** 

- `ShowAdvancedUserGroupFilterSelection`
- `ReportApprovalGlobalScope`

**Best Practices:** configure when a focused review process is needed, avoid when comprehensive oversight is required.