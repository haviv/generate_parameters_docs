# Authorization Review Disable Wide Approval Filter

**Technical Name:** AuthorizationReviewDisableWideApprovalFilter

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The Authorization Review Disable Wide Approval Filter parameter is designed to manage the scope of user approvals in authorization reviews within the Pathlock Cloud GRC platform. Enabling this parameter restricts the approval process to a narrower set of criteria, potentially limiting the visibility of certain items that would otherwise require approval.

**Business Impact:**

Enabling this parameter can streamline the approval process during authorization reviews by excluding broader criteria that might unnecessarily complicate or extend the review process. This can lead to a more focused and efficient review, aiding organizations in maintaining compliance while focusing on critical security and risk management tasks.

**Technical Impact when configured:**

When this parameter is set to true, it filters out wider approval requirements during the authorization review process. This change can decrease the number of items requiring review, focusing the approval process on more specific or critical items. It may also impact the workflow by potentially reducing the workload on approvers and speeding up the review cycles.

**Examples Scenario:**

Consider an organization undergoing a periodic review of user roles and access rights within its ERP system. Normally, the review would include a wide array of roles and permissions, requiring extensive scrutiny from multiple department heads. However, by enabling the Authorization Review Disable Wide Approval Filter, the review can be tailored to focus on critical roles and permissions, streamlining the process and reducing the time taken to complete the review.

**Related Settings:** 

N/A

**Best Practices:** 

- **Configure when:** You are seeking to streamline the approval process during authorization reviews by focusing on specific, critical items rather than reviewing a wide array of permissions and roles.
  
- **Avoid when:** The organization requires a thorough review of all roles and permissions, especially in highly regulated industries where comprehensive oversight is necessary.