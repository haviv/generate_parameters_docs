**Technical Name:** ActiveDirectoryDirectoryMonitoringIgnoredPatterns

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Active Directory Directory Monitoring Ignored Patterns parameter specifies patterns in directory names or paths that should be ignored by the Pathlock Cloud GRC platform during Active Directory monitoring processes. This is aimed at optimizing the monitoring by excluding directories that do not require surveillance based on organizational policies or that are known to produce irrelevant security, compliance, or risk notifications.

**Business Impact:**

Configuring this parameter correctly ensures that the organization's monitoring resources are focused on relevant directories, helping to reduce noise from unnecessary alerts and improving the efficiency of security, compliance, and risk management processes.

**Technical Impact when configured:**

- Improved performance of the Active Directory connector by avoiding unnecessary scanning of directories that match the ignored patterns.
- Reduction in the volume of irrelevant alerts and notifications, allowing security teams to focus on genuine issues.
- Enables customization of monitoring to suit the specific needs and policies of the organization.

**Examples Scenario:**

- Ignoring temporary directories such as `/temp/` or `/cache/` in Active Directory, which are frequently modified and do not contain sensitive information, thus reducing unnecessary monitoring traffic.
- Excluding directories known to be used for non-sensitive purposes, such as `/public/` or `/media/`, to focus security efforts on more critical areas.

**Related Settings:**

- `EnableDirectoryMonitoringActiveDirectoryMonitoring`

**Best Practices:** 

- **configure when** you want to optimize Active Directory monitoring by excluding non-essential or known safe directories from the monitoring scope to improve performance and focus.
- **avoid when** all directories within the Active Directory need to be monitored for security, compliance, or risk management purposes without exception.