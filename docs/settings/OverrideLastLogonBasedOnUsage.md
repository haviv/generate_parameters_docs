# Override Last Logon Based On Usage

**Technical Name:** OverrideLastLogonBasedOnUsage

**Category:** Audit

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The parameter 'OverrideLastLogonBasedOnUsage' is designed to calculate and potentially adjust the last logon timestamp for users within the system based on actual usage data. This is particularly relevant in scenarios where accurate tracking of user activity and logon data is crucial for audit, security, and compliance purposes.

**Business Impact:**

The ability to override last logon information based on actual usage can significantly improve the accuracy of audit reports, enhance the detection of possible security incidents, and ensure compliance with regulatory requirements regarding user activity monitoring.

**Technical Impact when configured:**

When configured, this feature recalculates the last logon timestamp for each user by examining the maximum timestamp of their activities. This helps in identifying the most accurate last access time, which may be different from what the system automatically logs as the 'last logon'. This can be especially useful in environments where user activities do not necessarily correspond to the traditional logon events captured by the system.

**Examples Scenario:**

- In a scenario where an organization needs to comply with stringent audit requirements that necessitate accurate tracking of user logon times, 'OverrideLastLogonBasedOnUsage' can be used to refine these timestamps based on actual data usage.
- For security purposes, it can help in quickly identifying any discrepancies between reported last logon times and actual usage patterns, aiding in the detection of unauthorized access.

**Related Settings:** N/A

**Best Practices:** 

- **Configure when:**
    - Accurate user activity tracking is required for compliance reasons.
    - There is a need to enhance security monitoring and the identification of anomaly access patterns.
    
- **Avoid when:**
    - There is minimal requirement for precise tracking of user logon times, and the overhead of recalculating this information based on usage data is not justified.