# Write Event On Every Report Run

**Technical Name:** WriteEventOnEveryReportRun

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls whether an event should be written to the log every time a report is run in the Pathlock Cloud GRC platform. 

**Business Impact:**

Enabling this feature ensures that administrators have a detailed audit trail of report executions, which is crucial for compliance and monitoring user activities within the system. It assists in tracking who accessed what information and when, significantly enhancing security and compliance postures.

**Technical Impact when configured:**

When enabled, the system will generate and store log entries for each report execution, possibly leading to increased data storage requirements. It also aids in debugging and monitoring report usage patterns.

**Examples Scenario:**

A financial auditing team regularly runs sensitive financial reports to comply with external regulatory requirements. Enabling WriteEventOnEveryReportRun ensures that each report run is logged, creating an audit trail that proves compliance with regulations that mandate strict control and logging of access to financial data.

**Related Settings:** 

- WorkflowRiskMitigatonNameAndDescription
- WorkflowHeaderDirectionLTR
- WorkflowSectionWidth
- WorkflowTypeForProcessVerification

**Best Practices:** configure when you need to audit report executions rigorously, avoid when such detailed logging is not necessary or could lead to excessive data storage.