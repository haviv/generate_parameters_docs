# Report Approval Global Scope

**Technical Name:** ReportApprovalGlobalScope

**Category:** Reporting

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter controls whether report approvals are scoped globally across the Pathlock platform. It affects the visibility and management of approved reports, ensuring that the appropriate level of oversight is applied to sensitive or critical reports within the GRC (Governance, Risk Management, and Compliance) framework.

**Business Impact:**

Enabling a global scope for report approvals can significantly impact an organization's ability to manage and mitigate risks. It ensures that only authorized reports are accessible, reducing the risk of unauthorized data access and ensuring compliance with internal and external regulations. This centralized control mechanism supports a stronger governance structure by enforcing consistent approval processes across the organization.

**Technical Impact when configured:**

- Ensures that report approval processes are consistently enforced across all reports and users within the Pathlock platform.
- Provides a centralized overview of report approval status, facilitating easier audit and compliance processes.
- Enhances security by limiting report access to only those with proper approval, reducing the risk of sensitive information exposure.

**Examples Scenario:**

An organization requires all financial reports to be reviewed and approved by senior management before they are distributed to stakeholders. By enabling the ReportApprovalGlobalScope parameter, the organization can ensure that this approval process is applied globally across all financial reports generated within the Pathlock platform, reducing the risk of unauthorized or premature report distribution.

**Related Settings:** 

- `ShowAdvancedUserGroupFilterSelection`

**Best Practices:** 

- **configure when**: There is a need for a consistent and secure report approval process across various departments and reports within the organization.
- **avoid when**: Individual departments or groups require flexibility in managing their own report approval processes independent of a global standard.