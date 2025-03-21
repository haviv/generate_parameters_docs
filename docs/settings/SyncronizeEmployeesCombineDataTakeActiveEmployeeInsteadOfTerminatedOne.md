# Synchronize Employees Combine Data Take Active Employee Instead Of Terminated One

**Technical Name:** SyncronizeEmployeesCombineDataTakeActiveEmployeeInsteadOfTerminatedOne

**Category:** User Management

**Default Value:** False

**Impact Level:** High

**Description:** This parameter configures the employee synchronization process to prioritize active employee records over terminated ones when combining data from multiple sources.

**Business Impact:** Ensures that the most relevant and current employee data is used in processes, enhancing data accuracy and operational efficiency. It prevents terminated employees from being accidentally authorized access or included in compliance reports, enhancing security and compliance posture.

**Technical Impact when configured:** When enabled, the system will ignore data from terminated employees if an active employee record exists with the same identifiers during data synchronization tasks. This reduces the risk of processing outdated or irrelevant employee data, which could lead to inaccurate access rights, compliance issues, or other data integrity problems.

**Example Scenario:** In an organization where employees may appear in multiple databases due to transfers or re-hiring, enabling this parameter ensures that only the latest, active employee record is utilized. For example, if an employee who was terminated and then rehired appears in both states across different data sources, the system will prioritize and synchronize the record where the employee is marked as active, ensuring up-to-date access rights and compliance classifications.

**Related Settings:** 

- `AddExcelDocumentSignDetails` (Ensures detailed signing information is included in Excel document exports)

**Best Practices:** Configure when you have multiple sources of employee data and need to ensure that only active employees are considered in GRC processes. Avoid configuration in environments where historical data of terminated employees is required for reporting or compliance purposes.