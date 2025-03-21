**Technical Name:** NotUsedDaysMediumLowLevel

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:** 

The `NotUsedDaysMediumLowLevel` parameter is used within Pathlock's GRC platform to designate a threshold value indicating the number of days a user account has not been active, at a medium to low severity level. This parameter is critical for identifying potentially stale or inactive user accounts, which may represent a security risk if not monitored and managed appropriately.

**Business Impact:** 

Setting an appropriate value for this parameter helps organizations maintain robust security policies by ensuring user accounts that have not been active for a specified period are flagged for review. This can significantly reduce the risk associated with dormant accounts, such as unauthorized access or misuse, thereby protecting sensitive information and maintaining compliance standards.

**Technical Impact: when configured**

When configured, the `NotUsedDaysMediumLowLevel` parameter assists in generating reports that highlight user accounts falling within the specified inactivity range. This allows IT security and compliance teams to take timely action, such as conducting further investigations, prompting users to log in, or disabling accounts as necessary to maintain security and compliance.

**Examples Scenario:**

A company sets the `NotUsedDaysMediumLowLevel` parameter to 60 days. Any user account that has not logged in for 60 days will be flagged in the Non-Active Users Report. This enables the security team to review these accounts, confirm if they are still needed, and take appropriate action such as reaching out to the account holders or disabling the accounts to prevent unauthorized access.

**Related Settings:** NotUsedDaysMediumLevel

**Best Practices:** configure when the organizational security policy requires monitoring and action on medium to low-level inactivity of user accounts; avoid when active monitoring and management of user account activity is not considered a security concern or is handled by other means.