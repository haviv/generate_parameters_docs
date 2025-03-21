# Include composite roles

**Technical Name:** SodResolverConfig_UseCompositeRoles

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

The `Include composite roles` parameter controls whether composite roles (roles made up of multiple other roles) are included in the Separation of Duties (SoD) conflict resolution process. This is crucial for a comprehensive analysis of user permissions and potential SoD violations within complex role hierarchies in an organization's IT environment.

**Business Impact:**

Enabling this feature ensures a more accurate and thorough analysis of SoD conflicts by accounting for the combined permissions of composite roles. It aids in identifying potential risks and vulnerabilities that might not be visible when only considering single, non-composite roles. This can impact the organization's ability to prevent fraud, unauthorized access, and compliance issues.

**Technical Impact when configured:**

When configured, this setting allows the SoD Resolver to include or exclude composite roles during the conflict resolution process. This can influence the number of conflicts detected and the suggestions for conflict mitigation. 

**Examples Scenario:**

An organization utilizes SAP for its ERP needs. Within their SAP environment, they have defined both single roles and composite roles that bundle several single roles for ease of assignment. By enabling the `Include composite roles` parameter, the organization can ensure that the SoD analysis takes into account all the permissions granted by both single and composite roles, thereby providing a holistic view of access risks.

**Related Settings:**

- SodResolverConfig_ExtraFactor

**Best Practices:** Configure when aiming for a detailed and comprehensive SoD analysis, especially in complex IT environments with nested role structures. Avoid when unnecessary to minimize processing time and complexity if your organization does not use composite roles extensively.