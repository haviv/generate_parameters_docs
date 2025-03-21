# Enable Lock User Locally For Non Active User

**Technical Name:** EnableLockUserLocalyForNonActiveUser

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether users who have not been active for a specified period are automatically locked locally within the system. It aims to enhance security by disabling accounts that are not in use, effectively reducing potential attack vectors for unauthorized access.

**Business Impact:**

Leaving inactive user accounts unlocked can pose a significant security risk to an organization, as these accounts can be exploited by attackers to gain unauthorized access to sensitive information and systems. Enabling this feature helps mitigate such risks by ensuring that only active and necessary accounts remain operational, thereby adhering to the principle of least privilege.

**Technical Impact when configured:**

When enabled, this feature automatically locks user accounts that have been inactive for the designated period, as specified in the system's configuration settings. It relies on the NonUsageDayLocking setting to determine the period of inactivity before locking the account. Furthermore, it supplements any default lockout policies by applying these settings locally, offering an additional layer of security beyond default authentication mechanisms.

**Examples Scenario:**

An organization wishes to enhance its security posture by ensuring that only actively used user accounts can access its systems. By activating the **EnableLockUserLocallyForNonActiveUser** parameter, they can automatically lock accounts that have not been used for a certain number of days, effectively reducing the risk associated with dormant accounts.

**Related Settings:**

- NonUsageDayLocking: Specifies the number of days of inactivity after which a user account is locked.
- AdditionalAdminMailRecipients: Defines additional email recipients to be notified when an account is automatically locked due to inactivity.

**Best Practices:** 

- **Configure when:** Enhancing system security and compliance with internal or external audit requirements by ensuring inactive accounts are automatically locked.
  
- **Avoid when:** If frequent user reactivation is required due to business processes involving extended periods of inactivity, consider adjusting the NonUsageDayLocking threshold instead of disabling the feature entirely.