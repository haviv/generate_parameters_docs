# Run One Level SoD Check In Memory

**Technical Name:** RunOneLevelSoDCheckInMemory

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

The "Run One Level SoD Check In Memory" parameter is designed to facilitate the execution of Segregation of Duties (SoD) checks within the Pathlock Cloud GRC platform, directly in memory. This method is intended to enhance performance by avoiding disk I/O operations, thus speeding up the SoD check processes. 

**Business Impact:**

Implementing this parameter can significantly reduce the time required for SoD checks, making the compliance process more efficient. It aids in the quick identification of forbidden combinations of roles or permissions assigned to a single user that might lead to potential conflicts of interest, thereby helping in maintaining a robust internal controls environment.

**Technical Impact when configured:**

Upon configuration, SoD checks are performed in memory, leading to faster processing times and immediate feedback on potential SoD violations. This can be particularly beneficial in environments with large user bases or complex permission structures.

**Examples Scenario:**

- During an internal audit, auditors need to review the current state of SoD controls. The "Run One Level SoD Check In Memory" parameter is enabled, allowing them to rapidly assess compliance without impacting system performance.
- A company is preparing for their yearly compliance audit and needs to ensure that all SoD conflicts are resolved. Enabling this parameter allows them to quickly run checks and address any issues in a timely manner.

**Related Settings:**

N/A

**Best Practices:** Configure when running frequent compliance checks in environments with complex permission settings to improve performance and reduce load times. Avoid when detailed logging of SoD checks on disk is required for audit trails or when memory resources are limited.