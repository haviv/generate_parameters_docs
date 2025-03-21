# Default Role For Direct Manager

**Technical Name:** DefaultRoleForDirectManager

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:**

This parameter is used to assign a default role to direct managers within the Pathlock Cloud GRC platform. It ensures that upon creation or assignment, managers have the necessary permissions to perform their duties, specifically in workflow approvals and group management contexts.

**Business Impact:**

Assigning the correct role to direct managers is crucial for maintaining efficient workflow processes and ensuring that the necessary control and oversight are in place for compliance and risk management. It helps in streamlining the operations related to access requests, employee management, and approval processes, directly impacting operational efficiency and security posture.

**Technical Impact when configured:**

When the DefaultRoleForDirectManager parameter is configured, it automatically assigns the specified role to new managers or those added to approval workflows. This eliminates the need for manual role assignment, reduces the risk of human error, and ensures that managers have the access rights needed to approve, manage, and oversee workflow processes.

**Examples Scenario:**

An organization wants to ensure that all direct managers have the ability to approve leave requests and access requests for their subordinates. By setting the DefaultRoleForDirectManager, the company can automatically grant these permissions to all managers, simplifying the onboarding process and ensuring that no managerial role is left without the necessary rights to perform these approvals.

**Related Settings:** 

- WorkflowAllowReturnRequestToRequester

**Best Practices:** 

- **Configure when:** Setting up the Pathlock Cloud GRC platform for the first time or when updating roles and permissions to ensure managers have the necessary rights.
  
- **Avoid when:** Every user's role and permissions should be controlled individually, and there's no need for a default managerial role or in smaller teams where role distinctions are not as necessary.