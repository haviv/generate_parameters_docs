# Server Discrepancy Not In PTD

**Technical Name:** ServerDiscrepancyNotInPTD

**Category:** Audit

**Default Value:** Not specified

**Impact Level:** High

**Description:**

The `ServerDiscrepancyNotInPTD` parameter is designed to identify discrepancies between the application servers configured within the Pathlock platform (Profile Tailor) and those recognized or registered within the organizational environment. It serves as a critical audit and control measure to ensure all application servers are accounted for and monitored within the Profile Tailor's configuration.

**Business Impact:**

Untracked or unregistered application servers can pose significant security and compliance risks, including unauthorized access, data breaches, and failure to comply with regulatory standards. The `ServerDiscrepancyNotInPTD` parameter helps in mitigating these risks by bringing attention to discrepancies that need to be resolved to maintain integrity, security, and compliance of IT assets.

**Technical Impact when configured:**

Upon configuration, the system actively monitors and reports discrepancies between the servers listed in the Profile Tailor and those present in the application environment. This enables IT security and audit teams to take timely actions to either register missing servers with the Profile Tailor or investigate and rectify any unauthorized or rogue servers operating within the environment.

**Examples Scenario:**

- **Detecting Unauthorized Servers:** The parameter alerts administrators to the existence of servers operating within the organizational network that have not been registered in the Profile Tailor, indicating potential unauthorized or rogue servers.
  
- **Auditing and Compliance:** During an audit, auditors can use the discrepancies reported by this parameter to verify that all application servers are accounted for and compliant with internal policies and external regulatory requirements.

**Related Settings:** 

- `SendWorkflowReminder` 
- `SendWorkflowReminderEvery` 

**Best Practices:** 

- **Configure when:** Regularly auditing server configurations and ensuring compliance with security policies.
  
- **Avoid when:** If the organizational infrastructure requires frequent changes and cannot ensure timely updates to the Profile Tailor configurations, consider more dynamic monitoring solutions alongside this parameter to manage the fluid environment effectively.