# Show SoD Combination Description

**Technical Name:** ShowSodCombinationDescription

**Category:** SOD

**Default Value:** 

**Impact Level:** Medium

**Description:** This parameter controls the visibility of the Segregation of Duties (SoD) combination descriptions in reports and user interfaces within the Pathlock Cloud GRC platform. When enabled, it provides detailed descriptions of each SoD combination, aiding in the understanding of potential security conflicts.

**Business Impact:** Enabling this feature helps stakeholders to understand the security and compliance implications of SoD conflicts within their organizational roles and permissions. This understanding is crucial for making informed decisions on role design, assignment, and SoD policy enforcement.

**Technical Impact when configured:** The visibility of detailed SoD combination descriptions in relevant Pathlock GRC interface sections and reports is toggled. This affects how administrators, audit teams, and compliance managers interpret SoD reports and resolutions.

**Examples Scenario:**
- An auditor reviewing SoD reports for compliance with regulatory standards can see not just the combinations of roles that represent a conflict, but also understand the nature and details of the conflict. This detailed insight aids in the auditing process and in crafting precise remediation plans.

**Related Settings:** 
- `IncludeRolesThatAreNotSafeToRemove`: Determines if roles deemed unsafe to remove are included in SoD analysis reports. This setting can impact which roles are considered when displaying SoD combination descriptions.

**Best Practices:** 
- Configure when: Detailed SoD analysis and reporting is required for thorough security and compliance reviews.
- Avoid when: Simplified reporting suffices or in environments where the additional information may overwhelm the stakeholders.