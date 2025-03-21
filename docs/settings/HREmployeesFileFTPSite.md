# HR Employees File FTPSite

**Technical Name:** HREmployeesFileFTPSite

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The HR Employees File FTPSite parameter is configured to specify the FTP site location where the HR employees' files are hosted. This setting is crucial for synchronizing organization structure data, particularly for operations related to the length of employee IDs.

**Business Impact:**

Proper configuration ensures the seamless import and synchronization of HR employee data into the Pathlock Cloud GRC platform. Incorrect setup may result in partial or failed data synchronization, affecting compliance and security posture management.

**Technical Impact when configured:**

Correct configuration enables the Pathlock GRC platform to correctly access and process HR employee files from the designated FTP site. This includes adjusting the employee ID length to match the system's requirements, ensuring data integrity and consistency across the platform.

**Examples Scenario:**

A company needs to integrate HR employee data from an external HR system hosted on an FTP site. By setting the HREmployeesFileFTPSite parameter with the correct FTP site URL, Pathlock Cloud GRC can access, import, and correctly format the employee IDs during the synchronization process, ensuring accurate employee data is available for compliance and risk management.

**Related Settings:** 

No specific related settings identified based on the provided code references.

**Applicable Workflows Actions:** 

No specific workflow actions identified for this parameter.

**Best Practices:** configure when the HR system or data source for employee information is external and accessible via an FTP site, avoid when employee data synchronization is not required or if employee data is stored and managed internally without the need for FTP access.