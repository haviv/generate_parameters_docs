# Enable Report Trace

**Technical Name:** EnableReportTrace

**Category:** Reporting

**Default Value:** False

**Impact Level:** Medium

**Description:**

The Enable Report Trace parameter is a configurable setting designed to enhance the debugging and monitoring capabilities of report generation within the Pathlock GRC platform. When activated, this feature allows for the detailed tracing of report execution processes, helping in identifying performance bottlenecks or errors that may occur during the report generation phase.

**Business Impact:**

Activating the Enable Report Trace feature can significantly aid in understanding the intricate workings of report generation and execution. For businesses, this means improved reliability and efficiency in the reporting process, as any issues can be quickly identified and addressed. However, it's important to manage this feature carefully, as excessive tracing might impact performance.

**Technical Impact when configured:**

When the Enable Report Trace setting is enabled, the system will start to log detailed information regarding the report generation process. This includes the start time, end time, duration, and any errors or warnings encountered during the process. This detailed logging helps in pinpointing the exact step where issues may have occurred, thereby facilitating a quicker resolution.

**Examples Scenario:**

A compliance officer runs a complex report to identify risks across multiple departments. The report unexpectedly takes longer than usual to complete, and the generated output is incomplete. By enabling the Enable Report Trace parameter, IT support can trace the report generation process, identify that a specific query is causing a timeout due to an inefficient database index, and rectify the issue, resulting in reports running smoothly thereafter.

**Related Settings:**

- UseSapQueryAsRoles

**Best Practices:** 

- **Configure when:** Detailed analysis of the report generation process is required, especially when diagnosing issues related to performance or errors in report content.
- **Avoid when:** The system is under heavy load or in a production environment where performance is critical, unless absolutely necessary for troubleshooting purposes.