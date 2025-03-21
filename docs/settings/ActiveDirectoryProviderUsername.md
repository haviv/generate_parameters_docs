# Active Directory Provider Username

**Technical Name:** ActiveDirectoryProviderUsername

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The Active Directory Provider Username parameter specifies the username required to connect to and interact with Active Directory services. This setting is vital for integrating the Pathlock Cloud GRC platform with an organization's Active Directory (AD) to manage user identities, permissions, and access control seamlessly.

**Business Impact:**

Configuring the Active Directory Provider Username correctly ensures that the Pathlock Cloud GRC platform can efficiently manage security, compliance, and risk policies by leveraging the organizational structure and user information stored in Active Directory. It enables automated user provisioning, de-provisioning, and synchronization of user accounts, enhancing security and compliance posture.

**Technical Impact when configured:**

- Enables secure communication and data exchange with Active Directory services.
- Facilitates the automation of user account management tasks, such as creating, updating, and removing user access based on roles and policies defined in Pathlock Cloud GRC.
- Supports the enforcement of Segregation of Duties (SoD) policies by utilizing accurate and up-to-date user role information from Active Directory.

**Examples Scenario:**

1. Automating User Provisioning: Whenever a new employee is added to the HR system, the Active Directory Provider Username allows the Pathlock Cloud GRC platform to automatically create a user account in Active Directory, assign the correct permissions based on the employee's role, and ensure that the appropriate compliance and security policies are applied.

2. Continuous Compliance Monitoring: The platform utilizes the Active Directory Provider Username to continuously monitor Active Directory for any changes in user accounts, roles, or permissions, ensuring that any deviations from compliance policies are quickly identified and addressed.

**Related Settings:**

- ActiveDirectoryProviderPassword: Specifies the password associated with the Active Directory Provider Username for authentication purposes.

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for the first time or when changes are made to the Active Directory credentials.
  
- **Avoid when:** The provided username and password do not have the necessary permissions to read from Active Directory, as this will lead to integration failures.