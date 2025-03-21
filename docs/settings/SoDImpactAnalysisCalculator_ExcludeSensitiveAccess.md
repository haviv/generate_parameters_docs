# SoD Impact Analysis Calculator Exclude Sensitive Access

**Technical Name:** SoDImpactAnalysisCalculator_ExcludeSensitiveAccess

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:**

The parameter configures the SoD (Segregation of Duties) Impact Analysis Calculator to exclude specific access rights identified as sensitive from the analysis process. This ensures that sensitive accesses are not inadvertently granted during role assignments or changes, supporting comprehensive security management and compliance enforcement.

**Business Impact:**

Excluding sensitive access from SoD impact analysis helps organizations prevent unauthorized access to critical systems and data, reducing the risk of internal fraud, data breaches, and compliance violations. It enables tighter control over the assignment of sensitive roles, ensuring that only authorized personnel can access high-risk or confidential information.

**Technical Impact when configured:**

When this parameter is configured, the impact analysis calculation will disregard any roles or permissions marked as sensitive. This means that these elements will not trigger an SoD conflict alert, allowing for focused analysis on non-sensitive role combinations. This adjustment is crucial for organizations that need to streamline their role management processes without compromising on security or regulatory compliance.

**Examples Scenario:**

A company implements a new policy requiring that access to financial reporting tools is considered sensitive. By configuring this parameter, when users are evaluated for potential role changes or new role assignments, access to these tools is excluded from the SoD analysis. This prevents unnecessary SoD conflict alerts from being triggered due to the sensitive nature of this access, focusing reviews on actual risky combinations of roles.

**Related Settings:**

- `ImpactAnalysisIncludeChildRolesOfCurrentAssignedRoles`
- `SodViolationMitigationForUserWillExpireSoonDays`

**Best Practices:** configure when excluding specific sensitive accesses from SoD analysis is necessary to focus on significant role combinations and streamline the user access review process. Avoid when comprehensive analysis including all available roles and access rights is required for complete risk assessment and compliance.