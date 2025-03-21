**Enable Active Directory Connector Remote Event Log Events**

**Technical Name:** EnableActiveDirectoryConnectorRemoteEventLogEvents

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the ability of the Pathlock Cloud GRC platform's Active Directory Connector to access and process remote event log events. Enabling this feature allows the connector to gather detailed event logs from remote servers, enhancing monitoring and analysis capabilities for security and compliance purposes.

**Business Impact:**

Enabling this feature enhances the organization's security posture by providing more detailed logs for analysis, which can be crucial for identifying malicious activity or compliance issues early. It can also aid in forensic investigations by providing a more comprehensive event timeline across different servers.

**Technical Impact when configured:**

When enabled, the Active Directory Connector will attempt to access remote event logs from the specified servers. This can increase network traffic and require additional permissions setup to allow for remote access to these logs.

**Examples Scenario:**

An organization wants to ensure they have detailed audit logs of all Active Directory related changes and access attempts across their network, not just from the local server. By enabling this parameter, they can capture a wide array of events from multiple servers, centralizing their monitoring and increasing their ability to detect and respond to potential security threats.

**Related Settings:**

- `EmploymentStatusForActiveEmployee`

**Best Practices:** 

- Configure when: There's a need for detailed auditing and monitoring across multiple servers, particularly in environments with heightened security requirements or when compliance with specific regulations necessitates comprehensive logging.
- Avoid when: The organization lacks the network infrastructure or permissions setup to support remote log access, or when the increased network traffic would significantly impact system or network performance.