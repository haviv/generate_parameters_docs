# Write Extension Dll To Log

**Technical Name:** WriteExtensionDllToLog

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables or disables the logging of extension DLL activities within the system. When enabled, actions performed by extension DLLs are recorded in the application's log, facilitating a detailed audit trail of DLL operations.

**Business Impact:**

Logging extension DLL activities aids in monitoring and auditing custom functionality extensions within the Pathlock GRC platform. It enhances the accountability and traceability of actions performed through these extensions, which is critical for compliance and security purposes.

**Technical Impact when configured:**

- **Enabled:** Every action taken by extension DLLs, including file uploads and configuration changes, is recorded in the system's log. This can aid in debugging, tracking unauthorized changes, and ensuring compliance with internal and external audit requirements.
- **Disabled:** Reduces log volume by not recording actions performed by extension DLLs. This could be beneficial in environments where performance is a concern or where DLL activities are deemed low risk.

**Examples Scenario:**

An organization has developed a custom extension for their Pathlock GRC platform to automatically upload certain compliance reports. Enabling 'Write Extension Dll To Log' would ensure that each time this DLL uploads a file or modifies a setting, the action is recorded. This provides an audit trail for compliance officers to verify that reports are being uploaded as required by their compliance framework.

**Related Settings:**

- WorkflowUploadForbiddenFileTypes

**Best Practices:** 

- **Configure when:** A detailed audit trail of extension DLL activities is required for compliance, security, or troubleshooting purposes.
- **Avoid when:** Log volume concerns outweigh the need for detailed tracking of DLL activities.