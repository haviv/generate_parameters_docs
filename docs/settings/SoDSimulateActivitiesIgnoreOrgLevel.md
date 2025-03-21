# SoD Simulate Activities Ignore Org Level

**Technical Name:** SoDSimulateActivitiesIgnoreOrgLevel

**Category:** SOD

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter controls whether organizational levels are considered during the simulation of Segregation of Duties (SoD) activities within the Pathlock Cloud GRC platform. When enabled, the system ignores organizational hierarchies, allowing for a more streamlined and generalized simulation process.

**Business Impact:**

Enabling this feature can significantly impact an organization's ability to identify and mitigate risks related to SoD across different organizational levels. Ignoring organizational levels during simulation can lead to undetected risks in higher organizational structures where specific activities should not be segregated due to their inherent hierarchical oversight.

**Technical Impact: when configured**

When configured to ignore organizational levels in SoD simulation activities, the system will not differentiate between users or roles at different organizational levels. This configuration could lead to a broader acceptance of potential SoD violations that, in a more granular setup, would be identified and addressed.

**Examples Scenario:**

Consider an organization with a strict hierarchy, where certain approvals or transactions are segregated based on organizational levels to ensure checks and balances. If the SoD Simulate Activities Ignore Org Level parameter is enabled, the system may not flag a simulation where a user in a lower organizational level performs activities typically reserved for higher levels, potentially overlooking a critical SoD risk.

**Related Settings:**

- `DisableSoDApprovalBySameUser`

**Best Practices:** configure when

- You require a broad overview of SoD risks without the complexity of organizational hierarchies.
- Analyzing SoD risks in flat organizational structures where different levels do not impact the segregation duties significantly.

**avoid when**

- Your organization operates with a strict hierarchical structure where duties and responsibilities are clearly segregated by levels.
- There is a high risk of overlooking critical SoD violations that could lead to security breaches or non-compliance with internal or external regulations.