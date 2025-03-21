# Delete Log Files

**Technical Name:** DeleteLogFiles

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `DeleteLogFiles` parameter controls whether system log files are to be deleted after they have been processed. It is applicable in scenarios where log data is extracted, reviewed, or monitored, and then the physical log files are no longer needed for operational or compliance purposes.

**Business Impact:**

Enabling this parameter can significantly reduce storage requirements on servers by ensuring that only current and relevant log files are retained. For organizations dealing with large volumes of log data, this can result in cost savings and improved system performance. However, care must be taken to ensure that log data required for audit, legal, or compliance purposes has been securely archived before deletion.

**Technical Impact when configured:**

- Reduction in disk space usage on servers.
- Potentially faster system performance due to less disk I/O operations.
- Reduced time and resources required for manual log file management.

**Examples Scenario:**

For an organization undergoing a security compliance audit, it's critical to maintain access logs for a minimum period as defined by regulatory requirements. The `DeleteLogFiles` parameter should be configured to retain log files for the necessary duration and only delete them post the regulatory retention period, ensuring compliance with audit requirements without manual intervention.

**Related Settings:** N/A

**Best Practices:** configure when
- Log files have been securely backed up or are no longer needed.
- Disk space on the server hosting log files is limited.

avoid when
- Compliance or internal policies require log files to be retained for a specific duration.
- Log files have not yet been reviewed or analyzed for security incidents.