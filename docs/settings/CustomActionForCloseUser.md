# Custom Action For Close User

**Technical Name:** CustomActionForCloseUser

**Category:** User Management

**Default Value:** *Not provided in the references*

**Impact Level:** High

**Description:**

This parameter defines a custom action to close or terminate user accounts in the context of Pathlock's cloud-based GRC platform. It enables the automation of user de-provisioning as part of workflow steps, particularly when initiating a start step in the workflow.

**Business Impact:**

Proper configuration of this parameter ensures compliance with security policies by timely revoking access rights of users no longer employed or authorized. It mitigates risks associated with unauthorized access, thereby protecting sensitive data and resources from potential breaches.

**Technical Impact when configured:**

When correctly configured, this parameter automates the process of identifying and closing user accounts based on criteria specified within workflow actions. This automation streamlines operations, reduces manual errors, and ensures compliance with internal and external security policies.

**Examples Scenario:**

- **Onboarding/Offboarding Workflows:** If an employee leaves the organization, the CustomActionForCloseUser parameter can automatically trigger actions to deactivate the user's account as part of the offboarding process in SAP systems or other integrated environments.

**Related Settings:** 

- **Config_SodResolverSettings:** This setting might influence how the CustomActionForCloseUser is executed, especially if there's a need to resolve conflicts of Separation of Duties (SOD) before closing a user account.

**Best Practices:** 

- **Configure When:** It is critical to configure and test this parameter as part of the deployment of onboarding and offboarding workflows to automate compliance with user access policies.
  
- **Avoid When:** Do not use this parameter without proper testing or in scenarios where manual review is required before user de-provisioning to prevent accidental loss of access for active users.