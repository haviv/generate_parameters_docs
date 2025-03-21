# Show Message On System Change

**Technical Name:** ShowMessageOnSystemChange

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter controls whether a notification message is displayed to the user when there are changes detected within the system's configuration or state. This could relate to updates in settings, security policies, or other relevant system modifications that users should be aware of.

**Business Impact:**

Enabling this feature ensures users are immediately informed about changes within the system that may affect their workflow or require their attention for compliance reasons. It aids in maintaining awareness and promoting immediate action when necessary, thus supporting overall system integrity and security posture.

**Technical Impact when configured:**

When configured, this parameter actively monitors for system changes and triggers notifications to users. This could potentially increase system resource usage due to the real-time monitoring aspect, but it significantly enhances transparency and responsiveness to system changes.

**Examples Scenario:**

- **Security Update Notification:** In the event of a security policy update or modification, users are notified of the changes and their implications, prompting them to adjust their practices accordingly.
- **Workflow Adjustments:** If a workflow or system configuration is altered, relevant users receive a notification to review the changes and understand how their operations are affected.

**Related Settings:**

- ShowLastLogonColumn: Indicates whether the "Last Logon" column is displayed in reports, which could be part of the system change notifications if user access patterns are relevant to the change being notified.

**Best Practices:** 

- **Configure when:** Immediate user notification is critical for maintaining operational integrity, compliance, and security. Especially effective in environments with dynamic changes.
- **Avoid when:** The system is relatively stable with infrequent changes, or if constant notifications could overwhelm the users, detracting from their main tasks.