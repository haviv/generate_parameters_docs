# Rest Organization Structure Provider Run In Cloud For Secondary Provider

**Technical Name:** RestOrganizationStructureProvider_RunInCloud_ForSecondaryProvider

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the secondary organizational structure provider to run in a cloud environment. It determines how the Pathlock Cloud GRC platform interfaces with external systems for organizational structure data sync when dealing with a secondary provider.

**Business Impact:**

Enabling this parameter ensures that the organization's secondary structure data is seamlessly integrated into the Pathlock GRC platform from a cloud-based service. This is crucial for organizations that manage their data across multiple platforms or have a complex organizational structure that requires syncing with the main GRC platform to ensure accurate risk, compliance, and security management.

**Technical Impact when configured:**

When configured, this parameter allows the Pathlock GRC platform to connect to and synchronize with a secondary organization structure provider operating in the cloud. This ensures that data related to the organizational structure, such as departments, roles, and employee hierarchies, are up-to-date and accurately reflected within the GRC platform.

**Examples Scenario:**

An organization uses a primary HR system for managing employee data but also uses a cloud-based project management tool that maintains a separate list of teams and projects. Configuring this parameter allows the GRC platform to integrate organizational data from the cloud-based tool as a secondary provider, ensuring comprehensive visibility and management of access controls, compliance, and risk assessment across all systems.

**Related Settings:**

- ExternalDatabaseEmployeesSelectQuery_ForSecondaryProvider

**Best Practices:** configure when the organization uses a secondary system for maintaining part of its organizational structure in the cloud. Avoid when the organizational structure is fully managed within a single, primary system to minimize complexity and potential data synchronization issues.