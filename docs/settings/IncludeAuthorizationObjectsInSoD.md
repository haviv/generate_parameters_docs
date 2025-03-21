**Include Authorization Objects In SoD**

**Technical Name:** IncludeAuthorizationObjectsInSoD

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls whether authorization objects are included in the analysis of Segregation of Duties (SoD) within the Pathlock Cloud GRC platform. Authorization objects are the specific permissions or rights assigned to users or roles within systems that determine what actions the users can perform. Including these objects in SoD analysis enhances the accuracy and depth of SoD violation detection.

**Business Impact:**

Including authorization objects in SoD analysis helps organizations identify and mitigate the risks associated with inappropriate access rights. This thorough analysis ensures that organizational policies around access control are adhered to, thereby reducing the risk of fraud, data breaches, and compliance violations.

**Technical Impact when configured:**

When enabled, the analysis takes into account the detailed permissions within roles or user profiles, leading to a more comprehensive identification of potential SoD conflicts. This configuration may increase the complexity and runtime of the analysis but results in more precise and actionable findings.

**Examples Scenario:**

An organization has two critical transactions that should not be performed by the same user: creating vendors and paying vendors. By including authorization objects in the SoD analysis, the platform can identify not only users who have both these transactions assigned but also delve deeper into the specific permissions within those transactions, catching more nuanced access controls that could still pose a risk.

**Related Settings:**

- SoxForbiddenCombination
- AuthorizationBuffer
- ActivityMode

**Best Practices:** 

- **Configure when**: Comprehensive SoD analysis is crucial for your organization's security and compliance posture. Particularly beneficial in environments with complex authorization models or when granular access control is implemented.
  
- **Avoid when**: Quick, high-level scans are required without the need for deep dive analysis into each authorization object, or when system performance is a concern due to the extensive data processing required.