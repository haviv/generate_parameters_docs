# Enable Change Management

**Technical Name:** EnableChangeManagement

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

The EnableChangeManagement parameter is designed to control the activation of change management features within the Pathlock Cloud GRC platform. When enabled, it allows organizations to track, manage, and audit changes across their GRC environments, providing a layer of security and compliance management that ensures all modifications are monitored and controlled.

**Business Impact:**

Enabling change management is crucial for organizations that are subject to regulatory compliance requirements or those that seek to enforce stringent internal controls over their GRC processes. It ensures accountability by logging every change, supports compliance by maintaining a historical record of alterations, and enhances security by monitoring unauthorized changes.

**Technical Impact when configured:**

When configured, the system begins to track changes made within the GRC platform, including user modifications, system configuration changes, and policy updates. It may impact system performance slightly due to the additional logging activity but significantly improves auditability and control over the GRC environment.

**Examples Scenario:**

A company needs to comply with SOX regulations, which require stringent control over financial reporting systems. By enabling change management, the company can ensure that any changes to their GRC-related configurations or policies are logged, providing an audit trail for compliance purposes.

**Related Settings:**

- DisableAutomaticRebuildIndexes

**Best Practices:** Configure the EnableChangeManagement parameter in environments where regulatory compliance or internal controls necessitate detailed tracking and auditing of changes. Avoid enabling in development environments where frequent changes are made and which may not require the same level of scrutiny.