# Sap Employee Id Add Zero

**Technical Name:** SapEmployeeIdAddZero

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

The parameter determines whether zeros should be trimmed from SAP Employee IDs when synchronizing or processing data involving employee identifiers. When enabled, leading or trailing zeros in an employee ID are removed.

**Business Impact:**

Correct and consistent employee ID formatting is crucial for the accurate management of employee-related data and permissions. Misalignment in employee ID formats can lead to access issues, incorrect data reporting, and potential security breaches.

**Technical Impact when configured:**

Enabling this setting ensures that SAP Employee IDs are standardized across integrated systems, particularly when interfacing with Active Directory. It aids in preventing discrepancies due to leading or trailing zeros in employee IDs.

**Examples Scenario:**

When syncing employee data from SAP to Active Directory, an employee ID "000123" is automatically adjusted to "123" if `SapEmployeeIdAddZero` is enabled, ensuring uniform ID formats across both systems.

**Related Settings:**

- SapEmployeeIdTrimZero

**Best Practices:** configure when integrating SAP with systems that do not require leading or trailing zeros for identification purposes; avoid when exact matching of employee ID formats, including zeros, is necessary for system integration or data processing.