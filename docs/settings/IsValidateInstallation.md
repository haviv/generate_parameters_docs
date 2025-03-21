# Is Validate Installation

**Technical Name:** IsValidateInstallation

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The IsValidateInstallation parameter is designed to ensure the integrity and proper configuration settings of the Pathlock Cloud GRC platform. It checks for the correct installation of specific modules and the consistency of configuration settings across the system.

**Business Impact:**

Using the IsValidateInstallation parameter helps in preventing system misconfigurations, thus ensuring that the GRC platform operates as expected. This contributes to maintaining compliance standards and securing the IT environment against risks associated with incorrect configurations.

**Technical Impact when configured:**

When enabled, IsValidateInstallation performs an in-depth validation of the system's installation and configuration, identifying discrepancies, missing components, or misconfigurations, which might otherwise lead to system vulnerabilities or performance issues. 

**Examples Scenario:**

- Before activating new features or modules within the Pathlock Cloud GRC platform, enabling IsValidateInstallation can validate if the system meets all necessary configuration requirements, ensuring a smooth and error-free feature activation.
  
**Related Settings:**

- `CommonSettings`: This setting is involved in applying configuration changes and might be relevant when IsValidateInstallation is used to ensure these changes comply with the system's installation and configuration requirements.

**Best Practices:** 

- Configure when: You're making significant changes to the system, adding new features, or after a system upgrade to confirm the integrity of the installation.
  
- Avoid when: Making minor changes that do not affect the system's overall configuration or operational integrity, to reduce unnecessary system checks that could impact performance.