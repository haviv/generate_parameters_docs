# Show Lock Time

**Technical Name:** ShowLockTime

**Category:** Configuration

**Default Value:** True

**Impact Level:** Low

**Description:** 

Enables the display of system lock times within the application interface. When activated, this feature provides visibility into the specific times at which system access locks are engaged or disengaged, offering a clearer understanding of access restrictions within the system.

**Business Impact:**

The activation of this parameter can aid in audit and compliance processes by offering definitive timestamps for when particular security measures were enabled or disabled. It supports transparency in access management and can contribute to identifying potentially irregular or unauthorized access patterns.

**Technical Impact when configured:**

When enabled, this setting impacts the system's user interface by displaying the lock times directly to the user. It requires no additional resources or significant changes in system performance. It merely alters the visibility of certain data points within the system to enhance user awareness and control over security protocols.

**Examples Scenario:**

- **Audit Preparation:** Ahead of an internal or external audit, an organization might enable Show Lock Time to provide auditors with clear evidence of when access controls were in effect.
  
- **Security Review:** During a periodic security review, enabling this feature could help identify gaps in security posture by showing periods where access controls were not enforced.

**Related Settings:** 

- `UserInformationUrl`
- `UserMultipleUsageTimeRangeInMinutes`
- `WorkflowAdmin`

**Best Practices:** configure when visibility into system lock operations is required for security audits or to enhance understanding and oversight of access controls. Avoid when such visibility is considered unnecessary or could clutter the user interface with extraneous information.