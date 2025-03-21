# Enable Portal For Deleted Users

**Technical Name:** EnablePortalForDeletedUsers

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether users who have been deleted from the system can still access the portal. By default, once a user is removed, they lose access to the portal. Enabling this parameter allows for a grace period or specific business scenarios where a deleted user's access is temporarily necessary.

**Business Impact:**

Enabling this feature can be critical in scenarios where users are removed from the active directory or user database but need to retain access to the portal for a transitional period. This could be for completing pending tasks, accessing historical reports, or facilitating a smoother turnover process. However, it poses a risk if not managed correctly, as it could potentially allow unauthorized access.

**Technical Impact when configured:**

When configured to `true`, the system will permit access to the portal for users marked as deleted. This behavior overrides the default security measures that prevent deleted users from accessing the portal, requiring careful consideration and monitoring.

**Examples Scenario:**

- A employee has been terminated, but they need access to the portal for an additional week to complete handover documentation.
- A consultant's contract ends, and their user account is deleted, but they require portal access for a short period to finalize their reports.

**Related Settings:** Not applicable

**Best Practices:** configure when, avoid when 

- Configure this setting to `true` in scenarios where there is a clear, temporary need for a deleted user to access the portal. Ensure that there are stringent processes in place to review and revoke this access in a timely manner.
- Avoid enabling this setting as a default practice. Keep it set to `false` to maintain strict access control and security, only enabling on a case-by-case basis with appropriate oversight.