# Read Fiori Service Descriptions

**Technical Name:** ReadFioriServiceDescriptions

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `ReadFioriServiceDescriptions` parameter is designed to control access to Fiori service descriptions within the Pathlock Cloud GRC platform, specifically within SAP environments. This configuration helps ensure that only authorized users can read the service descriptions, contributing to maintaining the security and integrity of the system's configuration.

**Business Impact:**

Restricting access to Fiori service descriptions prevents unauthorized viewing or alteration of service metadata, which could potentially lead to system vulnerabilities or misuse. Ensuring that only specific roles have access helps in maintaining system compliance with internal policies and external regulations.

**Technical Impact when configured:**

When properly configured, this parameter strengthens system security by limiting read access to Fiori service descriptions to authorized personnel only. This limitation helps protect against unauthorized access and potential security breaches by ensuring that sensitive information related to Fiori services is not exposed to unqualified individuals.

**Examples Scenario:**

- **Scenario 1:** An organization wants to ensure that their Fiori applications' service descriptions are not accessible by general users to prevent any unauthorized configuration changes or data exposure. They would enable `ReadFioriServiceDescriptions` for specific administrative roles.

**Related Settings:**

- SERVICE_CALL
- ActivitySelectorConfigurationFilterAttributes.Attribute1

**Best Practices:** 

- **Configure when:** You need to secure access to Fiori service descriptions to authorized personnel within your SAP environment. This is particularly important in environments where security and compliance are tightly managed.
  
- **Avoid when:** All users require access to Fiori service descriptions for their operations. However, consider implementing other controls to mitigate potential security risks.