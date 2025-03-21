# Show Not Locked Icon

**Technical Name:** ShowNotLockedIcon

**Category:** User Management

**Default Value:** Not explicitly provided in the provided code snippets. Assume default behavior aligns with overall system defaults based on configuration settings.

**Impact Level:** Medium

**Description:**

The "Show Not Locked Icon" parameter controls the display of visual icons indicating the lock status associated with user accounts or resources within the Pathlock Cloud GRC platform. This setting allows administrators to configure the user interface to either show or hide icons for items that are not locked, enhancing the clarity of user or resource status.

**Business Impact:**

The visibility of not locked icons assists in quick identification of active or available user accounts and resources, contributing significantly to the management and review processes within security, compliance, and audit operations. It aids in preventing unauthorized access and ensuring that proper security measures are in place and effective.

**Technical Impact when configured:**

When the parameter is configured to display the not locked icons, it provides immediate visual feedback on the status of users or resources directly from the interface, improving operational efficiency. In contrast, disabling this feature could obscure the visibility of such statuses, potentially making the management of user access rights and resource allocations more cumbersome.

**Examples Scenario:**

An administrator wishes to quickly identify all user accounts currently not locked out due to incorrect logon attempts or other security policies. By enabling the "Show Not Locked Icon", administrators can visually scan through a list or report within the Pathlock platform, identifying at a glance those accounts that are active and not subject to a lockout.

**Related Settings:**

- `SendRecurringRemindersForAutoLock`: This setting, when enabled, sends recurring reminders for automatically locking features, indirectly related through the overarching theme of account and resource lock management.

**Best Practices:** Configure to show the not locked icons in environments where rapid verification of user status contributes to operational security and efficiency. Avoid when minimalistic UI is preferred or in scenarios where the presence of additional icons could lead to information overload.