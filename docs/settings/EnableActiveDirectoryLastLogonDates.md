# Enable Active Directory Last Logon Dates

**Technical Name:** EnableActiveDirectoryLastLogonDates

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:** 

This parameter controls whether the Pathlock Cloud GRC platform captures and monitors the last logon dates from Active Directory. Enabling this feature allows organizations to track the activity and authenticate the status of users within their network, which is crucial for maintaining security protocols and managing user access effectively.

**Business Impact:** 

Enabling this feature provides insights into user activity, helping to identify inactive accounts that might pose a security risk if compromised. It also aids in compliance by ensuring only active and legitimate users have access to critical systems and information. 

**Technical Impact when configured:** 

Once configured, the system begins to monitor and record the last logon dates for users within the Active Directory. This data is essential for audits, compliance reporting, and for the enforcement of access control policies based on user activity.

**Example Scenario:** 

Consider a scenario where an organization needs to comply with industry regulations that require active monitoring and reporting of user access and activity. By enabling this parameter, the organization can easily identify users who have not logged in for an extended period, which might indicate a dormant account that should be disabled to reduce the potential attack surface for hackers.

**Related Settings:** 

- CloudApprovalServerUrl
- CloudApprovalToken

**Best Practices:** 

- **Configure when:** Implementing or enhancing security and audit controls, especially in environments subject to strict regulatory compliance requirements regarding user access and activity monitoring.
- **Avoid when:** The organization lacks the capacity to manage the data or when user logon activity is not relevant for security or compliance purposes.