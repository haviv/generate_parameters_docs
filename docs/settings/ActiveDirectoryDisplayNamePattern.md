# Active Directory Display Name Pattern

**Technical Name:** ActiveDirectoryDisplayNamePattern

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The Active Directory Display Name Pattern is a configuration setting that specifies the pattern used to generate or match display names for users within the Active Directory environment.

**Business Impact:**

This parameter impacts how user accounts are identified and displayed within the system. It is crucial for ensuring consistency in user account management, which can affect auditing, reporting, and access control processes. Incorrect or inconsistent display name patterns can lead to user misidentification, impacting security protocols and compliance reporting.

**Technical Impact when configured:**

When this parameter is configured correctly, it ensures that all user accounts follow a uniform naming convention, simplifying user management, identification, and authentication processes. It aids in streamlining account setup, user identification for access reviews, and auditing activities by maintaining consistency in naming across the platform.

**Examples Scenario:**

- A company implements a naming convention ```[DepartmentCode]-[LastName][FirstInitial]``` for all user display names to quickly identify the department of the user and maintain consistency across the organization.
  
- During an audit, auditors can easily identify and verify user accounts based on their display names aligning with the configured pattern, facilitating a smoother compliance process.

**Related Settings:**

- OverrideCompanyLogoInPortal

**Best Practices:** 

- **Configure when:** Implementing or updating naming conventions for user accounts in Active Directory to ensure consistency, ease of management, and compliance with internal policies.
  
- **Avoid when:** There is no clear naming convention policy within the organization, as incorrect configuration can lead to inconsistencies and confusion in user account management.