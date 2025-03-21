# Show Only End Users

**Technical Name:** ShowOnlyEndUsers

**Category:** User Management

**Default Value:** Not specified in the provided references.

**Impact Level:** Medium

**Description:**

The `ShowOnlyEndUsers` parameter is designed to filter and display data relevant only to end users within various reports and dashboards on the Pathlock Cloud GRC platform. This filtering helps in narrowing down the visibility to the activities, risks, or compliance statuses pertinent to end-user roles, thereby making the data representation more relevant and actionable for specific user groups.

**Business Impact:**

Applying the `ShowOnlyEndUsers` filter can significantly enhance decision-making processes by providing a focused view on end-user activities and risks. It helps in identifying potential security or compliance issues among the end-user segment, facilitating targeted remediation actions and improving overall compliance and security posture.

**Technical Impact when configured:**

When the `ShowOnlyEndUsers` parameter is configured, the system will exclude non-end-user-specific data from the reports and dashboards. This ensures that the displayed information is directly relevant to managing and assessing the risks, activities, and compliance of end users.

**Examples Scenario:**

- **Security Assessment:** A compliance officer needs to assess the security posture of end users who have access to sensitive financial data. By applying the `ShowOnlyEndUsers` filter, they can easily identify and focus on the accounts that directly interact with this data, streamlining the assessment process.
  
- **Compliance Reporting:** During an audit, an auditor wishes to review access rights and activity logs of end users to ensure no unauthorized access to protected health information (PHI). Utilizing this parameter would allow for a streamlined and focused audit process.

**Related Settings:**

- `ShowAuthorizationFieldInRoleUsage`
- `ShowEventDetailsInWorkflow`

**Best Practices:** 

- **Configure when:** You need a clear and concise view of end-user related data for security, compliance, or audit purposes. This is particularly useful in large organizations with complex user structures.
  
- **Avoid when:** Comprehensive data, including both end-user and system-level interactions, is necessary for broader analysis or when the inclusion of all user types is critical for the assessment at hand.