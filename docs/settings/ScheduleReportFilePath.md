# Schedule Report File Path

**Technical Name:** ScheduleReportFilePath

**Category:** Reporting

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `ScheduleReportFilePath` parameter specifies the default file path used for saving the output files of scheduled reports within the Pathlock Cloud GRC platform. It is accessed within the notification utility to generate and save reports based on predefined schedules.

**Business Impact:**

Configuring the `ScheduleReportFilePath` correctly ensures that generated reports are saved in an appropriate, secure, and accessible location. This aids in effective risk management, compliance auditing, and maintaining the integrity of security policies by allowing timely access to critical reports.

**Technical Impact when configured:**

- Ensures scheduled reports are consistently saved to a reliable path.
- Facilitates the automation process by eliminating the need for manual file path configuration for each report.
- Enhances the system's manageability and the efficiency of data retrieval for compliance and audit purposes.

**Examples Scenario:**

An organization schedules weekly risk assessment reports to monitor potential vulnerabilities. By setting the `ScheduleReportFilePath` to a designated secure server folder, these reports are automatically saved in the correct location, where they can be easily accessed by the compliance team for timely risk analysis and reporting.

**Related Settings:** Not specified

**Best Practices:** 

- Configure the `ScheduleReportFilePath` to a secure, backed-up location to prevent data loss.
- Avoid using shared or public folders to ensure the confidentiality and integrity of the reports.