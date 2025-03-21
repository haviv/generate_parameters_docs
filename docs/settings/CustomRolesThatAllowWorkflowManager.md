# Custom Roles That Allow Workflow Manager

**Technical Name:** CustomRolesThatAllowWorkflowManager

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `CustomRolesThatAllowWorkflowManager` parameter is designed to help manage the roles that are authorized to modify, create, or interact with workflow instances within the Pathlock Cloud GRC platform. This pertains specifically to workflows that involve role authorization changes, highlighting its importance in the security and workflow management aspects of the platform.

**Business Impact:**

Configuring this parameter properly ensures that only authorized roles have the ability to make significant changes to role authorizations through workflows. This is crucial for maintaining the integrity of role-based access controls and preventing unauthorized access or changes to sensitive functionalities and data.

**Technical Impact when configured:**

- Ensures workflow management related to role authorization changes is limited to custom roles specified by this parameter.
- Enhances security by preventing unauthorized role modifications.
- Enables closer control over workflow processes, reducing the risk of security breaches or compliance issues.

**Examples Scenario:**

Consider an organization that uses the Pathlock Cloud GRC platform to manage its IT security, risk, and compliance. The organization decides to implement stricter controls over which employees can modify critical role authorizations. By configuring the `CustomRolesThatAllowWorkflowManager` parameter to include only senior IT security roles, the organization can ensure that only authorized personnel can initiate or approve changes to role authorizations through workflows.

**Related Settings:**

- `RunOneLevelSoDCheckInMemory`: Whether one-level Segregation of Duties (SOD) checks are performed in memory. This setting complements authorization management by ensuring role changes respect SOD policies.

**Best Practices:** 

- **configure when** you need to strictly control who can interact with and manage workflows related to role authorization changes within the Pathlock platform. This is particularly important in larger organizations or those with complex compliance and security requirements.
- **avoid when** there is no need to restrict workflow management capabilities to specific roles beyond the default platform access controls. This might be applicable in smaller organizations with less stringent security policies.