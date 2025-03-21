# HR Employees File FTPSite Password Password Key

**Technical Name:** HREmployeesFileFTPSitePasswordPasswordKey

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter stores the encryption key used for securing the password associated with the username to access the FTP site for HR employees' files. It is essential for the secure transfer of sensitive HR data between the Pathlock GRC platform and the company’s HR systems.

**Business Impact:** Proper configuration of this parameter ensures that HR employee files transferred via FTP are done so securely, protecting sensitive employee data and ensuring compliance with data protection regulations. Misconfiguration may lead to unauthorized access to sensitive data, posing significant risk to privacy and compliance status.

**Technical Impact when configured:** When correctly configured, this parameter enables the secure encryption and storage of the FTP password, ensuring that only authorized systems and personnel can access HR employee files. It helps in maintaining the integrity and confidentiality of HR data during transfers.

**Examples Scenario:** An organization needs to regularly sync HR employee files from their internal systems to the Pathlock GRC platform for auditing and compliance purposes. The `HREmployeesFileFTPSitePasswordPasswordKey` is configured to encrypt the FTP password securely. This ensures that the automated process that syncs these files operates securely, without exposing sensitive password information in plain text.

**Related Settings:** HREmployeesFileFTPSite, HREmployeesFileFTPSiteUsername

**Best Practices:** 
- **Configure when:** Setting up the sync process for HR employee files via FTP for the first time or changing the FTP password.
- **Avoid when:** The FTP site does not require authentication or if files are transferred via a more secure method that does not involve FTP.