# Report Filter Use Wide Role Filter

**Technical Name:** ReportFilterUseWideRoleFilter

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether a wide or narrow filter scope is applied when generating reports related to user roles within the Pathlock Cloud GRC platform. When enabled, the filter broadens the search scope, potentially including a wider array of user roles in the report.

**Business Impact:**

Enabling this parameter can significantly affect the comprehensiveness of reports, impacting decisions on access control and compliance monitoring. It aids in gaining a broader understanding of role assignments and potential security risks, which is vital for regulatory compliance and internal audits.

**Technical Impact when configured:**

When the parameter is set to true, reports will include an expanded set of user roles, potentially uncovering hidden risks or misconfigurations that a narrow filter might miss. This could also affect performance due to the broader data set being processed.

**Examples Scenario:**

A compliance officer needs to generate a report on all user roles across the system to audit access controls and review for separation of duties (SoD) violations. By enabling this parameter, the report includes a comprehensive list of roles, ensuring no role is overlooked during the audit.

**Related Settings:** 

- ReportFilterUseWideUserFilter

**Best Practices:** configure when needing comprehensive reports that cover all aspects of user roles within the system; avoid when reports only need to focus on specific, narrow criteria as it may unnecessarily broaden the report scope and impact report generation performance.