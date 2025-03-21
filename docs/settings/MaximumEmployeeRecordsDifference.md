# Maximum Employee Records Difference

**Technical Name:** MaximumEmployeeRecordsDifference

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:** 

This parameter defines the maximum allowed difference between the number of employee records in the system and the number of synchronized employee records. It ensures data consistency and integrity across integrated systems by monitoring and limiting discrepancies in employee data.

**Business Impact:**

A discrepancy beyond the configured threshold may indicate synchronization issues, potentially leading to access discrepancies, reporting inaccuracies, and compliance risks. It ensures that employee data remains consistent, up-to-date, and reliable across integrated platforms, supporting effective access governance and compliance with regulatory standards.

**Technical Impact when configured:**

When this parameter is configured, the system performs checks to ensure the difference between current and new employee records does not exceed the set threshold. If the threshold is exceeded, the system may trigger alerts or prevent further synchronization processes until the discrepancy is resolved, thereby promoting data integrity and consistency.

**Example Scenario:**

A company with dynamic employee turnover integrates the Pathlock GRC platform with its HR system to manage access rights. The Maximum Employee Records Difference parameter is set to allow a maximum discrepancy of 10 records. After a mass hiring or termination event, the synchronization process detects a difference of 15 employee records, triggering an alert signaling an investigation into the discrepancy to prevent unauthorized access or compliance issues.

**Related Settings:** 

- EmployeeFullNameSync
- CompanyEmployeeSyncThreshold

**Best Practices:** 

- Configure this parameter to a realistic threshold based on the organization's size and employee turnover rate to balance between regular synchronization needs and the avoidance of significant unsynced data that could impact security and compliance.
- Regularly review and adjust the threshold as the organization evolves or in response to observed synchronization performance and issues.