# User Multi User Max Number Of Users Per Computer Message

**Technical Name:** UserMultiUserMaxNumberOfUsersPerComputerMessage

**Category:** Reporting

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the display message related to the maximum number of users allowed per computer within the Pathlock Cloud GRC platform. It is primarily utilized in reports focusing on user-computer associations.

**Business Impact:**

Proper configuration of this parameter ensures compliance with internal user access policies and helps in managing the risk associated with excessive user associations to a single workstation, which can lead to potential security vulnerabilities and audit findings.

**Technical Impact when configured:**

When appropriately configured, it enhances the reporting capability by clearly communicating the policy restrictions concerning the number of users associated with a single computer. This helps in identifying and mitigating instances where excessive associations may suggest shared accounts or other compliance issues.

**Examples Scenario:**

An organization sets a policy that no more than 5 users should be associated with a single workstation to ensure individual accountability and reduce shared account risks. This parameter helps to generate reports highlighting any deviations from this policy, enabling quick remedial action.

**Related Settings:**

- SapUserRoleBackTraceRoleFromGeneratedProfile
- ImpactAnalysisShowControlsSelection

**Best Practices:** Configure this parameter according to your organization's internal controls around workstation access and user account management. Avoid overly restrictive settings that may hinder legitimate operational flexibility.