# Workflow Report Default Query

**Technical Name:** WorkflowReportDefaultQuery

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

The WorkflowReportDefaultQuery setting determines the default SQL query used to generate custom reports within the Pathlock Cloud GRC platform. It is utilized specifically when routing types for workflows are defined, influencing the content and structure of the reports generated based on specified parameters.

**Business Impact:**

Configuring the WorkflowReportDefaultQuery can significantly affect how an organization monitors and manages workflow processes. A well-defined default query ensures that reports are aligned with the organization's security, risk, and compliance requirements, facilitating better decision-making and enhancing the organization's ability to meet audit and compliance standards.

**Technical Impact when configured:**

Upon configuration, the WorkflowReportDefaultQuery directly influences the effectiveness and relevance of the reports generated for workflow analysis. It allows for the customization of report outputs to include essential information pertinent to the organization's workflow management strategies, thereby optimizing the GRC platform's utility.

**Examples Scenario:**

- An organization may configure the WorkflowReportDefaultQuery to focus on workflows that involve sensitive data access approvals. By tailoring the query, the resultant reports can highlight areas where unauthorized access approvals are attempted, aiding in the enhancement of security measures.

**Related Settings:**

- `AuthorizationReviewShowFillEmptyToApprove`

**Best Practices:** 

- **Configure when:** there is a need for specialized reporting on workflow processes to meet specific compliance, risk management, or audit requirements.
- **Avoid when:** default reporting meets the organization's information needs, or if there is insufficient expertise to customize queries safely without impacting system performance or risking exposure of sensitive information.