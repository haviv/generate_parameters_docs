# Active Directory Provider Test Employee

**Technical Name:** ActiveDirectoryProviderTestEmployeeId

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:** 

The ActiveDirectoryProviderTestEmployeeId parameter is used within the Pathlock Cloud GRC platform's Active Directory integration processes. It identifies a specific employee as a test entity during synchronization operations, enabling organizations to validate and manage employment statuses effectively within their Active Directory environments.

**Business Impact:**

Utilizing this parameter helps maintain accurate and up-to-date employee status information within the organization's GRC platform. It ensures that employees with outdated or incorrect employment statuses are identified and corrected, thus mitigating risks associated with incorrect user access rights which could lead to unauthorized access or non-compliance with internal and external policies.

**Technical Impact when configured:**

When configured, this parameter triggers the mechanism within the Active Directory Provider to replace the information of an employee marked as "not found" with the updated status provided by this test employee configuration. It plays a critical role in automating user status updates and maintaining compliance with employment policies.

**Examples Scenario:**

An organization wishes to verify that their Active Directory synchronization process correctly identifies and updates the employment status of individuals no longer employed at the company. By configuring the ActiveDirectoryProviderTestEmployeeId, they can simulate the process of detecting an employee whose status needs to be updated and ensure the system behaves as expected without affecting actual employee data.

**Related Settings:**

- CommonSettings.Default.EmploymentStatusForNotFound
- CommonSettings.Default.CustomTerminateDateFieldinActiveDirectory

**Best Practices:** configure when

- Testing changes to employee status synchronization processes.
- Verifying the accuracy of employment status updates in the Active Directory.

avoid when

- Performing live updates on actual employee records.
- In environments where the employment status does not require regular verification or updates.