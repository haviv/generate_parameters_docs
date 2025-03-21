# Enable Get Current Use

**Technical Name:** EnableGetCurrentUse

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The Enable GetCurrent Use parameter is designed to control the visibility and accessibility of certain configuration settings within the Pathlock Cloud GRC platform. It influences how advanced settings are displayed and managed, contributing to the overall security and operational efficiency of the platform.

**Business Impact:**

Enabling this parameter ensures that sensitive configuration settings remain hidden from unauthorized access, thus preserving the integrity and security of the system configurations. It plays a crucial role in minimizing the risk of accidental or intentional misconfigurations, which could lead to security vulnerabilities or compliance issues.

**Technical Impact when configured:**

When enabled, the parameter hides specific sensitive keys in the Advanced Configuration, All Configuration, and SoD Resolver Configuration pages, preventing their exposure in the UI. This action safeguards system settings by allowing only authorized users to view or modify them, based on their access rights.

**Examples Scenario:**

- A company wants to ensure that critical system settings related to validation, role registry, and global administration are not accidentally altered or exposed to unauthorized personnel. By enabling this parameter, they can hide these settings from the general user interface, reducing the risk of unintended changes.

**Related Settings:**

- IsValidateInstallation
- ShowCSG
- SettingsKey
- RolesRegistryNodes
- GlobalAdministrator

**Best Practices:** 

- **Configure when:** It's essential to protect sensitive configuration settings from being accessed or modified by unauthorized users.
- **Avoid when:** If there is a requirement for broad transparency and access to configuration settings for auditing or training purposes, consider the implications carefully before enabling.