**Working Hours Margin**

**Technical Name:** WorkingHoursMargin

**Category:** Workflow Configuration

**Default Value:** Not provided in the references.

**Impact Level:** Medium

**Description:**

The Working Hours Margin parameter is designed to configure the minimum allowable time difference between two uses of the same transaction by the same user. This setting helps in preventing rapid, repeated transactions within a very short timeframe, which could indicate improper usage or exploitation of system vulnerabilities.

**Business Impact:**

By setting an appropriate margin for working hours, organizations can add an additional layer of security and integrity to their transactions. This reduces the chances of fraud and ensures compliance with internal policies regarding system usage and transaction processing.

**Technical Impact when configured:**

When configured, the Working Hours Margin enforces a mandatory waiting period between transactions performed by the same user, thus ensuring that each transaction is deliberate and authorized. It helps in auditing and monitoring by filtering out noise created by too-frequent transaction attempts, improving the accuracy of transaction logs and reports.

**Examples Scenario:**

In a scenario where an organization requires that no user should perform the same transaction within a 10-minute interval to ensure all transactions are adequately vetted and authorized, the Working Hours Margin can be configured to enforce this policy. This would prevent a user from executing potentially harmful actions in quick succession, thereby mitigating risks associated with rapid transaction execution.

**Related Settings:**

- CommonSettings.Default.MinimumTimeDiffBetweenToUsesOfTheSameTransactionByTheSameUserInMinutes

**Best Practices:** configure when you need to enforce a minimum time interval between identical transactions by the same user to prevent abuse and ensure compliance. Avoid when transactions require flexibility and rapid execution that could be hampered by the enforcement of waiting periods.