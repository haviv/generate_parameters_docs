# Time Period Interval

**Technical Name:** TimePeriodInterval

**Category:** Reporting

**Default Value:** None specified

**Impact Level:** Medium

**Description:**

The Time Period Interval parameter is utilized to specify the duration or interval between assessments or audits within the Pathlock GRC platform. It defines how often certain metrics or usage statistics are collected and reviewed for compliance, risk management, or security purposes.

**Business Impact:**

Adjusting the Time Period Interval can significantly affect how timely and effective an organization is in identifying and mitigating risks, ensuring compliance, and maintaining security standards. A well-configured interval ensures that data is collected sufficiently frequently to be actionable but not so often as to be burdensome.

**Technical Impact when configured:**

When configured, this parameter dictates the intervals at which automated processes collect and analyze data. This can influence the system's performance, the relevance of reporting, and the workload for staff involved in review processes.

**Examples Scenario:**

For instance, setting a Time Period Interval to "Weekly" would mean that the system gathers usage statistics, audit trails, or compliance metrics on a weekly basis. This could be crucial for industries requiring timely compliance checks or for high-risk environments where frequent reviews are essential to maintaining security integrity.

**Related Settings:** 

- TakeUsageSinceLastRecord
- TakeMailFromEmployeeRecord

**Best Practices:** configure when data needs to be closely monitored on a regular or frequent basis, avoid when the system or processes do not change frequently enough to necessitate short intervals between reviews.