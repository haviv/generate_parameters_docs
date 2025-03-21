# Authorization Review Wide Approval Show Dept Level4

**Technical Name:** AuthorizationReviewWideApproval_ShowDeptLevel4

**Category:** Configuration

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the fourth level department details in the authorization review wide approval process within the Pathlock Cloud GRC platform. It specifies whether users can view detailed departmental information when conducting wide approval of authorization reviews.

**Business Impact:**

Enabling this parameter can provide a deeper understanding of the organizational structure during the review process, potentially highlighting areas of risk or concern in specific departments. It assists in making informed decisions during the approval process by offering an additional layer of detail.

**Technical Impact when configured:**

When enabled, the authorization review interface will include an additional level of department detail, allowing approvers to view and consider fourth-level department information. This can affect the user interface's complexity and the amount of information an approver must evaluate.

**Examples Scenario:**

- **Scenario 1:** In an organization with a deep departmental structure, enabling this feature helps approvers identify authorization requests coming from specific sub-departments, enhancing the granularity of the review process.

**Related Settings:**

- AuthorizationReviewWideApproval_ShowActivityGroup
- AuthorizationReviewWideApproval_ShowApplicationArea

**Best Practices:** 

- **Configure when:** Detailed departmental scrutiny is required during the authorization review process to identify specific security or compliance risks.
- **Avoid when:** The additional departmental detail complicates the review process without adding significant value, or if the organizational structure does not benefit from this level of granularity.