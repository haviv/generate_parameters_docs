# Authorization Review Wide Approval Show System

**Technical Name:** AuthorizationReviewWideApproval_ShowSystem

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls the visibility and functionality of wide approval mechanisms within authorization review processes in the Pathlock Cloud GRC platform, particularly focusing on system and departmental level approvals.

**Business Impact:**

Enabling this parameter streamlines the authorization review process by allowing bulk approvals at the system or department level, thereby reducing administrative overhead and time to compliance. It impacts the efficiency and speed with which organizations can manage and review large volumes of authorization data.

**Technical Impact when configured:**

When enabled, users involved in the authorization certification process can perform wide approvals, affecting multiple items or users at once, based on predefined criteria. This setting also influences how departmental-level data visibility and approval actions are displayed within the authorization review UI.

**Examples Scenario:**

- In situations where a department head needs to approve all pending authorizations for their department before an audit deadline, enabling this setting allows for a more efficient review process.
  
- When a system-wide policy change requires mass approval or review, this parameter allows authorized users to perform such actions without the need to individually review each case.

**Related Settings:**

- AuthorizationReviewWideApproval_ShowDeptLevel4
- AuthorizationReviewWideApproval_ShowDeptLevel5

**Best Practices:** 

- **configure when:** Large scale authorization reviews are common, and there is a need for efficient, bulk processing capabilities to manage department or system-wide approvals.

- **avoid when:** Authorization reviews require a high degree of granularity, and individual case assessment is preferred to maintain control and oversight over the approval processes.