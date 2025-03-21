# Create New User Delay After Creation

**Technical Name:** CreateNewUser_DelayAfterCreation

**Category:** User Management 

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter controls the delay after a new user account creation within the Pathlock Cloud GRC platform. It is designed to set a waiting period before the new user can start performing activities or access certain areas of the platform. This can be essential for synchronizing with other user management activities or systems.

**Business Impact:**

Implementing a delay after creating new users ensures that all necessary backend processes, such as access rights provisioning, security checks, and compliance validations, are completed before the user gains access. It helps in mitigating the risk of unauthorized access and ensuring that new users have a seamless onboarding experience with the correct access permissions.

**Technical Impact when configured:**

When configured, this parameter introduces a defined waiting period before a new user's account becomes fully active. This delay allows system administrators to ensure that all user-related configurations and security protocols are properly applied, thus enhancing the overall security posture and compliance of the organization.

**Examples Scenario:**

- **Scenario 1:** After creating a new user in the Pathlock Cloud GRC platform, the organization wants to ensure that automated processes for setting up access permissions and roles are fully completed. They set up a delay to prevent the user from logging in and accessing incomplete or incorrect configurations.

**Related Settings:**

No directly related settings were identified in the provided code references.

**Best Practices:** 

- **Configure when:** a new user has been added to the system, especially in environments where multiple systems need to synchronize user access rights or when additional manual checks are required before granting full access.
  
- **Avoid when:** Immediate access for new users is critical and there are no dependent processes that need to complete before the user gains access.