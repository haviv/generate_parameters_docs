# Active Directory Account Remove Disable Users

**Technical Name:** ActiveDirectoryAccountRemoveDisableUsers

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls whether disabled user accounts in Active Directory should be automatically removed from the Pathlock Cloud GRC platform. When enabled, it helps maintain a clean and up-to-date user management system by removing access for users no longer active within the organization's Active Directory.

**Business Impact:** Keeping disabled users in the system can lead to inaccurate reporting and potential security risks, as it may provide a way for unauthorized access if these accounts were to be reactivated maliciously. Automatically removing these accounts helps ensure that only current, active users have access, thereby enhancing the overall security and accuracy of user access management within the platform.

**Technical Impact when configured:** When enabled, this setting actively monitors the status of user accounts within the connected Active Directory. If a user is marked as disabled in Active Directory, the corresponding user account is automatically flagged for removal within the Pathlock Cloud GRC platform, ensuring that there is no lag time in removing access rights for users no longer employed or authorized.

**Examples Scenario:**
- A company has a policy of disabling user accounts in Active Directory immediately upon an employee's departure. Enabling this parameter ensures that these users are also promptly removed from the Pathlock Cloud GRC platform, thereby preventing any unauthorized access and maintaining compliance with the company's access control policies.

**Related Settings:**
- NotifySubmitterInEmergancyAccessStep

**Best Practices:** Configure when the organization has a large number of users and high turnover, ensuring user accounts are accurately reflected in the system. Avoid when there is a process that requires manual review before permanently removing users from the system.