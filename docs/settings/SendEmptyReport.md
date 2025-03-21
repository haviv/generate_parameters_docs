# Send Empty Report

**Technical Name:** SendEmptyReport

**Category:** Reporting

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:** This parameter controls whether empty reports are sent in the context of the 'SendCustomReport' workflow action. An empty report results when the specified criteria do not match any records.

**Business Impact:** Enabling empty reports to be sent ensures that stakeholders are informed even when no actionable data matches the report criteria, maintaining transparency and accountability in monitoring activities.

**Technical Impact when configured:** When enabled, the system will send a report via email even if it contains no data. This can be useful for confirming the absence of specific conditions or issues within the monitored scope.

**Examples Scenario:** If a scheduled report is set to monitor for unusual transactions within a certain threshold and no such transactions occur, enabling SendEmptyReport ensures that the compliance team receives an email notification, confirming no action is required.

**Related Settings:**

- ScheduleReportFileExtention
- SendMailOnStepStarted

**Best Practices:** 

- **configure when:** Regular confirmation is needed that specific checks have been performed, even if no issues were flagged.
  
- **avoid when:** Report recipients prefer only to receive notifications when there are new or actionable items to conserve inbox space and reduce unnecessary communications.