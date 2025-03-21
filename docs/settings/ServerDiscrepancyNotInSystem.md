# Server Discrepancy Not In System

**Technical Name:** ServerDiscrepancyNotInSystem

**Category:** Audit

**Default Value:** N/A

**Impact Level:** Medium

**Description:** Identifies discrepancies between the servers configured within the Pathlock platform and those recognized by the organization's Profile Tailor application.

**Business Impact:** Ensuring server configurations are accurately reflected and synchronized between Pathlock and Profile Tailor is crucial for maintaining the integrity of audit trails, compliance reporting, and security policies. Discrepancies may indicate configuration drift, unauthorized changes, or issues in deployment that could lead to compliance risks, security vulnerabilities, or operational inefficiencies.

**Technical Impact when configured:** Configuration of this parameter enables automated notifications and detailed reporting of discrepancies. This proactive measure helps in maintaining system integrity, compliance standards, and operational continuity by facilitating timely resolution of identified discrepancies.

**Examples Scenario:** If a new server is added to the organization's network and integrated into the Profile Tailor system but not registered within Pathlock's configurations, this discrepancy is flagged. The responsible teams receive an alert, prompting verification and appropriate action to ensure both systems reflect the current operational environment accurately.

**Related Settings:** 

- ServerDiscrepancyEmailSubject
- ServerDiscrepancyEmailTemplate

**Best Practices:** 

- **Configure when:** Regular monitoring and audit processes are in place, and there is a need for tight integration between Pathlock and other systems like Profile Tailor to ensure data consistency and compliance.
  
- **Avoid when:** The organization does not use Profile Tailor or similar systems where server discrepancies would not impact operational or compliance standards.