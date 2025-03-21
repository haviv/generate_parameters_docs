# Delete Old Manager From Approval Groups

**Technical Name:** DeleteOldManagerFromApprovalGroups

**Category:** User Management

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter is designed to manage the transition of managerial responsibilities within organizational unit approval groups. When a manager is changed, this setting dictates whether the previous manager's permissions and roles within approval groups are automatically revoked, ensuring that only the current manager has the appropriate access.

**Business Impact:**

Implementing this parameter can significantly enhance the security and integrity of the approval process by preventing outdated access permissions. It ensures that only the current managers have the right to approve or deny requests, aligning with best practices for access control and reducing the risk of unauthorized or inappropriate approvals.

**Technical Impact when configured:**

Upon activation, the system will automatically remove the previous manager's access to approval groups associated with their former position. This action is critical for maintaining accurate and secure management tiers within the company's organizational structure. It directly impacts workflow continuity and operational efficiency by ensuring that the appropriate managerial level reviews all approvals.

**Examples Scenario:**

- A department head is promoted or leaves the company, and their successor is appointed. Activating this parameter ensures that the outgoing manager's access to approve departmental requests is revoked and transferred to the new manager, streamlining the transition and maintaining secure operations.

**Related Settings:** Not specified

**Best Practices:** Configure this parameter during managerial transition periods to maintain security and operational integrity within approval workflows. Avoid leaving the parameter disabled as it could lead to security lapses and unauthorized access to critical approval processes.