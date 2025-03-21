# Include Only Users With HR Record In Lock Process

**Technical Name:** IncludeOnlyUsersWithHRRecordInLockProccess

**Category:** User Management

**Default Value:** Not provided

**Impact Level:** High

**Description:**

This parameter controls whether the lock process in Pathlock's Cloud GRC platform applies only to users who have an associated HR record. When enabled, it ensures that only users verified by HR data are subject to automatic lock processes due to inactivity or incorrect logon attempts. This adds an additional layer of verification before locking out a user, helping to prevent erroneous lockouts.

**Business Impact:**

The primary business impact of enabling this parameter is to reduce the risk of locking out active users who are vital to day-to-day operations but may be flagged by automated security protocols. It helps in maintaining operational continuity by ensuring that only users without HR validation are considered for lockouts. It's particularly useful in scenarios where temporary or contractor accounts might not have HR records and should not be locked out automatically based on the same criteria as permanent employees.

**Technical Impact when configured:**

When configured, this parameter filters the user base considered by the lock process, concentrating lockout actions on users with HR records. This approach minimizes disruptions to business processes by protecting against potential overreach of automated security measures. It also implies that organizations need to maintain up-to-date HR records in the system for effective implementation.

**Examples Scenario:**

A company uses Pathlock's Cloud GRC to automate user account lockouts after repeated incorrect logon attempts or prolonged inactivity. However, they have experienced issues with temporary employees and contractors getting unfairly locked out, as these accounts often do not have complete HR records. By enabling 'IncludeOnlyUsersWithHRRecordInLockProccess', the company can ensure that only those users with verified HR records are included in the lockout process, reducing unnecessary lockouts and avoiding operational disruptions.

**Related Settings:** 

- `AutomaticLockUserEnableWorkflowAction`
- `AutomaticUserLockIncludeUsersLockedByIncorrectLogons`

**Best Practices:** configure when you have a reliable and up-to-date HR record system to validate user accounts, avoid when your organization has a significant number of active users without HR records as it could potentially overlook security risks among these users.