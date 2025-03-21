# Get Employee Roles By Active Directory User

**Technical Name:** GetEmployeeRolesByActiveDirectoryUser

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

This parameter is used to fetch roles assigned to employees based on their Active Directory User information within the Pathlock Cloud GRC platform. It plays a critical role in ensuring that employees have the appropriate access and permissions aligned with their organizational roles.

**Business Impact:**

Accurate mapping and retrieval of employee roles via Active Directory User information are vital for enforcing proper access controls and compliance standards. It ensures that employees have the necessary permissions to perform their tasks while preventing unauthorized access, thereby protecting sensitive information and reducing the risk of compliance violations.

**Technical Impact when configured:**

When configured, this parameter dynamically retrieves and assigns roles to users based on their current position in the organizational structure as reflected in Active Directory. This automation streamlines user management processes, reduces manual overhead, and decreases the likelihood of errors associated with manual role assignments.

**Examples Scenario:**

- **Scenario 1:** An employee is promoted within the organization. The Pathlock Cloud GRC platform, utilizing the `GetEmployeeRolesByActiveDirectoryUser` parameter, automatically updates the user's roles to reflect their new position, ensuring they gain access to the necessary resources without manual intervention.
  
- **Scenario 2:** A user's role changes due to a departmental shift. The system automatically revokes the previous permissions and grants new ones that align with the user's new role, maintaining strict adherence to the principle of least privilege.

**Related Settings:**

- `ReadActiveDirectoryEmployeeId`: Determines whether the system should read the employee ID from Active Directory for identity correlation.

**Best Practices:** configure when initializing user roles based on their organizational position, avoid when manual control over role assignment is preferred or in small environments where role changes are infrequent.