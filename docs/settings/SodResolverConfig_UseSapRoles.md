# Include SAP roles

**Technical Name:** SodResolverConfig_UseSapRoles

**Category:** SOD

**Default Value:** Not specified

**Impact Level:** High

**Description:**

This configuration parameter determines whether SAP roles should be considered during the resolution process of Segregation of Duties (SoD) conflicts within the Pathlock Cloud GRC platform. When enabled, the system filters and selects SAP roles based on specific criteria related to transaction permissions and SoD rule violations.

**Business Impact:**

Enabling this parameter ensures that only appropriate SAP roles, which do not contribute to SoD conflicts, are considered in SoD resolution proposals. This enhances the organization's ability to maintain robust security and compliance stances by preventing unauthorized access combinations through role assignments.

**Technical Impact: when configured**

- Filters out SAP roles that are associated with transactions leading to SoD conflicts.
- Promotes a more secure and compliant SAP environment by systematically excluding roles that could potentially violate SoD policies.
- Facilitates a more streamlined and efficient SoD conflict resolution process by focusing on roles that are compliant with organizational policies.

**Examples Scenario:**

An organization wishes to enforce strict SoD policies within their SAP system to comply with internal and external audit requirements. By configuring the `SodResolverConfig_UseSapRoles` parameter to include only compliant SAP roles, the Pathlock Cloud GRC platform can automatically filter and suggest roles that meet these criteria during the SoD resolution process. This avoids the manual effort of identifying and excluding roles that could lead to SoD violations, thereby reducing the risk of non-compliance.

**Related Settings:**

- SodResolverConfig_RolesInSolutionFactor

**Best Practices:** 

- **Configure when:** Implementing or enhancing SoD conflict resolution processes within SAP environments. It is especially useful in complex environments where manually identifying compliant roles is inefficient and prone to errors.
- **Avoid when:** The organization does not use SAP or if the SAP environment does not have defined SoD policies requiring enforcement through role selection.