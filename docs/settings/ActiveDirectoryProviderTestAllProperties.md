# Active Directory Provider Test All Properties

**Technical Name:** ActiveDirectoryProviderTestAllProperties

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The parameter `ActiveDirectoryProviderTestAllProperties` is designed to ensure the correctness and completeness of the employee data synchronization process from an Active Directory (AD) to the Pathlock Cloud GRC platform. It focuses on verifying that all necessary employee attributes are updated correctly, particularly when an employee's employment status is not found in the system's default settings.

**Business Impact:**

Incorrect or incomplete employee data synchronization from Active Directory can lead to incorrect access rights assignment, failure to comply with security policies, and inefficient user management. Ensuring accurate data synchronization helps maintain operational efficiency, compliance with security standards, and effective access control within the organization.

**Technical Impact when configured:**

When configured, this parameter triggers a verification process for all properties of employee records during synchronization. If an existing employee's employment status matches the "employment status not found" setting, the system will update this employee's record with the new details. This ensures that employee data within the Pathlock GRC platform is comprehensive and up-to-date, reflecting any changes made in the Active Directory.

**Examples Scenario:**

- Scenario: An organization undergoes a restructuring process, leading to many employees changing departments or roles. The HR department updates these changes in Active Directory. `ActiveDirectoryProviderTestAllProperties` ensures that all such changes are accurately reflected in the Pathlock Cloud GRC platform, avoiding any discrepancies in access rights or compliance issues.

**Related Settings:**

- `EmploymentStatusForNotFound`: The default employment status used to identify employees whose current status may not be correctly listed in the Active Directory.

**Best Practices:** Configure `ActiveDirectoryProviderTestAllProperties` during initial setup and periodically thereafter to ensure consistent data synchronization, especially following significant organizational changes. Avoid manual data entry where possible to reduce errors.