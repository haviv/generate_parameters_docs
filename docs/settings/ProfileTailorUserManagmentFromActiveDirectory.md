# Pathlock User Management From Active Directory

**Technical Name:** ProfileTailorUserManagmentFromActiveDirectory

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:** 

This parameter governs the integration of Pathlock Cloud GRC platform with Active Directory for user management, facilitating the seamless import and synchronization of user accounts and related details from Active Directory to Pathlock's User Management module.

**Business Impact:**

Proper configuration ensures that user data remains consistent across business systems, improving security by leveraging existing Active Directory accounts. This eliminates the need for separate account management, reduces administrative overhead, and enhances overall compliance posture by using up-to-date access controls.

**Technical Impact when configured:**

- Enables automatic user provisioning and de-provisioning based on Active Directory status, ensuring user access rights in Pathlock are always current.
- Integrates role and access management seamlessly, allowing for alignment with organizational structure and access policies defined in Active Directory.

**Examples Scenario:**

A large organization with multiple departments and varying levels of access requirements can use this feature to automate the process of user access management. When a new employee is added to Active Directory, their account is automatically created in Pathlock with predetermined access rights based on their role and department. Similarly, if an employee leaves the organization and their account is deactivated or removed from Active Directory, their access in Pathlock is also automatically revoked.

**Related Settings:**

- `PowerShelllExePath`: Path to the PowerShell executable used for executing Active Directory related scripts.
- `HideWorkflowInProfileTailorHeader`: This setting might indirectly impact the visibility of certain workflow actions in the ProfileTailor module. Although not directly related to user management, it could affect administrative workflows.

**Best Practices:** 

- **Configure when**: You have a large number of users to manage and want to automate user account synchronization between Active Directory and Pathlock.
- **Avoid when**: Your organization does not use Active Directory, or there are specific reasons to manage Pathlock user accounts separately.