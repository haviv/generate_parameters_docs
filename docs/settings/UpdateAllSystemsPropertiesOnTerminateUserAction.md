# Update All Systems Properties On Terminate User Action

**Technical Name:** UpdateAllSystemsPropertiesOnTerminateUserAction

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

The `UpdateAllSystemsPropertiesOnTerminateUserAction` parameter controls whether all system properties related to a user are automatically updated across applicable systems when the Terminate User workflow action is executed. When enabled, this ensures that any changes related to the termination of a user, such as deactivation or removal from groups, are propagated throughout all connected systems, maintaining consistency and compliance.

**Business Impact:**

Enabling this parameter impacts the organization by ensuring that when a user is terminated, their access rights and statuses are immediately and uniformly updated across all systems, reducing the risk of unauthorized access and simplifying the offboarding process. This is critical for maintaining security and compliance with internal policies and external regulations.

**Technical Impact when configured:**

When this parameter is configured to update all system properties on termination, it performs a comprehensive update across all connected systems and applications within the Pathlock environment. This automatic update includes changes to user roles, permissions, and access levels, ensuring that there are no lingering access rights that could pose a security risk.

**Examples Scenario:**

- An employee is terminated from the organization, and the HR department initiates the termination process in the HR system. With the `UpdateAllSystemsPropertiesOnTerminateUserAction` enabled, as soon as the Terminate User workflow is triggered, the user's access rights are automatically revoked in all connected systems, such as email, CRM, ERP, and any custom applications, ensuring a swift and secure offboarding process.

**Related Settings:** RefreshUserOnWorkflowCompleted

**Best Practices:** 

- **Configure when:** Immediate and comprehensive updates to user properties across all systems are required upon user termination, particularly in environments where security and compliance are paramount.
  
- **Avoid when:** The organization’s processes require manual review or staged updates to user properties following termination. In such cases, automating this process could bypass necessary checks and balances.