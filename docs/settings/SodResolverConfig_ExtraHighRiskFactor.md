# Additional high risk activities factor

**Technical Name:** SodResolverConfig_ExtraHighRiskFactor

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** This parameter is used within the SoD (Segregation of Duties) conflict resolution process. It adjusts the emphasis placed on high-risk activities when calculating the priority of solutions. The value of this parameter influences the ranking of potential fixes by highlighting those that address the most critical risks first.

**Business Impact:** Adjusting this factor can significantly affect the risk posture of an organization by prioritizing the resolution of the most significant security and compliance violations. It helps in focusing efforts on mitigating high-impact risks, thus enhancing the overall security and compliance stance.

**Technical Impact when configured:** Modifying this parameter affects how solutions are prioritized and presented during the SoD conflict resolution process. Increasing the value places a higher emphasis on resolving conflicts involving high-risk activities, potentially changing the order in which solutions are considered and implemented.

**Examples Scenario:** If an organization identifies that unauthorized access to financial records is a serious risk, increasing the `SodResolverConfig_ExtraHighRiskFactor` would prioritize solutions that mitigate this risk over others that might affect less sensitive parts of the system.

**Related Settings:** 

- `SodResolverConfig_CoveragePercentageFactor`: Determines the weight of coverage percentage in the solution score.

**Best Practices:** Configure this parameter to a higher value when the organization is in a high-regulatory environment or has identified specific high-risk activities that need immediate attention. Avoid high values in less sensitive environments to prevent less critical issues from being deprioritized unnecessarily.