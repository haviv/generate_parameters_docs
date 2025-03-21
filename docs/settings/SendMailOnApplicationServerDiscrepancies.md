# Notify about application servers discrepancy:

**Technical Name:** SendMailOnApplicationServerDiscrepancies

**Category:** Configuration

**Default Value:** (The default value was not provided in the code references)

**Impact Level:** Medium

**Description:**

Enables the system to notify administrators via email when there is a discrepancy between the application servers defined in Profile Tailor and the actual active servers monitored by Pathlock.

**Business Impact:**

Ensuring that all application servers are correctly monitored is crucial for maintaining the integrity and security of the enterprise environment. Discrepancies may indicate configuration issues or unauthorized changes, potentially leading to security risks and compliance issues.

**Technical Impact when configured:**

When this setting is enabled, it actively monitors the alignment between configured application servers and those actively communicating with the Pathlock platform. Any discrepancies trigger an automatic email notification to the designated administrators, allowing for quick identification and resolution of sync issues or unauthorized modifications.

**Example Scenario:**

A company’s IT department defines three application servers in Profile Tailor for monitoring. If one of these servers goes offline or a new, unregistered server begins communication with Pathlock, an email alert is triggered. This facilitates immediate investigation and resolution, enhancing security and operational integrity.

**Related Settings:**

- ScheduleMailWithReport
- ScheduleMailWithoutReport

**Best Practices:** 

- Configure this setting to ensure continuous monitoring and real-time alerts for discrepancies in application server configurations.
- Avoid enabling this feature without first establishing a protocol for responding to alerts, to prevent oversight of critical notifications.