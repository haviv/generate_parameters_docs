
# ImpactAnalysisShowControlsFromCombinationOnlyHideMigitaionBoxForOtherRisks Parameter Documentation

## Category:
Security & Compliance

## Default Value:
Not specified in the code provided. Please refer to the application's global settings or documentation for the default setting.

## Impact Level:
High

## Description:
This parameter controls the visibility and behavior of UI elements related to mitigation controls and forbidden risk combinations within certain workflows. When enabled, it ensures that mitigation options are only displayed for risks associated with a specific forbidden combination, while hiding these options for all other types of risks.

## Business Impact:
Enabling this setting can streamline the workflow for users by showing only the relevant mitigation controls tied to specific risk combinations, potentially reducing confusion and ensuring that mitigation efforts are focused correctly. It helps in maintaining a clear and effective approach towards risk mitigation, making the user experience more intuitive in risk management tasks.

## Technical Impact when configured:
- The visibility of mitigation control dropdowns or options within the specified workflow context is conditional based on the presence of forbidden risk combinations.
- Ensures that the system focuses on displaying controls only for configured risk combinations, making other risks appear less cluttered by hiding mitigation-related UI elements.
- Can impact how users interact with the application's risk management features by either simplifying or limiting their options based on the context.

## Example Scenario:
In a scenario where an organization has identified specific combinations of actions or permissions that pose a particular risk, this parameter can be activated to ensure that only those combinations receive focus in the workflow. For example, if a combination of "Access to Financial Records" and "Bank Account Modification" is flagged as a forbidden risk combination, enabling this setting would hide mitigation options for risks not part of this combination, thus highlighting and prioritizing the mitigation efforts for the critical risk combination.

## Related Settings:
- RiskIdentificationParameters: May influence what is considered a risk or a forbidden combination.
- MitigationControlVisibilitySettings: General settings that may affect the visibility of mitigation controls across the application.

## Best Practices:
- **Configure when**: There is a clear distinction and understanding of which risk combinations require specific mitigation controls. It's especially useful in environments where risk management is prioritized, and certain risk combinations are identified as critical.
- **Avoid when**: The determination of risky combinations is not clear, or if users require visibility into all available mitigation options to make informed decisions across a variety of risks.

## Context:
This parameter is part of the risk management configuration in the ProfileTailor GRC application. It plays a critical role in customizing the user experience and effectiveness of risk management workflows by tailoring the visibility of controls and mitigation options based on the configuration of risky combinations.
