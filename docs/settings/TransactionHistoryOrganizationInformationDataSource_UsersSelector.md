# Transaction History Organization Information Data Source Users Selector

**Technical Name:** TransactionHistoryOrganizationInformationDataSource_UsersSelector

**Category:** Reporting

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter is used to select data regarding the usage of transactions by users within an organization. It compiles data related to transaction history, focusing on the average usage per month, usage in the last month, and the total number of users who have executed a particular transaction within a specified period.

**Business Impact:**

Configuring this parameter helps organizations understand the utilization patterns of their enterprise systems, which is crucial for auditing, compliance, and optimizing business processes. By identifying underused or overly complex transactions, businesses can streamline operations, improve user training, and tighten security measures.

**Technical Impact when configured:**

- Enables detailed reporting on transaction usage.
- Can identify trends in transaction usage over time.
- Assists in compliance and audit processes by providing usage data.
- Helps in identifying potential security and authorization issues based on transaction access and usage patterns.

**Examples Scenario:**

An organization aims to review the usage of critical financial transactions in their ERP system to ensure only authorized users are accessing sensitive information and to comply with internal audit requirements. By configuring this parameter, they can generate a report showing how often these transactions are used, by whom, and identify any irregular patterns or unauthorized access.

**Related Settings:**

- DisableUsage

**Best Practices:** 

- Configure when you require detailed transaction usage insights for audit, compliance, or optimization purposes.
- Avoid when unnecessary to minimize performance overhead on reporting and to protect user privacy.