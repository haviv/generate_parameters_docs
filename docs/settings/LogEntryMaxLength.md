# Log Entry Max Length

**Technical Name:** LogEntryMaxLength

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Log Entry Max Length parameter controls the maximum length of log entries generated within the Pathlock Cloud GRC platform. This setting ensures log files are manageable in size, aiding in efficient storage and quicker access when reviewing logs for security, risk, or compliance purposes.

**Business Impact:**

Adjusting this parameter can significantly impact audit trails and security monitoring. A too-short log entry might truncate vital information, hindering issue diagnostics and compliance tracking. Conversely, excessively long entries can lead to inflated log sizes, increasing storage costs and complicating log analysis processes.

**Technical Impact: when configured**

Proper configuration of the Log Entry Max Length parameter ensures an optimal balance between detail and manageability of log data. It helps maintain system performance by preventing log bloat and facilitates compliance and security investigations by retaining necessary information without overwhelming detail.

**Examples Scenario:**

- **Security Audit Preparation:** To prepare for an upcoming security audit, an organization sets an appropriate Log Entry Max Length to capture all necessary event details while keeping the logs at a manageable size for auditors.

- **Compliance Requirement:** A company operating under GDPR needs to monitor user access without generating excessively large logs. Adjusting the Log Entry Max Length ensures compliance with data minimization principles.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** 
- **Configure when:** Setting up security monitoring and compliance reporting workflows to ensure that log entries contain sufficient detail for analysis without unnecessarily inflating log file sizes.
- **Avoid when:** There is a requirement to capture extremely detailed log entries for every minor event, which could lead to unmanageably large log files and degrade system performance.