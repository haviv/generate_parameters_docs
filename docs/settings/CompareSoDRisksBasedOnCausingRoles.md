# Compare SoD Risks Based On Causing Roles

**Technical Name:** CompareSoDRisksBasedOnCausingRoles

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CompareSoDRisksBasedOnCausingRoles` parameter is utilized within the Pathlock Cloud GRC platform to enable or enhance the comparison of Segregation of Duties (SoD) risks by focusing on the roles that cause these risks. This parameter facilitates a more nuanced analysis of SoD risks, highlighting the specific roles contributing to potential security or compliance issues. 

**Business Impact:**

Activating or configuring this parameter helps organizations to pinpoint the exact roles responsible for SoD violations, thereby allowing targeted adjustments to roles or permissions. This targeted approach can significantly reduce the risk of fraud or non-compliance with internal or external regulations, improving overall security posture and compliance levels.

**Technical Impact when configured:**

- **Enhanced Visibility:** Provides clearer insights into how specific roles contribute to SoD risks.
- **Risk Management:** Facilitates more effective risk management by allowing the adjustment of roles or permissions to mitigate identified risks.
- **Audit Readiness:** Supports compliance and audit processes by offering detailed information on the origin of SoD risks.

**Examples Scenario:**

An organization notices an elevated risk in its financial approval process, potentially allowing a user to both approve expenditures and process reimbursements. By leveraging `CompareSoDRisksBasedOnCausingRoles`, the company can identify which specific roles provide these permissions, thereby violating SoD principles. Following this identification, the organization can restructure these roles to mitigate risk.

**Related Settings:**

- SoDSimulateTemplateForPrevious
- ShowPrintWorkflowRequests

**Best Practices:** configure when initiating a comprehensive security or risk assessment to ensure all sources of SoD risks are identified. Avoid using this setting without a clear strategy for responding to the identified risks, as merely highlighting risks without action does not reduce them.