**Emergency Access Report Include Workflow Actions**

**Technical Name:** EmergencyAccessReportIncludeWorkflowActions

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether workflow actions related to emergency access are included in the Emergency Access Activity Report. It determines the inclusion of detailed actions taken during the emergency access period, thereby providing a comprehensive view of activities within the emergency access scenario.

**Business Impact:**

Including workflow actions in the emergency access report enhances the auditability and traceability of emergency accesses, allowing organizations to closely monitor and analyze the actions taken under emergency permissions. This capability supports stronger compliance practices by ensuring that all emergency actions are accounted for and reviewed.

**Technical Impact when configured:**

When enabled, the Emergency Access Activity Report will include all associated workflow actions, such as approvals or revocations that occurred during the emergency access period. This provides administrators and auditors with a detailed log of activities for review, enhancing security and compliance oversight.

**Examples Scenario:**

- **Audit Preparation:** To prepare for an audit, an organization enables this parameter to ensure that the Emergency Access Activity Report contains all necessary workflow actions. This action ensures auditors can easily verify that all emergency accesses were appropriately managed and actions were taken according to policy.
  
- **Security Review:** After noticing unusual activity, a security team enables this parameter to review detailed actions taken during emergency access periods. This allows the team to pinpoint potentially unauthorized or inappropriate actions taken under the guise of emergency access.

**Related Settings:**

- CustomDomains

**Best Practices:** configure when auditing requirements necessitate a detailed log of emergency access actions; avoid when minimal reporting suffices for organization needs.