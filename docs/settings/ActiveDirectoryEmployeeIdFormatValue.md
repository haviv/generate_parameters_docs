**Technical Name:** ActiveDirectoryEmployeeIdFormatValue

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls the formatting of employee IDs fetched from Active Directory within the Pathlock Cloud GRC platform. Specifically, it determines whether the employee ID should be read and if leading zeroes should be trimmed.

**Business Impact:**

Correct employee ID formatting is crucial for ensuring that employee records are accurately synchronized across systems. Incorrect or inconsistent employee IDs can lead to mismatches in user profiles, affecting access rights, audit trails, and compliance reporting. Ensuring proper employee ID formatting supports accurate identity management and access governance.

**Technical Impact when configured:**

When enabled, this feature removes leading zeros from employee IDs during the synchronization process, potentially standardizing ID formats across various systems connected to the Pathlock Cloud GRC platform. This can aid in unifying user identity records and ensuring that employee IDs are consistently formatted across integrated systems.

**Example Scenario:**

A company uses a leading zero in their employee IDs within their HR system (e.g., "001234") but does not use these leading zeros in their project management system (e.g., "1234"). Enabling this parameter will trim the leading zeros during import from Active Directory, making the ID format consistent across both systems and reducing user identity discrepancies.

**Related Settings:**

- `ReadEmployeeToUserMappingForAllSystemsFromHRSystem`

**Best Practices:** 

- Configure when there's a discrepancy in employee ID formats across integrated systems to ensure consistent identity records.
- Avoid when all integrated systems already use a consistent employee ID format, as unnecessary trimming might lead to data inconsistencies.
