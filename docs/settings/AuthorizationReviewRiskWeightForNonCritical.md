# Authorization Review Risk Weight For Non-Critical

**Technical Name:** AuthorizationReviewRiskWeightForNonCritical

**Category:** Risk

**Default Value:**

**Impact Level:** Medium

**Description:**

The AuthorizationReviewRiskWeightForNonCritical parameter determines the risk weight allocated to non-critical transactions or actions during an authorization review process within the Pathlock Cloud GRC platform. This parameter helps in categorizing and prioritizing non-critical activities based on their assigned risk weight, facilitating a more focused and streamlined authorization review.

**Business Impact:**

Adjusting the AuthorizationReviewRiskWeightForNonCritical parameter allows organizations to fine-tune their risk management strategies by identifying less critical but potentially risky actions. By assigning appropriate risk weights, organizations can ensure that their monitoring and control efforts are proportionately applied, thereby optimizing resource allocation and mitigating risks effectively.

**Technical Impact when configured:**

When configured, this parameter influences the reporting and oversight mechanisms within the GRC platform. It affects how non-critical authorization requests are flagged, reviewed, and audited, directly impacting the risk profiles generated for user activities and the overall security posture assessment reports.

**Examples Scenario:**

For example, if the platform identifies a user action that is deemed non-critical, such as accessing a low-sensitivity document, the AuthorizationReviewRiskWeightForNonCritical parameter helps in determining how much attention and priority this action receives during the review process compared to critical actions, thus ensuring critical resources are focused where they are needed most.

**Related Settings:**

- CommonSettings.Default.AuthorizationReviewForPositionChangeRunForAllOnlineSystems

**Best Practices:** 

- **Configure when:** You have clearly defined which actions within your system are considered non-critical but still require oversight. Adjust the weight to ensure a balanced approach to risk management that does not overlook less critical actions that could still pose a risk if abused.
  
- **Avoid when:** If all system actions are considered equally critical, or if the organization is not ready to differentiate actions based on risk weight due to a lack of clear guidelines or risk assessment policies, it's better to avoid using this setting to prevent an inaccurate risk profile.