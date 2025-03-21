# Active Directory Employee IDAttribute

**Technical Name:** ActiveDirectoryEmployeeIDAttribute

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The ActiveDirectoryEmployeeIDAttribute parameter specifies the attribute within Active Directory used to uniquely identify an employee within the Pathlock Cloud GRC platform. This parameter is crucial for integrating and synchronizing employee data between an organization's Active Directory and the Pathlock platform, ensuring accurate user management and security enforcement.

**Business Impact:**

Configuring this parameter correctly is essential for organizations to maintain accurate employee records, conduct reliable risk assessments, and enforce compliance measures. A proper setup enables streamlined operations, such as automating the provisioning and deprovisioning of user access, based on their employment status. Misconfiguration may lead to security vulnerabilities by allowing improper access to sensitive systems or data.

**Technical Impact when configured:**

- Ensures accurate synchronization of user profiles between Active Directory and Pathlock Cloud GRC platform.
- Facilitates precise user identification, aiding in efficient user management, security, and compliance operations.
- Supports effective risk management processes by maintaining updated user access rights in real-time.

**Examples Scenario:**

- An HR manager updates an employee's status in the corporate HR system, which in turn updates Active Directory. The ActiveDirectoryEmployeeIDAttribute ensures this update reflects in the Pathlock Cloud GRC platform, automatically adjusting the employee's access permissions according to their new status.

**Related Settings:**

- `DisableSystemSelectionNarrowByUserGroups`
- `ReadRoleAssignmentChangeDocuments`

**Best Practices:** configure when

- You have a stable and uniquely maintained employee identifier in Active Directory.
- You're looking to automate user management processes within the Pathlock Cloud GRC platform.

avoid when

- Employee identifiers in Active Directory are not consistently maintained.
- You lack the necessary permissions or knowledge to access or modify Active Directory attributes.