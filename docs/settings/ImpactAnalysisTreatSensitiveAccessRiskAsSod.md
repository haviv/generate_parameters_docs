# Impact Analysis Treat Sensitive Access Risk As SoD

**Technical Name:** ImpactAnalysisTreatSensitiveAccessRiskAsSod

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** Determines if sensitive access risks within the GRC platform are to be treated as segregation of duties (SoD) risks, affecting how these risks are identified and managed.

**Business Impact:** Treating sensitive access risks as SoD risks emphasizes the critical nature of managing privileged accesses and enforces stricter controls and oversight. It directly impacts an organization's ability to maintain a secure, compliant, and risk-aware environment.

**Technical Impact when configured:** Configuring this parameter to treat sensitive access risks as SoD will extend the SoD control framework to include sensitive access considerations, enabling more comprehensive risk detection and mitigation strategies.

**Examples Scenario:** If an employee has access to both create and approve financial transactions, treating this as an SoD risk ensures that such access combinations are flagged and reviewed to prevent potential fraud.

**Related Settings:** 

- `CommonSettings.Default.CompareSoDRisksBasedOnCausingRoles`

**Applicable Workflows Actions:** 

**Best Practices:** 
- Configure when: aiming to strengthen internal controls over sensitive access and to align with stringent audit and compliance requirements.
- Avoid when: the organizational control environment can adequately manage sensitive access risks without categorizing them as SoD risks, or if such categorization could result in operation inefficiencies without significant risk mitigation benefits.