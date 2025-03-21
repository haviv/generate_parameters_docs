# Active Directory Provider With External Data Employee Linkage Field

**Technical Name:** ActiveDirectoryProviderWithExternalDataEmployeeLinkadgeField

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the linkage field between employees in the Active Directory and external data sources. It allows for the synchronization and correlation of employee details across different systems.

**Business Impact:**

Effectively linking employee records between Active Directory and external data sources enhances the integrity of user management processes. It ensures that changes in employee statuses, roles, and other attributes are accurately reflected across all connected systems, reducing the risk of access discrepancies and security vulnerabilities.

**Technical Impact: when configured**

Correct configuration of this parameter ensures that the system can accurately merge and update employee details from Active Directory with those from external databases. This alignment is critical for maintaining up-to-date user access levels, adhering to compliance standards, and streamlining user management across multiple systems.

**Examples Scenario:**

- **Scenario 1:** An organization utilizes an external HR management system alongside their Active Directory. This parameter could be set to link employees by their employee ID, ensuring that any updates in the HR system, such as role changes or terminations, are automatically reflected in their access rights within the Active Directory.

**Related Settings:**

- `SodCheckForCompanyCodesByRolesOrgObjectName`
  
**Best Practices:** configure when the organization uses multiple sources for user management and needs to ensure data integrity across systems; avoid when there's no external data source to link with Active Directory.