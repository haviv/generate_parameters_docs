# SoD Full Report Run Offline Users Warn Threshold

**Technical Name:** SodFullReportRunOfflineUsersWarnThreshold

**Category:** Compliance

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the threshold for warning administrators when the number of offline users, with Segregation of Duties (SoD) violations in the system, reaches a specified limit. It is designed to enhance the monitoring and management of user compliance with SoD policies within the Pathlock Cloud GRC platform.

**Business Impact:**

Setting an appropriate threshold helps organizations in maintaining compliance by ensuring timely review and action on users who are not currently active but have potential SoD conflicts. It aims to reduce the risk of undetected SoD violations among inactive users, thereby supporting audit readiness and mitigating risk associated with unauthorized access or fraudulent activities.

**Technical Impact when configured:**

- When a defined threshold is reached or exceeded, the system will automatically notify administrators or designated compliance officers.
- Helps in proactive monitoring and resolution of SoD violations among users marked as offline in the system before they become active again.
- Supports maintaining a cleaner user access environment by drawing attention to and facilitating the review of potential SoD violations among inactive users.

**Examples Scenario:**

- An organization sets the *SodFullReportRunOfflineUsersWarnThreshold* to 10. This means when there are 10 or more users who are currently marked as offline but have SoD violations, the system will issue a warning to administrators. This allows compliance officers to review and address these violations proactively, ensuring these users are either cleared of violations or their access adjusted before returning to active status.

**Related Settings:**

**Applicable Workflows Actions:**

**Best Practices:** 
- **Configure when:** You have a large user base and need to ensure compliance across active and inactive users. Setting the threshold according to the organization's size and compliance requirements can help maintain a healthy security posture.
- **Avoid when:** Your organization has a very small user base, making manual monitoring of SoD violations feasible without automated warnings.