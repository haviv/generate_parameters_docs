# Take Usage Since Last Record

**Technical Name:** TakeUsageSinceLastRecord 

**Category:** Audit 

**Default Value:** N/A 

**Impact Level:** High 

**Description:**

This parameter determines whether the system should consider log entries that have not been active since the last record read during audit and monitoring workflows. Specifically, it helps in identifying inactive log reads, marking them as finished, and updating the system accordingly. 

**Business Impact:**

Allows businesses to ensure that their GRC (Governance, Risk Management, and Compliance) audits and monitoring activities are up-to-date by excluding outdated or irrelevant log entries. This parameter is crucial for maintaining the integrity and relevance of audit data, which in turn supports comprehensive risk assessments and compliance verification processes. 

**Technical Impact when configured:**

Once configured, `TakeUsageSinceLastRecord` will affect how the system handles inactive log reads by identifying log entries that haven't been active since the last recorded activity. It helps optimize the audit and monitoring processes by focusing on active and relevant log data, thus improving performance and accuracy in compliance reports and risk assessments.

**Examples Scenario:**

- An organization performs a monthly review of their security logs as part of their compliance with industry standards. Configuring this parameter ensures that only the logs relevant since the last review are considered, making the process more efficient and focused. 
- During a routine audit, auditors need to verify the activities performed in a given period. This parameter helps by filtering out all activities before the specified period, allowing for a targeted audit that saves time and resources.

**Related Settings:** 

- ReadUsageMaxDelayInSecondsForInactiveRead

**Best Practices:** configure when, 

- It's crucial to focus on recent activities for audits and compliance checks.
- The organization has a large volume of log data, and performance optimization during audits is necessary. 

avoid when,

- Complete historical log data is essential for your audit or compliance requirements, regardless of activity status.