# Get Roles By Business Role Take Data From Request

**Technical Name:** GetRolesByBusinessRoleTakeDataFromRequest

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter allows for the dynamic retrieval of roles based on the business role taken from the request within a workflow, specifically at the start step. When configured, it helps in determining the roles that need to be applied or removed from a user by comparing their current roles against the roles defined in a workflow request.

**Business Impact:**

Ensuring users have the correct roles according to business requirements is crucial for maintaining internal security policies and compliance with external regulations. The ability to dynamically adjust roles based on business role data from requests enhances flexibility and responsiveness in governance, risk management, and compliance (GRC) processes.

**Technical Impact when configured:**

When this parameter is configured, it provides a tailored list of roles for the user involved in the workflow by excluding the roles they already possess from the set of all roles determined by their business role. This ensures that the user is assigned only the roles they need without redundant or duplicate role assignments, optimizing efficiency and security.

**Examples Scenario:**

In an onboarding workflow, a new employee is assigned a business role. Based on this business role, the system uses the GetRolesByBusinessRoleTakeDataFromRequest parameter to fetch all relevant SAP roles for that business role. It then filters out any roles the employee might already have been assigned and proceeds to assign only the missing roles, ensuring efficient role management.

**Related Settings:** CommonSettings.Default.WorkflowRequestReplaceModeTechnicalName

**Best Practices:** configure when initiating workflows that require dynamic role assignment based on business roles. Avoid when static role assignments are sufficient or when the business role to roles mapping does not frequently change.