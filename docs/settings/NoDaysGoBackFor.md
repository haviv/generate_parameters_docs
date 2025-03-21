# Number of days back to check if a computer was used by more than one user

**Technical Name:** NoDaysGoBackFor

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the number of days to retrospectively analyze computer usage to identify if a device has been accessed by multiple users. It is utilized to enhance security measures by flagging shared use of a single workstation, which could indicate non-compliance with certain security policies.

**Business Impact:**

Enabling this feature helps organizations maintain tighter security controls and supports compliance with internal policies or regulatory requirements that discourage or prohibit the sharing of workstations. Identifying shared use can also aid in forensic investigations or in detecting unauthorized access within a certain look-back period.

**Technical Impact when configured:**

When configured, this parameter triggers an analysis process within the Pathlock Cloud GRC platform, scanning for instances where a single computer has been accessed by more than one user within the specified time frame. Recommendations or alerts can be generated based on this analysis to inform IT security teams of potential security risks or to enforce user access policies.

**Examples Scenario:**

If the parameter is set to "30" days, the system will audit all computers to determine if any have been used by multiple users within the last 30 days. This information could be essential for auditing purposes or to ensure that shared computers are only used in permitted scenarios, such as shared workstations in a hospital.

**Related Settings:**

- NewPasswordRule_MaximumPasswordDays
- IsTranslateMail
- NewUserAccountHeader

**Best Practices:** configure when, avoid when

- **Configure when:** an organization has strict policies regarding workstation sharing, or in environments where the risk of unauthorized access is high. Regularly reviewing and adjusting this parameter based on current security policies or compliance requirements is advisable.
- **Avoid when:** Workstations are intended to be shared as part of regular business operations, and such sharing does not pose a security risk. In environments where workstation sharing is essential and monitored through other means, setting this parameter may generate unnecessary alerts.