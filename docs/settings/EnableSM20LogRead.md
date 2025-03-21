# Enable SM20 Log Read

**Technical Name:** EnableSM20LogRead

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The `EnableSM20LogRead` parameter controls the reading of SM20 audit logs within the Pathlock Cloud GRC platform. Enabling this option allows for advanced monitoring and analysis of SAP security logs, providing deep insights into system activities and potential security incidents.

**Business Impact:**

Enabling the `EnableSM20LogRead` feature is crucial for organizations needing to enhance security measures, comply with audit requirements, and identify fraudulent activities or unauthorized system changes. It supports adherence to internal and external compliance standards by facilitating detailed scrutiny of security-related events.

**Technical Impact when configured:**

When enabled, `EnableSM20LogRead` permits the extraction and analysis of SM20 logs, a component of SAP that logs security-related activities and changes in the system. This capability is essential for in-depth security investigations, audit trail reviews, and for maintaining a comprehensive security posture within the SAP environment.

**Examples Scenario:**

- **Compliance Auditing:** A financial institution is required to adhere to strict regulatory standards that mandate the continuous monitoring of system access and changes. Enabling `EnableSM20LogRead` allows the institution to automatically gather and analyze security logs, ensuring compliance and simplifying audit processes.
- **Security Monitoring:** Following the detection of unauthorized access in its SAP system, a manufacturing company enables `EnableSM20LogRead` to monitor for similar incidents proactively. This early detection and response mechanism helps in preventing potential data breaches and system misuse.

**Related Settings:**

- `EnableGrantingAuthObjectToRolesSimulation`
- `ActiveDirectoryFileMonitoringIgnorePaths`

**Best Practices:** Enable `EnableSM20LogRead` in environments where security monitoring and compliance are of paramount importance. Avoid enabling it in systems where performance is a critical concern without proper assessment, as continuous log reading may impact system resources.