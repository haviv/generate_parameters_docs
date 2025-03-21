# Disable Approval Of Authorization Set Reports

**Technical Name:** DisableApprovalOfAuthorizationSetReports

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the approval of authorization set reports within the Pathlock Cloud GRC platform is disabled. When set to true, any attempts to approve authorization set reports will be blocked, enhancing control over the report approval process.

**Business Impact:**

Enabling this setting may impact operational workflows by introducing an additional layer of control over the authorization report approval process. It ensures that sensitive or critical changes in authorization data are reviewed and approved by designated personnel, reducing the risk of unauthorized access or compliance issues.

**Technical Impact when configured:**

- Prevents the automatic or unintended approval of authorization set reports.
- Increases oversight and accountability in the change management process for authorizations and roles.
- Requires manual intervention for report approval, potentially increasing the time to finalize authorization changes.

**Example Scenario:**

Consider a scenario where a company is undergoing a compliance audit and needs to ensure that any changes to roles and authorizations within their GRC platform are thoroughly reviewed and approved by a compliance officer. By enabling DisableApprovalOfAuthorizationSetReports, the company can prevent automatic approvals, ensuring that each report is manually checked for compliance before it is approved.

**Related Settings:**

- AuthorizationReviewDisableOverviewTabs

**Best Practices:** configure when sensitive or critical changes to authorizations are involved to ensure they are reviewed and approved by the appropriate personnel. Avoid when the approval process needs to be swift and does not require an additional layer of scrutiny.