**Technical Name:** ActiveDirectoryNumericFieldTypes

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**
ActiveDirectoryNumericFieldTypes parameter facilitates the customization and management of numeric field types within the Active Directory environment as part of the Pathlock Cloud GRC platform. It ensures the accurate interpretation and handling of numeric data associated with user accounts and business units (BU) in Active Directory.

**Business Impact:**
Proper configuration of ActiveDirectoryNumericFieldTypes aids in precise data management, supporting compliance with organizational policies and external regulations. It impacts security by ensuring the correct assignment of roles and access rights, which are often contingent upon these numeric values.

**Technical Impact: when configured**
- Ensures accurate processing and synchronization of numeric values between Pathlock GRC and Active Directory.
- Helps maintain data integrity, preventing errors that could arise from the misinterpretation of numeric fields.
- Facilitates correct data categorization and reporting, which is essential for audit and compliance purposes.

**Examples Scenario:**
An organization uses employee IDs as a critical part of their access control policy. Employee IDs are numeric and stored within Active Directory. The ActiveDirectoryNumericFieldTypes parameter is configured to recognize these IDs properly, ensuring that automated processes, such as role assignments based on employee IDs, are error-free.

**Related Settings:** CustomBUInfoTypeFields

**Best Practices:** 
- **Configure when** you have specific numeric fields in Active Directory that are integral to security and compliance workflows.
- **Avoid when** there is no clear definition or use of numeric fields within your organization’s Active Directory structure.