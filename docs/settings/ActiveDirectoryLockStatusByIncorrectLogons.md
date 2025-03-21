# Active Directory Lock Status By Incorrect Logons

**Technical Name:** ActiveDirectoryLockStatusByIncorrectLogons

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

This parameter is designed to help manage security within the Pathlock Cloud GRC platform, specifically concerning user access and authentication via Active Directory. It identifies the lock status of user accounts that have had multiple incorrect logon attempts, contributing to safeguarding against unauthorized access.

**Business Impact:**

Implementing this parameter enhances the organization's security posture by preventing potential breaches through brute-force attacks. It ensures that user accounts are monitored and controlled for incorrect logon attempts, mitigating the risk of unauthorized access to sensitive and critical business information.

**Technical Impact when configured:**

When configured, this parameter actively monitors and identifies Active Directory user accounts that are locked due to incorrect logon attempts. It serves as a preventive measure against unauthorized access attempts, ensuring that accounts subjected to such activities are flagged and can be reviewed for further action.

**Examples Scenario:**

A user account within an organization's Active Directory is subjected to multiple incorrect login attempts, triggering a lockout based on the organization's defined security policy. The Active Directory Lock Status By Incorrect Logons parameter will identify and flag this user account, enabling security administrators to investigate the lockout's cause and implement corrective measures, such as password reset protocols or additional security training for the affected user.

**Related Settings:**

- CustomRolesThatAllowWorkflowManager
- SapConnectorCreateUserCUARetries

**Best Practices:** 

- **Configure when:** Setting up security and compliance measures within the Pathlock platform to ensure user accounts are protected against brute force attacks or unauthorized access.
- **Avoid when:** If the organization operates within a highly flexible access control environment or if the parameter's implementation could inadvertently lock out authorized users without established protocols for quick account recovery.