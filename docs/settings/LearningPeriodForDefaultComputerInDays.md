# Learning Period For Default Computer In Days

**Technical Name:** LearningPeriodForDefaultComputerInDays

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter specifies the duration, in days, within which the system learns and identifies the default computer for a user based on their activity patterns and used transactions.

**Business Impact:**

By accurately determining a user's default computer, organizations can enhance security protocols, ensuring that sensitive tasks are performed only from secure and recognized devices. It aids in minimizing the risks associated with unauthorized access and transaction execution, thereby bolstering the overall security posture.

**Technical Impact when configured:**

When set, this parameter influences how the system calculates and updates a user’s default computer in the background. A properly configured learning period allows the system to adapt to changes in user behavior over time, which can be particularly useful in dynamic environments where users might switch primary devices.

**Examples Scenario:**

A company implements a policy where financial transactions above a certain threshold must be executed from known devices only. By setting the `LearningPeriodForDefaultComputerInDays`, the GRC platform can identify and confirm the user's default computer, contributing to the enforcement of this policy by preventing potentially fraudulent transactions from unrecognized devices.

**Related Settings:** 

- SendRolesInBulkToSAP

**Best Practices:** configure when the user base is stable and primary devices do not frequently change, avoid when users are expected to switch their primary computing devices often.