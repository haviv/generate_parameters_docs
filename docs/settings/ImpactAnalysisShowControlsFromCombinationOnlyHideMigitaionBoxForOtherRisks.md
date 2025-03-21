# Impact Analysis Show Controls From Combination Only Hide Migitaion Box For Other Risks

**Technical Name:** ImpactAnalysisShowControlsFromCombinationOnlyHideMigitaionBoxForOtherRisks

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:** This parameter controls the visibility of the mitigation options within the workflow for risks in the Pathlock Cloud GRC platform. When enabled, it limits the display of control options to only those that are part of a predefined combination, and hides the mitigation box for other unrelated risks.

**Business Impact:** Enhancing the focus on relevant mitigation measures streamlines the risk management process. This can lead to more effective and efficient control over potential security, compliance, or operational risks, directly impacting the organization's ability to safeguard its assets and reputation.

**Technical Impact when configured:** Once configured, the drop-down list within the risk workflow will exclude generic mitigation options and instead, highlight specific controls related to the risk combination under assessment. This limitation aids in preventing the selection of irrelevant or ineffective controls.

**Examples Scenario:** If an organization identifies a risk related to "Unapproved Access to Financial Records," this setting, when enabled, would ensure that the mitigation options presented are only those related to the specific access and security controls for financial records, rather than all potential access controls within the system.

**Related Settings:** ActiveDirectoryProviderCalculateEmploymentStatusBasedOnADStatus (It's important to ensure that employment status, which could affect mitigation strategies, is accurately calculated and considered when this feature is in use).

**Best Practices:** 
- **Configure when:** You have clearly defined risk-control combinations and want to ensure that the mitigation efforts are focused and relevant.
- **Avoid when:** The organization's risk profile is highly dynamic, or when a broader set of potential mitigations could be relevant for review and consideration.