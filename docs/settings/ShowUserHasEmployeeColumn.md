# Show User Has Employee Column

**Technical Name:** ShowUserHasEmployeeColumn

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of the "Has Employee" column in user-related reports and views within the Pathlock Cloud GRC platform. Enabling this setting will display an additional column indicating whether a user is associated with an employee record, providing a clearer linkage between user accounts and employee details.

**Business Impact:**

Enabling the "Show User Has Employee Column" feature provides administrators and auditors with enhanced visibility into the association between user accounts and their corresponding employee records. This visibility is crucial for ensuring accurate user management, compliance reporting, and for conducting thorough security and risk assessments.

**Technical Impact when configured:**

When configured, the system will include an additional column in relevant reports and user interfaces that indicates whether a user account is linked to an employee record. This can affect the performance of reports by introducing additional data retrieval and rendering requirements. 

**Examples Scenario:**

An administrator is auditing access controls and needs to verify that all active user accounts are associated with current employees. By enabling this feature, they can easily identify and investigate any user accounts that do not have a corresponding employee record, thereby mitigating potential risks associated with orphaned or unauthorized accounts.

**Related Settings:**

- UserInformationUrl
- UserMultipleUsageTimeRangeInMinutes

**Best Practices:** Configure when conducting audits, compliance checks, or when maintaining tight security and user management protocols. Avoid when unnecessary to minimize additional processing and simplify user interfaces.