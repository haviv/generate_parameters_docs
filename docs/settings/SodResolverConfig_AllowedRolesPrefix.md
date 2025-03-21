# SoD Resolver Config Allowed Roles Prefix

**Technical Name:** SodResolverConfig_AllowedRolesPrefix

**Category:** SOD

**Default Value:**

**Impact Level:** High

**Description:** This parameter is used in the context of SoD (Separation of Duties) resolution within the Pathlock Cloud GRC platform. It specifies a prefix to filter the roles considered during the SoD conflict resolution process.

**Business Impact:** Proper configuration of this parameter ensures that only relevant roles are evaluated during the SoD checks, streamlining the compliance process and reducing false positives. This can significantly impact the organization's ability to comply with internal and external audits and regulations by ensuring that only appropriate roles are considered for conflict resolution, thereby minimizing unauthorized access risks.

**Technical Impact when configured:** When set, this parameter limits the role evaluation scope during SoD resolution to those matching the specified prefix. This can lead to a more efficient resolution process by focusing on relevant roles, potentially reducing the computational load and improving the accuracy of SoD conflict detection and resolution.

**Examples Scenario:** For instance, if the "SodResolverConfig_AllowedRolesPrefix" is set to "FIN_", only roles that start with "FIN_" will be considered during the SoD resolution process. This is particularly useful in organizations where roles are prefixed based on their department or function, such as Finance (FIN_), Human Resources (HR_), etc., allowing for targeted SoD checks that align with organizational structures and access control policies.

**Related Settings:** 

**Best Practices:** configure when the SoD resolution process needs to be finely tuned to focus on specific types of roles, especially in large organizations with numerous roles. Avoid configuring this parameter without understanding the naming conventions and organizational role structure, as an inaccurate prefix can exclude relevant roles from the SoD resolution process, potentially leading to oversight of significant SoD conflicts.