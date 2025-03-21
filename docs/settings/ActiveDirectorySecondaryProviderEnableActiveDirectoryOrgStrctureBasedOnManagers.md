# Active Directory Secondary Provider Enable Active Directory Org Structure Based On Managers

**Technical Name:** ActiveDirectorySecondaryProviderEnableActiveDirectoryOrgStrctureBasedOnManagers

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter enables organizations to leverage a secondary Active Directory (AD) provider for generating the organizational structure based on the manager-employee relationships defined within AD. When configured, it allows Pathlock Cloud GRC to accurately reflect an organization's hierarchy as maintained in Active Directory, supporting enhanced compliance and governance.

**Business Impact:**

Enabling this feature can significantly enhance an organization's ability to manage user permissions and roles in line with their actual organizational structure. It ensures that access rights and compliance controls are aligned with real-world hierarchies, enhancing internal controls and reducing the risk of unauthorized access or non-compliance with internal and external regulations.

**Technical Impact when configured:**

- Organization structures are automatically updated and maintained in sync with Active Directory, reducing administrative overhead.
- Helps in enforcing Segregation of Duties (SOD) controls more effectively by reflecting accurate reporting lines and departmental structures.
- Support for secondary AD providers offers redundancy and flexibility in managing complex organizational structures across multiple domains or forests.

**Examples Scenario:**

An organization has recently restructured, creating new departments and changing reporting lines. By enabling this parameter, the Pathlock Cloud GRC platform will automatically update the organizational structure based on the AD information, saving time on manual updates and ensuring that access rights and compliance checks are immediately aligned with the new structure.

**Related Settings:**

- ActiveDirectorySecondaryProviderCustomDomains

**Best Practices:** configure when your organization's structure is primarily managed and up-to-date in Active Directory, and you have distinct manager-employee relationships defined. Avoid when your organizational structure does not map cleanly to AD or when most users do not have a designated manager in AD.