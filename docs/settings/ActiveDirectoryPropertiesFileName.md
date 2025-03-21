# Active Directory Properties File Name

**Technical Name:** ActiveDirectoryPropertiesFileName

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:**

This configuration parameter specifies the file name for Active Directory properties. It is used to define how Active Directory user profile attributes are mapped and handled within the Pathlock Cloud GRC platform.

**Business Impact:**

Proper configuration and naming of the Active Directory properties file help ensure that user data from Active Directory is accurately imported and managed within the Pathlock platform. This impacts user management, security policies enforcement, compliance reporting, and risk management processes.

**Technical Impact when configured:**

- Ensures that user profiles are populated with accurate data from Active Directory.
- Facilitates automated user account provisioning and deprovisioning based on organizational policies.
- Enhances security and compliance by ensuring that only the relevant AD attributes are imported and properly mapped to Pathlock user profiles.

**Examples Scenario:**

An organization wants to import specific user attributes from Active Directory to Pathlock for compliance purposes. By configuring the Active Directory Properties File Name, they can specify which attributes (e.g., `mail`, `manager`, `mobile`) are important for their compliance reports and should be imported into the Pathlock system.

**Related Settings:**

- `BackupRoot`
- `BackupFolderDateFormat`

**Best Practices:** configure when,

- Setting up initial integration with Active Directory.
- Updating mappings between Active Directory attributes and Pathlock user profile attributes.
  
avoid when,

- Making uninformed changes that might disrupt user profile data integrity.
- Unnecessary attribute mappings that do not add value to security, compliance, or risk management efforts.