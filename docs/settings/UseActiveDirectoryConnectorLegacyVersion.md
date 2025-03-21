# Use Active Directory Connector Legacy Version

**Technical Name:** UseActiveDirectoryConnectorLegacyVersion

**Category:** Configuration

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls whether the Pathlock Cloud GRC platform uses the legacy version of the Active Directory connector. When enabled, the platform will utilize the older connector version for Active Directory interactions, which may be necessary for compatibility with certain legacy system configurations.

**Business Impact:**

Enabling the use of the legacy Active Directory connector can ensure uninterrupted connectivity and functionality for organizations that have older or custom configured Active Directory environments. It can prevent potential integration issues and maintain the integrity of user management and authentication processes.

**Technical Impact when configured:**

When enabled, this setting may limit the use of newer features and enhancements available in updated versions of the Active Directory connector. However, it ensures compatibility and functional stability for systems that require the legacy connector version, by maintaining established workflows and avoiding disruptions to user authentication and management processes.

**Examples Scenario:**

- An organization has a custom-configured Active Directory setup that is not fully compatible with the latest Active Directory connector. Enabling the use of the legacy connector version allows for smooth integration and prevents authentication issues.

**Related Settings:** 

- `SapConnectorIsRemoveAllRolesSupported`

**Best Practices:** 

- **Configure when:** You are facing compatibility issues with the current Active Directory setup and the new version of the connector. This ensures that your GRC processes continue to run smoothly without interruption.
  
- **Avoid when:** Your environment supports the latest features and improvements of the new Active Directory connector version, to benefit from enhanced security and performance optimizations.