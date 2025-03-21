# Server Discrepancy Email Template

**Technical Name:** ServerDiscrepancyEmailTemplate

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The Server Discrepancy Email Template parameter is designed for configuring the content and format of email notifications sent by the Pathlock Cloud GRC platform. These notifications are triggered when there is a discrepancy between application servers listed in the ProfileTailor configuration and the actual application servers detected. This is to ensure administrators are promptly informed about potential misconfigurations or unmonitored servers that could affect security, risk, and compliance management processes.

**Business Impact:**

The proper configuration of this parameter directly impacts an organization's ability to quickly respond to and resolve discrepancies between expected and actual server environments. Timely notifications allow for the investigation and remediation of issues that may compromise application security or compliance with regulatory standards.

**Technical Impact when configured:**

- Ensures administrators are immediately aware of any inconsistencies between the configured and detected application servers.
- Facilitates quick response to potential security risks or compliance issues arising from unaccounted servers.
- Supports maintaining the integrity of the governance, risk management, and compliance processes by alerting relevant personnel about discrepancies needing attention.

**Examples Scenario:**

An organization using the Pathlock Cloud GRC platform has recently decommissioned several application servers but forgot to update the ProfileTailor configuration to reflect this change. As a result, the platform detects a discrepancy between the expected servers (as per the outdated ProfileTailor configuration) and the servers actively communicating with the platform. The Server Discrepancy Email Template, once configured, triggers an email notification to the system administrators detailing the discrepancy, enabling them to rectify the ProfileTailor configuration accordingly.

**Related Settings:** 

- SendMailOnApplicationServerDiscrepancies

**Best Practices:** 

- **Configure when:** Immediate notification of discrepancies between configured and detected application servers is essential for maintaining security and compliance.
- **Avoid when:** All application server inventories are up to date, and the risk of discrepancies is negligible. However, periodic review and testing of this configuration are recommended as part of a proactive GRC strategy.