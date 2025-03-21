# Schedule Report Body Empty Report

**Technical Name:** ScheduleReportBodyEmptyReport

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter determines the behavior of scheduled report deliveries when the report generates no data. It controls whether an empty report should still be emailed to recipients or if the delivery should be skipped altogether in the event of an empty report.

**Business Impact:** Ensuring that recipients are not overwhelmed with unnecessary emails when reports contain no data improves the efficiency of communication and focuses attention on reports that do contain valuable information. This can be particularly useful in monitoring compliance or security incidents where no news can be good news.

**Technical Impact when configured:** When enabled, it can significantly reduce the number of emails sent to users, declutters their inbox, and ensures that only actionable reports are delivered. When disabled, users might receive more emails, but will be notified even when there's no data, ensuring they are aware a report was generated but contained no findings.

**Examples Scenario:** If configured to skip sending empty reports, a scheduled compliance report that runs after business hours will only be delivered to the compliance team's inbox if there are non-compliance issues detected. This helps the team to immediately focus on addressing any issues reported without having to sift through emails with empty reports.

**Related Settings:** ScheduleReportHeader

**Best Practices:** 
- **Configure when** you want to streamline communication and ensure that users are only notified when there are significant findings in a report. This is particularly effective for reports that are intended to alert users about exceptions or issues that need attention.
- **Avoid when** it is critical to show that the reports are running as expected, even if there are no findings. Some stakeholders may require a report to confirm the absence of issues within a specific reporting period.