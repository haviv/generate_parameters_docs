# Enable SM20 Detailed Log From SE16

**Technical Name:** EnableSM20DetailedLogFromSE16

**Category:** Audit

**Default Value:** False

**Impact Level:** High

**Description:** This parameter enables the detailed logging of activities through SE16, enhancing the audit trails for data access and manipulation conducted via this transaction.

**Business Impact:** Activating this parameter significantly improves the organization's ability to monitor and audit sensitive data access and manipulation, thus aiding in compliance with internal and external audit requirements. It helps in identifying unauthorized or suspicious access to data, thereby reducing the risk of data breaches and ensuring data integrity.

**Technical Impact when configured:** When enabled, it provides granular logs of all activities executed through SE16, including read, update, or delete operations. This detailed logging aids forensic and compliance investigations by offering an in-depth view of data access patterns.

**Examples Scenario:** If a compliance officer needs to ensure that all data access through transaction SE16 is monitored and logged to comply with GDPR, enabling this parameter would ensure that all access and manipulation of data through SE16 is logged in detail. This would enable the organization to respond effectively to audits and data access queries, demonstrating compliance with GDPR requirements.

**Related Settings:** 
- CustomUserGroupIdForExcludedUsersFromUsageLogs
- EnableSoDForObjectLevelOnlyRoles

**Best Practices:** 
- Configure when: Detailed audits of SE16 transactions are required for compliance or security policies.
- Avoid when: The performance impact of logging detailed activities is a concern, or when the organization does not utilize SE16 for sensitive data access.