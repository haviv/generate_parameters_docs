# Send Recurring Reminders For Auto Lock

**Technical Name:** SendRecurringRemindersForAutoLock

**Category:** User Management

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls whether users receive recurring reminders if their account is set to be automatically locked due to inactivity. It ensures users are warned well in advance before their account gets locked, providing them an opportunity to remain active.

**Business Impact:**

Enabling this feature reduces the risk of business disruption by ensuring that users are aware of impending account locks due to inactivity. It promotes security awareness by reminding users to engage with the system regularly, thereby also helping in maintaining compliance with security policies that require regular user activity.

**Technical Impact when configured:**

When enabled, the system will automatically send out reminders to users who are approaching the auto-lock threshold for inactivity. This is particularly useful in environments where user engagement is critical, and access needs to be strictly managed to comply with internal or regulatory compliance requirements.

**Examples Scenario:**

A user has not logged into the Pathlock GRC platform for a period close to the threshold set for inactivity (e.g., 90 days). If the Send Recurring Reminders For Auto Lock parameter is enabled, the user will receive email reminders before the auto-lock policy is enforced, prompting the user to log in and thus prevent their account from being locked.

**Related Settings:** 

- EnableLockUserLocallyForNonActiveUser
- NonUsageDayLocking
- NonUsageDayWarning

**Best Practices:** 

- **Configure when:** It's critical to keep users informed about their account status, especially in environments with strict access and inactivity policies. Regular reminders can help mitigate the risk of accidental account locks that can disrupt user workflow and impact business operations.
- **Avoid when:** In scenarios where user activity is not a compliance requirement or where account inactivity does not pose a risk to operational efficiency, this feature could potentially be disabled to reduce unnecessary email traffic.