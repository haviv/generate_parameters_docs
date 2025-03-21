# Number of roles in solution factor

**Technical Name:** SodResolverConfig_RolesInSolutionFactor

**Category:** SOD

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter determines the influence of the number of roles involved in a solution when calculating the solution's overall ranking within the Pathlock Cloud GRC platform's Separation of Duties (SoD) conflict resolution process.

**Business Impact:**

Adjusting this factor can help organizations prioritize solutions that either minimize or maximize the roles count according to their security, compliance, and operational efficiency goals. An appropriate setting could enhance system security by ensuring that role assignments are optimized, thereby reducing unnecessary access rights and potential SoD violations.

**Technical Impact when configured:**

When configured, this parameter fine-tunes the SoD conflict resolution algorithm by attributing significance to the number of roles involved in a solution. This can lead to changes in how solutions are ranked, potentially affecting which solutions are recommended or selected for resolving SoD conflicts.

**Examples Scenario:**

- **Scenario:** An organization wants to prioritize solutions with fewer roles to simplify their access management and decrease the likelihood of SoD violations. By increasing the weight of the `Number of roles in solution factor`, solutions with fewer roles will be ranked higher, aligning the resolution process with the organization's simplification and compliance objectives.

**Related Settings:**

- `SodResolverConfig_CoveragePercentageFactor`
- `SodResolverConfig_ExtraFactor`

**Best Practices:** 

- **Configure when:** There is a clear organizational policy or preference towards minimizing the number of roles assigned to users for particular tasks or activities. This helps in maintaining a lean and more secure access environment.
  
- **Avoid when:** The organization's role design is complex and intentionally built with a high number of roles for flexibility and fine-grained access control. Increasing the weight of this factor in such scenarios may undesirably penalize solutions that leverage this design, potentially leading to suboptimal SoD resolutions.