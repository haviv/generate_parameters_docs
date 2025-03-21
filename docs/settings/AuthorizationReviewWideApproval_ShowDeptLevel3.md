**Authorization Review Wide Approval Show Dept Level3**

**Technical Name:** AuthorizationReviewWideApproval_ShowDeptLevel3

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:** This setting controls whether Department Level 3 data is shown during the authorization review process for wide approvals.

**Business Impact:** Enabling this feature ensures that reviewers have visibility over departmental structures up to three levels deep, enhancing the decision-making process by providing additional context around the roles and responsibilities of the users under review. This can lead to more informed approval decisions and enhance the security posture by appropriately managing access at a granular level.

**Technical Impact when configured:** When enabled, users with the necessary permissions will see Department Level 3 data in the authorization review screens. This additional data can aid in identifying any discrepancies or unnecessary permissions granted to users, ensuring that only appropriate levels of access are maintained.

**Examples Scenario:** Suppose a company uses a complex organizational structure with multiple layers of departments. In such a case, enabling this parameter allows reviewers to see detailed departmental information up to three levels deep during an authorization review. For example, when reviewing a user's access permissions, a reviewer can see that the user belongs to "Sales > North America > East Coast," providing clear context on the user's role and the appropriateness of their access levels.

**Related Settings:** AuthorizationReviewWideApproval_ShowDeptLevel5

**Best Practices:** configure when

- The organization has a complex departmental structure, and additional context is needed to make informed approval decisions.
  
avoid when

- The organization has a flat structure, making this level of detail unnecessary and potentially overwhelming for the reviewers.