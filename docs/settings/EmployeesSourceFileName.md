**Employees Source File Name**

**Technical Name:** EmployeesSourceFileName 

**Category:** User Management 

**Default Value:** Not Provided 

**Impact Level:** High 

**Description:** The EmployeesSourceFileName parameter is utilized for specifying the file name containing employee data that is synchronized via an FTP site, as part of the organization's process in the Pathlock Cloud GRC platform.

**Business Impact:** Incorrect configuration or misuse of this parameter could lead to failure in updating the employee data in the Pathlock system, affecting access controls, compliance reporting, and potentially exposing the organization to internal security risks due to outdated or incorrect employee information.

**Technical Impact when configured:** Proper configuration ensures the accurate and timely update of employee information within the platform, supporting effective user management and compliance processes. Misconfiguration may result in synchronization errors or absence of important employee data updates, impacting system reliability and data integrity.

**Examples Scenario:** A company wants to automate the process of updating its employee records in the Pathlock Cloud GRC platform. The HR department provides a weekly CSV file containing updates on employees. By specifying the correct EmployeesSourceFileName, the system can automatically retrieve and process this file, ensuring the platform reflects the most current employee data.

**Related Settings:** 

- `CommonSettings.Default.HREmployeesFileFTPSiteUsernamePasswordKey`
- `CommonSettings.Default.HREmployeesFileFTPSitePasswordPasswordKey`

**Best Practices:** 

- **Configure when:** you have established a regular update routine for employee data, ensuring the file name matches the provided CSV or data file from your HR system.
- **Avoid when:** you do not have a secure and encrypted method for transferring the employee data file or if the file does not follow the required data format standards.