# Check Deleted Users By Attribute In Workflow Scheduled Actions

**Technical Name:** CheckDeletedUsersByAttributeInWorkflowScheduledActions

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter determines whether the system checks for users deleted based on specific attributes during the execution of scheduled workflow actions. It helps in maintaining the integrity and accuracy of user-related decisions and actions within workflows.

**Business Impact:**

Ensuring that actions are not mistakenly applied to deleted users can prevent unnecessary or erroneous workflow executions, thereby enhancing the operational efficiency and security posture of the organization.

**Technical Impact when configured:**

When enabled, this setting ensures that workflows are only executed on active users, hence, reducing the risk of data breaches and compliance violations by preventing unauthorized access or actions.

**Examples Scenario:**

An organization implements a scheduled workflow for updating user access rights on a weekly basis. By enabling this parameter, the workflow checks and excludes any user marked as deleted based on relevant attributes before executing the access rights update. This prevents the application of access rights to users who are no longer part of the organization.

**Related Settings:**

- `CombinationMaxSystemsForDisplay`: This setting might influence the system's performance during the check for deleted users if a large number of systems are displayed.

**Best Practices:** 

- **Configure when:** You have workflows that perform actions affecting user accounts or access rights, especially in larger organizations where user statuses frequently change.
  
- **Avoid when:** Workflows are designed to not interact with user accounts directly or when the business process requires including actions on previously deleted users for record-keeping or auditing purposes.