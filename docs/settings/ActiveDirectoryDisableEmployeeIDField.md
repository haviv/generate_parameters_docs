# Active Directory Disable Employee IDField

**Technical Name:** ActiveDirectoryDisableEmployeeIDField

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

The ActiveDirectoryDisableEmployeeIDField parameter controls whether the Employee ID field is utilized during the synchronization process between the Pathlock Cloud GRC platform and an organization's Active Directory (AD). When enabled (set to True), the synchronization process will ignore the Employee ID field, potentially altering the handling of user identities and credentials.

**Business Impact:**

Enabling this parameter may impact how user accounts are identified and managed within the Pathlock Cloud GRC platform, particularly in environments where Employee ID is a significant attribute for distinguishing between user accounts. It may affect user data accuracy, reporting, and auditing functionalities related to employee identification.

**Technical Impact when configured:**

- **Enabled (True):** The synchronization process will not consider the Employee ID field. This may be suitable for scenarios where the Employee ID is not consistent, not used, or could lead to duplications or conflicts during the synchronization process.
- **Disabled (False):** The Employee ID field will be used as part of the user account synchronization process, allowing for more precise mapping and management of user identities between Active Directory and the Pathlock Cloud GRC platform.

**Examples Scenario:**

For organizations that have recently undergone a merger or acquisition, there might be overlapping or duplicate Employee ID values. Enabling this setting could help mitigate issues related to duplicate identities by ignoring the Employee ID field, thus relying on other attributes to distinguish between user accounts.

**Related Settings:**

- RemoveInvalidApproversFromApprovalGroups

**Best Practices:** 
- **Configure when:** There are known inconsistencies in Employee ID usage within your organization's Active Directory, or when Employee ID duplication could lead to synchronization issues.
- **Avoid when:** Employee ID is a critical attribute for your organization's identity management processes, and there is confidence in its consistency and uniqueness across all user accounts.