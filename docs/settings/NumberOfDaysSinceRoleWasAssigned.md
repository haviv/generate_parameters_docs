# Number Of Days Since Role Was Assigned

**Technical Name:** NumberOfDaysSinceRoleWasAssigned

**Category:** Audit

**Default Value:**

**Impact Level:** Medium

**Description:**

The "Number Of Days Since Role Was Assigned" parameter is utilized within the Pathlock Cloud GRC platform to track the duration (in days) since a user role was last assigned within a system. This information is critical for auditing purposes, allowing organizations to identify roles that may no longer be required or are potentially outdated.

**Business Impact:**

Understanding how long roles have been assigned to users helps in compliance and security management by ensuring that only relevant and necessary access is maintained. This minimizes the risk of security breaches and ensures compliance with regulatory standards that mandate regular review and justification of access rights.

**Technical Impact when configured:**

Once this parameter is configured, the system can automatically flag roles that have been assigned for periods exceeding the defined threshold. This facilitates proactive security and compliance audits, assisting in the timely review and revocation of roles that may no longer be necessary or pose a risk if left unchecked.

**Examples Scenario:**

A company has a policy that user access should be reviewed and justified at least once every year. By setting the "Number Of Days Since Role Was Assigned" parameter to 365, the system can automatically identify any roles that have not been reassessed within this timeframe, thus helping to maintain strict access controls and compliance with internal policies.

**Related Settings:** 

**Best Practices:** Configure when roles within your organization require regular review and auditing for compliance and security purposes. Avoid configuring this parameter in an environment where role assignments are static and do not change frequently, as it may not add value and could lead to unnecessary administrative overhead.