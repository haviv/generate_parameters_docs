# Authorization Review For SoD Show Dynamic Data

**Technical Name:** AuthorizationReviewForSoDShowDynamicData

**Category:** SOD

**Default Value:** True

**Impact Level:** High

**Description:** This parameter controls the inclusion of dynamic violation and role-specific data within SoD (Segregation of Duties) authorization reviews. When enabled, it enriches the review details by adding information about the last usage of roles and the number of dynamic violation occurrences.

**Business Impact:** Enabling this setting provides a detailed view of potential security and compliance risks by highlighting dynamically identified violations and role activity. This facilitates informed decision-making in managing and mitigating SoD risks.

**Technical Impact when configured:** When enabled, the review reports will contain additional columns such as "Last Used" and "# of Dynamic Violations" for a more comprehensive overview. This allows for a deeper analysis of authorization data and helps in identifying problematic permissions more accurately.

**Examples Scenario:** 

- A compliance officer is reviewing authorization data to prepare for an upcoming audit. By having the "Authorization Review For SoD Show Dynamic Data" enabled, they can focus on roles that exhibit frequent dynamic violations and recent activity, thus prioritizing review efforts on high-risk areas.

**Related Settings:** AuthorizationReviewWideApproval_ShowSystem

**Best Practices:** 
- Configure when: Detailed audit trails and comprehensive SoD review reports are required for compliance and security management.
- Avoid when: The organization prefers high-level reviews without in-depth data analysis to minimize complexity in review processes.