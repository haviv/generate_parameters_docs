# Time Slice In Hours For Read Log

**Technical Name:** TimeSliceInHoursForReadLog

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

The `TimeSliceInHoursForReadLog` parameter defines the time segment in hours for processing audit logs in the Pathlock Cloud GRC environment. It dictates how audit logs are partitioned and read during analysis and reporting, enhancing performance and manageability for system administrators and compliance officers.

**Business Impact:**

Configuring this parameter optimally ensures efficient log processing, leading to better system performance, quicker compliance reporting, and more timely risk identification. An inadequately configured time slice could result in delayed log processing and reduced system performance, affecting timely compliance and risk assessments.

**Technical Impact when configured:**

When configured, this setting optimizes the system's ability to process and analyze large volumes of audit logs by dividing them into manageable time-segmented blocks. This division helps in prioritizing log analysis, improving the system's responsiveness, and reducing the load on system resources during log processing.

**Example Scenario:**

Consider an organization needs to review and report on security events recorded in the audit logs for compliance purposes. By setting `TimeSliceInHoursForReadLog` to an optimal value, the system can efficiently process logs in segments, enabling quicker access to relevant audit information for reporting and analysis, and thus meeting compliance deadlines.

**Related Settings:**

- SystemStoppedBody
- SystemStoppedSubject

**Best Practices:** 

- **Configure when:** You have large volumes of audit logs that need to be processed and analyzed. Adjust the time slice to ensure logs are processed efficiently without overwhelming system resources.
- **Avoid when:** If the volume of audit logs is minimal or the system is dedicated to log processing, a larger time slice might be more efficient as it reduces the number of processing cycles.