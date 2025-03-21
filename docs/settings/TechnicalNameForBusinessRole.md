**Technical Name:** TechnicalNameForBusinessRole

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The TechnicalNameForBusinessRole parameter is designed to associate specific business roles with technical roles or permissions within the Pathlock Cloud GRC platform. It helps in the automation and management of user roles and permissions based on business requirements.

**Business Impact:**

Proper configuration of this parameter ensures that users are granted access to the system and functionalities required for their roles, enhancing operational efficiency and security. Misconfiguration could lead to inappropriate access rights, affecting compliance and security stance.

**Technical Impact when configured:**

When configured accurately, it automates the role assignment process in workflow actions related to user creation and management. This ensures that users have the necessary permissions as per their business roles, aligning with security and compliance policies.

**Examples Scenario:**

- **Automated User Onboarding**: Automatically assign the required system roles to a new user based on their business role during the user creation process.
- **Role Adjustment in Role Change Scenario**: When an employee's business role is changed, the TechnicalNameForBusinessRole parameter helps in automatically updating the user's system roles to reflect their new responsibilities.

**Related Settings:**

- WorkflowUIComponentUtils.GetWorkflowInstanceId
- WorkflowManager.Instance.db.UserNamePatterns
- ProfileTailorContext.Context.SystemConnector

**Applicable Workflows Actions:** 

- AssignPositionToVMA
- CreateNewUser
- DerivedRolesSelector
- UserCreationManagement

**Best Practices:** configure when the business role to technical role mapping changes or new roles are introduced; avoid when business roles are stable, and no changes in role assignments are expected.