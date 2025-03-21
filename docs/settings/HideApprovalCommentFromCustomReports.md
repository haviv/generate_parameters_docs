# Hide Approval Comment From Custom Reports

**Technical Name:** HideApprovalCommentFromCustomReports

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter controls whether approval comments are included or excluded from custom reports generated within the Pathlock platform. When enabled, this setting ensures that sensitive approval comments are not visible in the output of custom reports, enhancing the security and privacy of the approval process.

**Business Impact:** Enabling this feature helps in maintaining the confidentiality of the approval comments that might contain sensitive information. It ensures that only authorized personnel can view these comments, thereby protecting business-sensitive data and adhering to compliance requirements.

**Technical Impact when configured:** When this parameter is activated, any custom report generated will exclude the approval comments column from its data presentation layer. This affects how reports are visualized and interacted with by end-users, ensuring that approval-specific commentary is safeguarded against unauthorized access.

**Examples Scenario:** A user generates a custom report to audit user access approvals within a specific period. If the 'Hide Approval Comment From Custom Reports' parameter is enabled, the report will exclude the approval comments, ensuring that sensitive decision-making rationale remains confidential and is not exposed to unauthorized viewers.

**Related Settings:** 

**Applicable Workflows Actions:** 

**Best Practices:** configure when sensitive information is discussed in the approval comments that should not be disclosed through reporting. Avoid when it is necessary for report users to understand the context or reasoning behind each approval.