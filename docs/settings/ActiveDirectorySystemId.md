# Active Directory System

**Technical Name:** ActiveDirectorySystemId

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The ActiveDirectorySystemId parameter is used for identifying and integrating Active Directory (AD) usernames within the Pathlock Cloud GRC platform workflows and user management processes. 

**Business Impact:**

Incorporating AD with GRC processes enables streamlined user identity management, facilitates automated user provisioning and de-provisioning, and ensures that access rights and permissions are accurately managed according to the organization's security policies. This can significantly reduce the risk of unauthorized access and improve audit performance.

**Technical Impact when configured:**

When the ActiveDirectorySystemId is properly configured, it allows the system to map Pathlock platform users to their corresponding Active Directory (AD) identities. This integration aids in automating the workflow of granting or revoking access based on employee status changes, reflected in their AD user properties.

**Examples Scenario:**

For instance, if an employee's role changes within an organization, the GRC platform can automatically update its access permissions to align with the new role, leveraging the Active DirectorySystemId parameter for identification.

**Related Settings:**

- `IncludeEmployeeADUserNameInWorkflowParameters`
- `UserSelectionShowFullNameFromEmployee`

**Best Practices:** 

- **Configure when:** Setting up user management workflows that require integration with Active Directory for automated user provisioning and de-provisioning.
- **Avoid when:** Your organization does not use Active Directory for managing user identities, or if there is no requirement for integrating user management processes with AD.