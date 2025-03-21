# Time interval (seconds) between two identical Activities:

**Technical Name:** AuditMinTimeBetweenRequredsInSeconds

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies the minimum duration in seconds that must elapse between two identical audit activities before they are logged again. This helps in reducing noise in the audit logs by preventing the recording of repetitive actions performed in a short time frame.

**Business Impact:**

Configuring this parameter appropriately can greatly enhance the effectiveness of audit logs by filtering out redundant entries. This makes it easier for compliance and security teams to identify significant security events and anomalies amidst the vast amount of audit data, thereby improving the overall security posture and compliance with regulatory requirements.

**Technical Impact when configured:**

When configured, this parameter reduces the size of audit logs, making them more manageable and easier to analyze. It ensures that only significant actions are logged, preventing the database from becoming overwhelmed with redundant data. This also optimizes the performance of the audit logging system by minimizing unnecessary disk I/O and storage consumption.

**Examples Scenario:**

If the `AuditMinTimeBetweenRequredsInSeconds` is set to 60 seconds, and a user performs the same activity (e.g., accessing a specific file or application) multiple times within a minute, only the first action will be recorded in the audit log. Any identical activity within the next 60 seconds will not be logged again.

**Related Settings:**

- AllowMultipleEmergencyAccessRequests

**Best Practices:** configure when auditing activities that occur frequently but do not require immediate attention for every occurrence; avoid when every instance of specific activities needs to be recorded for compliance or security reasons.