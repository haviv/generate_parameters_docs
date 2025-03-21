# FMGet Missing Authorization For User

**Technical Name:** FMGetMissingAuthorizationForUser

**Category:** Security

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to identify and retrieve missing authorizations for a specific user by comparing the current user authorizations against the required authorizations defined in the system. It plays a crucial role in maintaining the security posture of an organization by ensuring users have the necessary permissions to perform their job functions without exceeding their authority, thereby minimizing the risk of unauthorized access or actions within the system.

**Business Impact:**

Improper configuration of this parameter may lead to users having insufficient permissions, hindering their ability to perform job duties efficiently. Conversely, it may also result in users having more access than necessary, which can lead to unauthorized activities, potentially compromising system integrity and sensitive data.

**Technical Impact when configured:**

When properly configured, this parameter enhances security by dynamically identifying discrepancies in user authorizations and suggesting necessary adjustments. It aids in the ongoing review and rectification of authorization issues, aligning user access with organizational policies and compliance requirements.

**Example Scenario:**

A financial auditor requires temporary access to certain financial records and systems. By utilizing the FMGetMissingAuthorizationForUser parameter, the system can automatically identify the specific authorizations missing from the auditor's profile, allowing the security team to grant access efficiently and securely, ensuring compliance with audit requirements while minimizing the risk of unauthorized access.

**Related Settings:**

- AuthorizationReviewExcludeLockedUsersByLogons

**Best Practices:** configure when you need to periodically review user authorizations for compliance and security reasons. Avoid configuring this parameter without a clear understanding of the required user authorizations and roles within your organization to prevent granting excessive or insufficient access rights.