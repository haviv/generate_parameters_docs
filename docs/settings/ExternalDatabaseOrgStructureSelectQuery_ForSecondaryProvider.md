# External Database Org Structure Select Query For Secondary Provider

**Technical Name:** ExternalDatabaseOrgStructureSelectQuery_ForSecondaryProvider

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:** This parameter defines the SQL query used to select organizational structure information from an external database when the secondary provider is configured. This setting allows for the customization of the data retrieval process based on specific database schemas or requirements.

**Business Impact:** Proper configuration ensures that accurate and up-to-date organizational structure information is imported into the Pathlock platform from secondary sources. This impacts roles, permissions, and compliance reporting accuracy across the board, thus maintaining the integrity of security and risk management processes.

**Technical Impact when configured:** When correctly configured, it allows the system to accurately pull organizational structure data from an external source, ensuring the system's user and permissions data reflects the current organizational hierarchy and roles as defined in the external HR or identity systems.

**Examples Scenario:** If your organization uses a custom HR system as a secondary provider for organizational data, and this system stores employee information in a unique schema, you would customize this query to accurately retrieve employee roles, departments, and hierarchy information to ensure Pathlock's access control and compliance features operate with the most current data.

**Related Settings:** 
- OrganizationStructureSecondaryProvider_Custom_HR_SystemId

**Best Practices:** 
- **configure when:** you have a secondary provider that contains vital organizational structure information not available in the primary source, and this information is crucial for your GRC processes.
- **avoid when:** your primary data source already includes all necessary organizational structure data, to prevent duplications and inconsistencies.