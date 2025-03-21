# Organization Structure Secondary Provider Mode

**Technical Name:** OrganizationStructureSecondaryProvider_Mode

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter configures the mode for the secondary provider within the organization structure synchronization process.

**Business Impact:** Proper configuration ensures accurate and efficient synchronization of organization structure data from a secondary provider, enhancing the platform's ability to manage security, risk, and compliance effectively.

**Technical Impact when configured:** When this parameter is configured, it enables the system to incorporate additional comparison fields from a secondary provider, allowing for more granular control and accuracy in the synchronization process.

**Examples Scenario:** A company uses Pathlock GRC to manage their security posture and has multiple sources of organizational data. One source is the primary HR system and the other is Active Directory. To ensure both sources accurately reflect the current organizational structure, the OrganizationStructureSecondaryProvider_Mode can be configured to include additional comparison fields from Active Directory, ensuring that user roles and permissions are accurately assigned according to the most current information.

**Related Settings:** ActiveDirectorySecondaryProviderAdditionalFields

**Best Practices:** Configure when multiple sources for organizational data exist and need to be synchronized accurately. Avoid when only a single source of organizational information is used, to prevent unnecessary complexity.