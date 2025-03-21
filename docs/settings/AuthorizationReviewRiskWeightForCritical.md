# Authorization Review Risk Weight For Critical

**Technical Name:** AuthorizationReviewRiskWeightForCritical

**Category:** Risk Management

**Default Value:** 

**Impact Level:** High

**Description:**

The `AuthorizationReviewRiskWeightForCritical` parameter plays a crucial role in the Pathlock Cloud GRC platform by influencing risk assessment calculations during authorization review processes. It determines the weight of risk assigned to critical authorization elements, impacting how risk prioritization and mitigation strategies are formulated.

**Business Impact:**

Adjusting the risk weight for critical authorizations directly affects the organization's ability to identify and prioritize security and compliance risks. A higher risk weight prompts more stringent reviews and potentially more aggressive mitigation efforts, thereby enhancing the overall security posture and compliance status of the organization.

**Technical Impact when configured:**

When this parameter is configured, it alters the risk calculation algorithms within the Pathlock platform. This adjustment affects the outcome of authorization reviews, leading to a potentially different set of recommendations or actions to address identified risks. It can lead to a focus on more critical areas, ensuring resources are allocated where they are most needed for maintaining or improving security and compliance.

**Examples Scenario:**

For instance, if the `AuthorizationReviewRiskWeightForCritical` parameter is set to a high value, critical permissions within the IT systems might undergo more rigorous scrutiny during reviews. This could result in identifying a critical permission misassignment that had been overlooked, leading to immediate action to revoke the misassigned permission and prevent potential security breaches.

**Related Settings:**

- AuthorizationReviewForPositionChangeRunForAllOnlineSystems
- ActiveDirectoryUserProvisionFallbackMode

**Best Practices:** 

- **Configure when:** Implementing or revising a risk management framework that requires differentiated handling of critical versus non-critical permissions.
  
- **Avoid when:** The organization lacks the resources to handle the increased workload that might result from a higher number of critical findings or if it might lead to too conservative an approach, potentially slowing down business processes without a commensurate increase in security.