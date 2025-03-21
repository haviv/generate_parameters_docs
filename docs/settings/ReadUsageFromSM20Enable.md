# Read Usage From SM20 Enable

**Technical Name:** ReadUsageFromSM20Enable

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

Enables the reading and analysis of SAP security audit logs (SM20) to identify and report on system access and activities. This parameter is crucial for organizations seeking to enforce security policies, monitor system usage, and detect potential breaches or unauthorized activities within their SAP environment.

**Business Impact:**

Activating this feature provides organizations with a comprehensive overview of user actions in the system, enhancing security and compliance by ensuring that only authorized activities are performed. This capability is vital for maintaining the integrity of sensitive information and for meeting external regulatory requirements.

**Technical Impact when configured:**

When enabled, this parameter allows the Pathlock Cloud GRC platform to connect with SAP's security audit log (SM20), gather data on user activities, and analyze these against predefined security policies. The analysis helps in identifying suspicious behaviors, potential security risks, or policy violations, enabling timely corrective actions.

**Examples Scenario:**

A company implements the Read Usage From SM20 Enable parameter to monitor access to its financial systems. It identifies an unauthorized attempt to access sensitive salary information outside of normal working hours, enabling the security team to investigate and address the issue promptly.

**Related Settings:**

- DailyEMailAddLinkToWaitingRequests
- DailyEMailLinkToWaitingRequestsText

**Best Practices:** configure when you need comprehensive monitoring and analysis of user activities within your SAP systems for security and compliance purposes. Avoid when the organization does not utilize SAP or where minimal auditing is sufficient.