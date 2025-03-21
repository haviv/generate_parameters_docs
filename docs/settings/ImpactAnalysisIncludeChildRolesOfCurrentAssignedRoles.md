# Impact Analysis Include Child Roles Of Current Assigned Roles

**Technical Name:** ImpactAnalysisIncludeChildRolesOfCurrentAssignedRoles

**Category:** Risk

**Default Value:** False

**Impact Level:** Medium

**Description:**

This setting controls whether the impact analysis for changes in user roles should include the evaluation of child roles associated with currently assigned roles. When enabled, the impact analysis process will take into consideration not only the direct roles being added or removed but also any subsidiary roles that are hierarchically under the direct roles.

**Business Impact:**

Enabling this feature ensures a more comprehensive analysis of potential risks, as it accounts for the permissions and access levels inherited by child roles. This is particularly important in complex authorization structures where parent roles encompass wide-ranging access through their child roles.

**Technical Impact when configured:**

- When set to True, the system performs a deeper analysis, including all underlying roles which could increase the time taken for impact analysis but results in a thorough risk assessment.
- When set to False, the system limits the analysis to the direct roles being assigned or removed, which may decrease the time taken for analysis but could overlook potential risks introduced by inherited child roles.

**Examples Scenario:**

A user is granted a new role that has several child roles. Each child role grants access to different systems or data:

- If this setting is disabled (`False`), the impact analysis would not consider the access granted by child roles, potentially missing out on identifying significant security or compliance risks.
- If this setting is enabled (`True`), the impact analysis would include all child roles, thereby identifying any access that could violate segregation of duties policies or introduce undue risk.

**Related Settings:**

- `SendWorkflowAdminMailTemplateToFallbackApprovalGroup`

**Best Practices:** 

- **Configure when:** a thorough risk assessment is required, especially in environments with complex role hierarchies to ensure all potential access risks are evaluated.
- **Avoid when:** quick impact analysis is preferred over depth of analysis, especially in less complex environments where roles have fewer or no child roles.