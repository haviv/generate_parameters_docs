**Technical Name:** EmergencyAccessLogTimeThresholdInMinutes

**Category:** Security

**Default Value:** N/A

**Impact Level:** High

**Description:**

This parameter specifies the time threshold in minutes for logging Emergency Access activities within the Pathlock Cloud GRC platform. It’s used to determine the time frame for which emergency access activities are monitored and logged, providing insight into the emergency access granted to users and ensuring that such access is timely and appropriately used.

**Business Impact:**

Setting an appropriate threshold for the Emergency Access Log Time Threshold is crucial for maintaining security protocols within an organization. It helps in identifying potential security breaches or misuses of emergency access privileges by keeping a time-bound record of when such access was granted and used. This ensures that emergency access is not abused and helps in audit trails and compliance reporting.

**Technical Impact when configured:**

When configured, this parameter actively controls the logging and monitoring of emergency access activities, aiding in security and compliance efforts. It serves as a critical metric for audit trails, allowing organizations to have a detailed insight into the usage patterns of emergency access and ensuring these actions remain aligned with security policies.

**Examples Scenario:**

Imagine a scenario where an organization grants emergency access to a user for a critical system due to an abrupt system failure. The EmergencyAccessLogTimeThresholdInMinutes is set to 60 minutes. Any activity performed under this emergency access is logged for an hour from the time of access grant. This helps in reviewing the necessity and appropriateness of the access, along with ensuring that the emergency privileges are revoked once the critical situation is resolved.

**Related Settings:** N/A

**Best Practices:** Configure when establishing or reviewing emergency access policies to ensure timely and appropriate use of such privileges. Avoid setting this threshold too high as it might delay the detection of potential misuse of emergency access rights. Conversely, setting the threshold too low might not accurately capture all necessary activities performed under emergency access, so a balanced approach based on the criticality of accessible systems and typical duration of emergency situations is recommended.