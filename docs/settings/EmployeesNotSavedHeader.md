# Employees Not Saved Header

**Technical Name:** EmployeesNotSavedHeader

**Category:** HR

**Default Value:**

**Impact Level:** Medium

**Description:**

The EmployeesNotSavedHeader parameter is used to identify and manage employees within the synchronization process who are not saved to the organization's employee records in the Pathlock Cloud GRC platform. It is crucial for maintaining up-to-date and accurate employee data for HR management and compliance.

**Business Impact:**

Ensuring that all employee records are correctly saved and updated impacts several HR processes, including payroll, onboarding, access provisioning, and compliance with various regulations. Incorrect or outdated employee data can lead to security risks, compliance issues, and operational inefficiencies.

**Technical Impact when configured:**

When configured properly, this parameter helps in identifying discrepancies between the source of employee data (e.g., HRMS) and the Pathlock Cloud GRC platform, allowing for timely updates and corrections. This ensures that employee-related controls and compliance requirements are based on the most current data.

**Examples Scenario:**

An HR administrator notices that a recently onboarded employee's details are not reflected in the compliance reports. Using the EmployeesNotSavedHeader parameter, they identify that the new employee's record was not updated due to a synchronization issue, allowing them to correct the discrepancy promptly.

**Related Settings:**

- SMSNewUserAccountPassword
- SMSFolder

**Best Practices:** configure when new employees are added to the organization's HRMS to ensure they are correctly synchronized with the Pathlock Cloud GRC platform. Avoid manual interventions without proper verification to ensure data accuracy and integrity.