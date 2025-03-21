# SoD Resolver Config Exclude Roles With SoD

**Technical Name:** SodResolverConfig_ExcludeRolesWithSoD

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:**
This configuration parameter is used to exclude certain roles from Segregation of Duties (SoD) checks within the Pathlock Cloud GRC platform. When enabled, it ensures that specific roles identified by the system or administrators are not included in the SoD analysis process. This can be particularly useful for roles that are known to have inherent SoD conflicts by design and are accepted risks by the organization.

**Business Impact:**
Enabling this parameter can help reduce false positives in SoD violation reports, making them more accurate and easier for compliance officers to manage. It allows businesses to focus on real and actionable SoD conflicts, streamlining compliance efforts and ensuring that resources are allocated efficiently.

**Technical Impact when configured:**
When configured, this setting prevents specified roles from being evaluated for SoD conflicts. This can lead to a decreased number of identified SoD conflicts, allowing audit and compliance teams to focus on resolving genuine SoD risks. However, it requires careful configuration to ensure that only appropriate roles are excluded, as misconfiguration could inadvertently overlook significant SoD risks.

**Examples Scenario:**
Imagine an organization with specific administrative roles that require access across multiple functions for maintenance and monitoring purposes. These roles are designed with an understanding that they breach SoD principles but are managed with other controls. By applying the SodResolverConfig_ExcludeRolesWithSoD parameter, these roles can be exempted from SoD checks, thus avoiding unnecessary alerts and allowing the security team to focus on unintended SoD violations.

**Related Settings:**
- AuthorizationCertificationByActivitiesIncludeRoleName
- FioriConnectorIdentifyBasedOnCatalogs

**Best Practices:** 
- **Configure when:** you have roles that are known to inherently violate SoD rules but are accepted by the organization's risk posture, or when the organization wants to focus on high-priority SoD issues.
- **Avoid when:** every role's compliance status is important to the organization or when the organization has not developed a mature risk management strategy.