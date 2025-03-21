# Send Workflow Admin Mail Template To Fallback Approval Group

**Technical Name:** SendWorkflowAdminMailTemplateToFallbackApprovalGroup

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**
This parameter specifies whether to send workflow administration mail templates to a defined fallback approval group if the primary recipient(s) are unavailable or cannot be determined. When configured, it helps ensure that workflow notifications and approvals do not stall due to the absence of the primary approver, by routing these communications to an alternate group designed to handle such scenarios.

**Business Impact:**
Enabling this parameter ensures that the workflow process remains fluid, preventing delays in approvals or notifications that could lead to compliance risks, missed deadlines, or operational inefficiencies. It is particularly valuable in maintaining continuous governance, risk management, and compliance (GRC) processes within the Pathlock platform.

**Technical Impact when configured:**
When this parameter is configured, the system automatically redirects email notifications intended for the primary recipient to the fallback approval group's email addresses. This action is taken if the primary recipient is not available (determined by their absence in the system or other predefined criteria). It requires proper setup of the fallback group in the system and association of relevant user emails.

**Examples Scenario:**
In a scenario where a critical compliance approval is needed for a financial transaction within the Pathlock platform, and the primary approver is out of office without access, this parameter ensures that the approval request is sent to the fallback approval group. This group, having been predefined, can review and act on the request promptly, preventing any delays in the transaction that could affect compliance status or operational efficiency.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when:** There is a need for redundancy in workflow notifications and approvals, particularly in critical workflows involving compliance, risk management, or security tasks.
- **Avoid when:** All workflow steps are non-critical, or there is certainty that appointed approvers will always be available to respond to notifications and approvals.