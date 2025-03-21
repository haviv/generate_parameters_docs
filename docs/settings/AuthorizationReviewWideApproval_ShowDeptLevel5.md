# Authorization Review Wide Approval Show Dept Level5

**Technical Name:** AuthorizationReviewWideApproval_ShowDeptLevel5

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of Department Level 5 information within the Authorization Review process for wide approvals. When enabled, it allows users conducting an authorization review to see detailed departmental hierarchy up to the fifth level. This enhancement aims to provide finer granularity in the review process, enabling more informed decisions.

**Business Impact:**

Enabling this feature has a direct impact on the authorization review process's thoroughness and accuracy. By providing visibility up to Department Level 5, organizations can ensure that approvals are granted with a deep understanding of the hierarchical structure, potentially reducing the risks associated with incorrect or overly broad authorizations. This is particularly crucial for large organizations with complex departmental structures.

**Technical Impact when configured:**

When this parameter is configured to show Department Level 5 details, the Authorizations Review page will display additional information related to the employees' departmental hierarchy. This could lead to a more comprehensive review process, as reviewers can leverage this added layer of detail to make more nuanced decisions regarding authorization approvals.

**Examples Scenario:**

In a scenario where a company has a multi-layered departmental structure, an employee from a sub-department at Level 5 requires certain access rights. Reviewers, with this parameter enabled, could see the employee's exact position within the organizational hierarchy, aiding in determining whether the requested access is appropriate for their role and department level.

**Related Settings:**

- AuthorizationReviewWideApproval_ShowJobTitle
- AuthorizationReviewWideApproval_ShowActivityGroup

**Best Practices:** 

- **Configure when:** You have a complex organizational structure with multiple layers of departments, and there's a need for granular visibility during the authorization review process.
- **Avoid when:** Your organization has a flat structure with less emphasis on departmental levels or when the added information may overload the reviewers without adding meaningful insight.