# Show All Risks In Risk Analysis

**Technical Name:** ShowAllRisksInRiskAnalysis

**Category:** Risk

**Default Value:** False

**Impact Level:** High

**Description:**

This parameter controls whether the risk analysis should show all the risks associated with business roles within the Pathlock Cloud GRC platform. When enabled, it provides a comprehensive view of all potential and mitigated risks, including Segregation of Duties (SoD) and Sox compliance risks, across business roles involved in the specified workflow instance.

**Business Impact:**

Enabling this setting ensures that risk managers and compliance officers have visibility into all risks, facilitating more informed decision-making. It aids in identifying hidden risk exposures that might not be immediately apparent, promoting a proactive risk management approach.

**Technical Impact when configured:**

Upon configuration, the system will include all identified risks within the impact analysis calculations, as opposed to filtering out already mitigated or accepted risks. This can lead to more extensive data processing and impact the performance of the risk analysis process, but ensures a thorough review of all potential risk exposures.

**Examples Scenario:**

A company wants to implement a new business role that encompasses critical financial transaction capabilities. By enabling Show All Risks In Risk Analysis, the risk management team can evaluate all associated risks—including those that have already been mitigated through controls or previously accepted—to ensure comprehensive analysis and decision-making.

**Related Settings:**

- EnableActiveDirectoryLastLogonDates (indirectly related through common settings infrastructure)

**Best Practices:** 

- **Configure when** you are conducting comprehensive risk assessments, especially in preparation for audits or when implementing significant changes to roles and access controls within the organization.
- **Avoid when** performing routine risk analysis where detailed visibility into already mitigated or accepted risks is not necessary, to optimize performance.