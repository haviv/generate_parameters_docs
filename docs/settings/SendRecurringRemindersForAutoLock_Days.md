# Send Recurring Reminders For Auto Lock Days

**Technical Name:** SendRecurringRemindersForAutoLock_Days

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The parameter controls the sending of recurring reminders to users about the upcoming account auto-lock due to inactivity. This feature aims to ensure that users are aware of the auto-lock policy and take necessary action to avoid being locked out.

**Business Impact:**

Implementing this parameter can significantly reduce the number of user lockouts due to inactivity, thereby minimizing work disruption and reducing the workload on the IT support team. It helps maintain operational efficiency and enhances user accountability for maintaining active accounts.

**Technical Impact when configured:**

When enabled, the system will periodically send reminders to users about the impending auto-lock event. This ensures that users are given ample warning to take necessary action, such as logging in to the system to avoid account lockout.

**Examples Scenario:**

- A user hasn't logged in for a period close to the set threshold for inactivity. With this parameter enabled, the system automatically generates and sends a reminder to the user, prompting them to log in and thus avoid auto-lock.

**Related Settings:** 

- NonUsageDayLocking
- NonUsageDayWarning

**Best Practices:** 

- Configure when: You have a clear inactivity policy, and wish to proactively engage users to maintain access by reminding them to log in before reaching the auto-lock threshold.
- Avoid when: Your organization does not have a specific inactivity threshold or if constant reminders might cause unnecessary annoyance to the users.