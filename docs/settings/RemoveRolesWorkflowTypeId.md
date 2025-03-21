**Technical Name:** RemoveRolesWorkflowTypeId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** Identifies the specific type of workflow designed to handle the removal of user roles within the Pathlock Cloud GRC platform. This parameter is crucial for ensuring that role assignments are accurately managed and updated to reflect current permissions and access controls.

**Business Impact:** Proper configuration of this parameter directly affects the organization's ability to maintain a secure and compliant access control environment. Misconfiguration may lead to inappropriate access levels being granted or revoked, posing potential security risks and compliance issues.

**Technical Impact when configured:** Streamlines the process for removing roles from users, ensuring that actions are carried out within the defined workflows. This contributes to the overall integrity of the security infrastructure by enforcing consistent and controlled changes to user roles.

**Examples Scenario:** An organization needs to revoke access privileges from a user who is changing departments or leaving the company. By configuring the `RemoveRolesWorkflowTypeId`, the system automates the removal of specific roles associated with that user, ensuring they no longer have access to sensitive or irrelevant resources.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** configure when implementing role-based access control changes, avoid when changes to roles and permissions are managed outside of the Pathlock platform.