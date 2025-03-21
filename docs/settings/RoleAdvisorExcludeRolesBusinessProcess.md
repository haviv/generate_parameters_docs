# Role Advisor Exclude Roles Business Process

**Technical Name:** RoleAdvisorExcludeRolesBusinessProcess

**Category:** Configuration

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:** This parameter controls the inclusion or exclusion of roles based on certain criteria such as role name, description, parent role presence, and associated transactions within the business processes.

**Business Impact:** Proper configuration of this parameter can lead to a more streamlined and efficient role discovery process by excluding irrelevant roles from advisories, enhancing security posture and compliance by ensuring only relevant roles are considered for analysis.

**Technical Impact when configured:** Allows the system to efficiently filter out roles that do not meet the specified criteria, reducing the processing load and focus on roles that are significant to the business processes being analyzed.

**Examples Scenario:** 
- If a company wants to focus on analyzing roles related to a specific transaction code without the noise of unrelated roles, configuring this parameter to exclude roles not associated with the specified transaction code will sharpen the focus of the analysis.

**Related Settings:** PerformWorkflowActionsInBackground

**Best Practices:** 
- Configure when you have a clear understanding of the roles and transactions that are relevant to your GRC objectives to avoid inadvertently excluding important roles.
- Avoid when comprehensive role analysis is required without any preconception of which roles may or may not be relevant.