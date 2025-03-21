# SoD Simulate Template For Previous

**Technical Name:** SoDSimulateTemplateForPrevious

**Category:** SOD

**Default Value:** N/A

**Impact Level:** High

**Description:** The SoD Simulate Template For Previous parameter is used within the Pathlock Cloud GRC platform to determine if a simulated Segregation of Duties (SoD) risk assessment should consider combinations of roles or permissions that were previously not flagged as violations but might now be considered as such due to changes in the SoD rules or roles.

**Business Impact:** This parameter significantly impacts the organization's ability to proactively manage and mitigate risk by identifying new potential violations that were not detected in past assessments. It ensures that the organization's access controls remain robust in the face of changes, safeguarding against fraud and ensuring compliance with internal and external SoD policies.

**Technical Impact when configured:** When enabled, the system will include in its assessment any combinations of roles or permissions that have not been previously identified as violating SoD rules. This allows for a more dynamic risk management process, as it can adapt to updated definitions of what constitutes a risk.

**Examples Scenario:** For instance, if an organization updates its SoD rules to include a new potential conflict between two permissions, the SoD Simulate Template For Previous parameter, when configured, will ensure that any existing users who may now be in violation of this updated rule are identified in the simulation results. 

**Related Settings:** N/A

**Best Practices:** 
- **Configure when:** It's crucial to adjust this setting following any changes to SoD rules or role definitions within your GRC platform. This ensures all potential risks are accounted for based on the most current information.
- **Avoid when:** There may be specific instances, such as during initial rule configuration or when comprehensive auditing has been recently completed, where re-evaluating all past combinations might not be necessary or could lead to redundant work.