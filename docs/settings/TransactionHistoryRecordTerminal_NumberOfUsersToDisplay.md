**Transaction History Record Terminal Number Of Users To Display**

**Technical Name:** TransactionHistoryRecordTerminal_NumberOfUsersToDisplay

**Category:** Audit

**Default Value:** Not explicitly provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter controls the number of user records to display in the Transaction History Record Terminal panel. It is utilized for auditing purposes, providing visibility into the users that have accessed a particular terminal.

**Business Impact:**

Adjusting this parameter impacts an organization's ability to efficiently audit and monitor terminal usage. Ensuring that an optimal number of user records are displayed aids in identifying potential unauthorized access or misuse of company terminals, thus aiding in risk mitigation and policy enforcement.

**Technical Impact when configured:**

Configuring this parameter can optimize load times for the Transaction History Record Terminal and can also affect the comprehensiveness of the audit logs displayed. A lower number might load faster but could miss critical audit information, while a higher number might be more comprehensive but slower to load.

**Examples Scenario:**

- **Scenario 1:** An organization requires a detailed audit trail of terminal access for compliance reasons. Setting a higher value for this parameter will ensure that more user records are displayed, enhancing the ability to perform thorough audits.
  
- **Scenario 2:** To speed up the load times of the Transaction History Record Terminal, especially in high-traffic environments, the organization opts to decrease the number of users displayed. This adjustment allows for quicker access to the data, albeit at the cost of less detailed logs.

**Related Settings:** Not explicitly mentioned in the provided code references.

**Best Practices:** 

- **Configure when** detailed audit trails are essential for compliance and security monitoring. Increasing the value ensures comprehensive visibility into terminal access.
  
- **Avoid when** performance or load times are a concern, particularly in high-traffic scenarios. Reducing the number of records displayed can mitigate potential performance issues.