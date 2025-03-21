# Update Active Directory Properties On Terminate User Action

**Technical Name:** UpdateActiveDirectoryPropertiesOnTerminateUserAction

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

This parameter controls the behavior of updating Active Directory properties when a user's account is terminated in the Pathlock Cloud GRC platform. When enabled, this ensures that the termination process is comprehensive by extending beyond the GRC platform to include the user's Active Directory (AD) profile, thus maintaining system integrity and security.

**Business Impact:**

Enabling this feature reduces security risks associated with inactive users still having valid credentials in Active Directory. It helps in enforcing access control policies by ensuring terminated users lose access to all integrated systems immediately upon termination, thus protecting sensitive information and reducing the risk of unauthorized access.

**Technical Impact: when configured**

Once configured, the system will automatically update the Active Directory properties related to the terminated user. This can include disabling the account, removing the user from certain groups, or even deleting the account, depending on the organization's policy. This ensures that the user's access is promptly revoked from all areas within the organization's network.

**Examples Scenario:**

- **Scenario:** In the case of an employee termination, the HR department initiates the termination process in the Pathlock Cloud GRC platform. With the UpdateActiveDirectoryPropertiesOnTerminateUserAction parameter enabled, not only will the user be deactivated in the GRC platform, but their associated Active Directory record will be updated to reflect this change. This could include disabling the user account, ensuring that the user cannot access organizational resources through their Active Directory credentials.

**Related Settings:**

- ActiveDirectoryConnector
- CUASystemId

**Best Practices:** 

- **Configure when:** Immediate revocation of access upon user termination is vital for your security policy. It should also be enabled if your organization relies heavily on Active Directory for access management across various services.
  
- **Avoid when:** If the organization uses a manual process for updating Active Directory properties or if there is a dedicated team that handles these updates outside of the termination workflow, to prevent potential conflicts.