# Active Directory File Monitoring Ignored Extensions

**Technical Name:** ActiveDirectoryFileMonitoringIgnoredExtensions

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter specifies file extensions that are to be ignored during the monitoring of Active Directory share folder activities. It is used to filter out file types that do not require surveillance or auditing, helping to streamline the monitoring process and focus on relevant data.

**Business Impact:**

Ignoring specific file extensions can significantly reduce the noise in monitoring logs, making it easier to identify unauthorized access or modifications to sensitive files. It helps organizations maintain a high level of security and compliance by ensuring that only significant activities are logged and reviewed.

**Technical Impact when configured:**

When configured, this parameter will exclude files with specified extensions from being monitored. This means that activities such as creation, modification, or deletion of these files in monitored directories will not be logged or trigger alarms. It can improve system performance and reduce the volume of audit logs by excluding file types deemed irrelevant or not sensitive.

**Examples Scenario:**

For instance, an organization might decide to exclude image file types (e.g., .jpg, .png) from being monitored in their Active Directory share folders because these are not considered sensitive. This exclusion allows the organization to focus on monitoring changes to document files (e.g., .docx, .pdf), which are more likely to contain confidential information.

**Related Settings:**

- MonitoredDirectory
- TransactionForUser

**Applicable Workflows Actions:** 

**Best Practices:** configure when, avoid when 

- **Configure when:** It's essential to neglect non-sensitive or less critical file types from monitoring to optimize performance and focus on high-risk extensions.
- **Avoid when:** All file types within a monitored directory are considered sensitive or critical, requiring comprehensive auditing for security or compliance.