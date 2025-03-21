# Ranking For Org Unit

**Technical Name:** RankingForOrgUnit

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `RankingForOrgUnit` parameter is designed to determine the order of organisational units based on their priority or importance within Pathlock Cloud GRC platform workflows. This parameter facilitates the prioritization of organizational units by assigning a rank, where a unit with a higher rank is given precedence over others.

**Business Impact:**

Adjusting the `RankingForOrgUnit` parameter can significantly impact how resources and risks are managed across different organizational units. By properly configuring the ranking, an organization can ensure that more critical units are prioritized, which is crucial for resource allocation, risk assessment, and compliance activities.

**Technical Impact when configured:**

Once configured, the `RankingForOrgUnit` parameter influences the execution order of workflow actions and decision-making processes within the Pathlock Cloud GRC platform. Configuration affects both automated and manual procedures in handling security, risk, and compliance, ensuring that high-ranked organizational units are addressed preferentially.

**Examples Scenario:**

- **Risk Assessment:** In a scenario where multiple organizational units are undergoing simultaneous risk assessments, the `RankingForOrgUnit` parameter ensures that units with higher ranks are assessed and addressed first, optimizing resource allocation and mitigation efforts.
  
- **Compliance Checks:** When scheduling compliance checks, this parameter can ensure that units with higher priority due to their sensitive nature, critical infrastructure, or higher data protection requirements are reviewed before others.

**Related Settings:** ProcessWorkHour, UserAccountExpirationDaysInWeek

**Best Practices:** configure when organizational units have varying levels of importance and require differentiated handling. Avoid over-complicating the ranking system to prevent confusion and ensure that all units are reviewed in a timely manner.