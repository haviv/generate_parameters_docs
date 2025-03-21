# Include Unassigned Roles

**Technical Name:** SodResolverConfig_UseUnassignedRoles

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SodResolverConfig_UseUnassignedRoles` parameter controls whether unassigned roles are considered during the SoD (Segregation of Duties) conflict resolution process within the Pathlock Cloud GRC platform. Enabling this parameter includes roles that have not been assigned to any user in the SoD analysis.

**Business Impact:**

Including unassigned roles in the SoD analysis can help organizations proactively identify and manage potential SoD conflicts before roles are assigned to users. This preemptive approach enhances the security posture by ensuring that roles, even those not currently in use, do not create unintended access conflicts that could be exploited in the future.

**Technical Impact when configured:** 

When enabled, this configuration broadens the scope of SoD conflict detection and resolution efforts to include roles not assigned to any users. This ensures a comprehensive review of all available roles within the system against defined SoD rules and policies, facilitating a proactive rather than reactive risk management strategy.

**Examples Scenario:**

A company implements a new financial approval role but has not yet assigned it to any users. With `SodResolverConfig_UseUnassignedRoles` enabled, during the SoD analysis, the system includes this new role in its checks against existing roles for potential conflicts. This allows the company to address any SoD conflicts before the role is activated and used, therefore mitigating any unseen risks.

**Related Settings:**

- `SodResolverConfig_AllowedRolesPrefix`
- `SodResolverConfig_UsageDaysBack`

**Best Practices:** 

- **Configure when:** There's a need for comprehensive SoD checks that include roles planned for future use but not yet assigned. This is particularly relevant when new roles are frequently created but their assignments are delayed until a later date.
  
- **Avoid when:** The organization prefers to focus SoD analysis strictly on active roles that are already assigned to users, hence minimizing the scope of the analysis for quicker results.