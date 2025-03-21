# PTDM Smart Query Entities Path

**Technical Name:** PTDM_SmartQueryEntitiesPath

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The PTDM_SmartQueryEntitiesPath parameter specifies the filesystem path to the entities used by the Smart Query functionality within the Pathlock GRC platform. This setting is critical for ensuring that Smart Query has access to the necessary files to perform its operations.

**Business Impact:**

Correct configuration of this parameter ensures that the Smart Query features operate efficiently and securely, allowing users to perform complex data queries across the organization's digital assets. Misconfiguration could lead to issues in data retrieval or potential security vulnerabilities.

**Technical Impact when configured:**

When properly configured, the PTDM_SmartQueryEntitiesPath parameter allows for seamless access to the required entity files by the Smart Query functions, ensuring robust and secure data querying capabilities. It also supports maintenance of the GRC platform's compliance and facilitates effective risk management.

**Examples Scenario:**

An organization may need to adjust the PTDM_SmartQueryEntitiesPath parameter when moving the location of Smart Query entity files due to storage optimization, security considerations, or during an upgrade process. For example, if the Smart Query entities were initially stored in a network shared location but need to be moved to a more secure, localized storage solution, the PTDM_SmartQueryEntitiesPath would need to be updated to reflect this new location.

**Related Settings:**

- PTDM_LogoHtmlPath: This setting, while primarily affecting the location of a logo file, indicates the usage of path-based configurations within the Pathlock GRC platform, which could be relevant when considering the broader implications of file path settings on the platform's operation and security.

**Best Practices:** configure when

- Moving entity files to a new location for operational efficiency or security reasons.
- Setting up the Pathlock GRC platform for the first time or during migration to a new server.

avoid when

- Making arbitrary changes without understanding the impact on Smart Query functionality and security.
- Ignoring file permission settings on the new path, which could lead to unauthorized access.