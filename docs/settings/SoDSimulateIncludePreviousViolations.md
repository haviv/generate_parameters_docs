**SoD Simulate Include Previous Violations**

**Technical Name:** SoDSimulateIncludePreviousViolations

**Category:** Compliance

**Default Value:** False

**Impact Level:** High

**Description:**

This parameter controls whether the segregation of duties (SoD) simulation includes previous violations in its analysis. When enabled, the system will take into account prior SoD violations alongside current configuration and permission settings to assess potential risk exposure.

**Business Impact:**

Enabling this setting provides a more comprehensive view of SoD risks by considering historical violation data. This is critical for organizations seeking to maintain compliance over time and reduce the likelihood of repeat violations that could lead to audit failures or operational risks.

**Technical Impact when configured:**

If set to true, the simulation of forbidden combinations (SoD violations) will include data on previous violations, thus offering a broader risk assessment. This may impact the total number of risks identified in the simulation results, potentially increasing the volume of violations reported if past unresolved or mitigated risks are considered relevant.

**Examples Scenario:**

A scenario where this parameter is relevant could be during an audit preparation phase where an organization wants to evaluate its current compliance stance. By including previous violations in the simulation, the compliance team can identify whether past issues have been adequately addressed and if they pose any ongoing risk due to current system permissions or user roles.

**Related Settings:**

- `FilterRulesWithEffectWorkflow`
- `ShowAllRisksInRiskAnalysis`

**Best Practices:** Configure this parameter to true during comprehensive compliance reviews, risk assessment exercises, or ahead of audits for a thorough examination of SoD violations. Avoid enabling this feature for routine checks where the focus is strictly on new or active violations, as it may unnecessarily complicate the analysis with historical data that has already been addressed.