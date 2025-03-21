# Additional activities factor

**Technical Name:** SodResolverConfig_ExtraFactor

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

The Additional activities factor parameter is designed to refine the process of resolving Segregation of Duties (SoD) conflicts within the Pathlock Cloud GRC platform. It enables a more granular control over the activities displayed and considered during the SoD conflict resolution process, allowing for a personalized approach to risk assessment and mitigation.

**Business Impact:**

Implementing this parameter can significantly enhance the organization's ability to manage and mitigate risk by allowing for the exclusion or inclusion of specific transactions and roles that are considered when identifying potential SoD conflicts. This can lead to a more efficient allocation of resources, reduced false positives, and a more accurate representation of the organization's risk posture.

**Technical Impact when configured:**

Upon configuration, this parameter affects the SoD resolution process by altering the set of activities (transactions and roles) that are considered. This can help in fine-tuning the application's behavior to align with the organization's specific compliance and risk management strategies, improving overall security and compliance performance.

**Examples Scenario:**

- A financial institution wants to ensure that high-risk transactions are scrutinized more closely for SoD conflicts. By configuring the Additional activities factor, they can specify these transactions to always be included in the analysis, regardless of other settings.

**Related Settings:**

- `SodResolver_ShowActivities`
- `SodResolver_MaxNoOfCombinationsToShow`

**Best Practices:** 

- **Configure when:** There is a need to tailor the SoD analysis to include or exclude specific activities that are critical to the business's operational or compliance requirements.
- **Avoid when:** The default SoD conflict resolution settings align well with the organization's risk tolerance and compliance requirements, as unnecessary configuration can complicate the SoD resolution process without providing significant benefits.