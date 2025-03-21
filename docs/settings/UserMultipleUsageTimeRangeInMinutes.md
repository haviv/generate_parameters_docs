# User Multiple Usage Time Range In Minutes

**Technical Name:** UserMultipleUsageTimeRangeInMinutes

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:**

This configuration parameter defines the time range, in minutes, for detecting multiple usage instances of a single user account. It's utilized to identify potential security risks associated with concurrent or near-simultaneous sessions that could indicate shared credentials or unauthorized access.

**Business Impact:**

Setting an appropriate time range helps in mitigating risks related to account sharing or compromised credentials by alerting administrators to unusual activity patterns. It is crucial for maintaining the integrity of user accounts and ensuring compliance with security policies that prohibit the sharing of access credentials.

**Technical Impact when configured:**

Once configured, the system monitors user activities within the specified time range to identify and report instances where a single user account appears to be accessed multiple times. This can indicate potential security breaches or policy violations, triggering further investigation.

**Example Scenario:**

A company has set the "User Multiple Usage Time Range In Minutes" to 30 minutes. If a user's credentials are used to log in from two different IP addresses within this timeframe, the system flags this activity for review. This helps identify potential unauthorized access or credential sharing.

**Related Settings:**

- `Duration_Days`
- `TimeOutErrorPage`

**Best Practices:** 

- **Configure when:** there's a need to tighten security measures around user account access, especially in environments where confidentiality and data integrity are paramount.
- **Avoid when:** the setting might generate too many false positives in environments where rapid switching between workstations is normal and expected behavior.