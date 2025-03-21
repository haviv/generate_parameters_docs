# Read Change Document When Detecting Dynamic SoD Violation

**Technical Name:** ReadChangeDocumentWhenDetectingDynamicSodViolation

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether the system reads change documents associated with Segregation of Duties (SoD) violations when they are dynamically detected. Enabling this feature allows for detailed tracking and mitigation of SoD risks by analyzing changes that might have led to current policy violations.

**Business Impact:**

Enabling this parameter strengthens the organization's risk management framework by ensuring timely detection and response to SoD violations. It directly impacts the integrity of financial reporting and compliance processes, thereby reducing the risk of fraud and non-compliance penalties.

**Technical Impact when configured:**

When this parameter is configured, the system will actively seek out and document any changes leading to or resulting from SoD violations. It involves tracking user and role-based modifications that could potentially violate defined SoD policies.

**Examples Scenario:**

- A user inadvertently is assigned an additional role that conflicts with their existing roles, leading to an SoD violation. With this parameter enabled, the system logs the change, aiding in quick remediation and policy enforcement.
  
- During an audit, investigators need a comprehensive log of actions leading to SoD breaches. Having this parameter enabled ensures that all relevant changes are recorded and easily accessible.

**Related Settings:**

- `SoxForbiddenCombiantionMitigates`
- `SoxForbiddenCombiantionMitigatesForRoles`

**Best Practices:** Enable this parameter in environments where SoD policy enforcement is critical, and detailed tracking of policy violations is required for compliance purposes. Avoid enabling in scenarios where performance impact is a concern or if detailed tracking is not necessary.