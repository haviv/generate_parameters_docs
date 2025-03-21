# Hide Role Advisor In Workflow Screens

**Technical Name:** HideRoleAdvisorInWorkflowScreens

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `HideRoleAdvisorInWorkflowScreens` parameter controls the visibility of the Role Advisor feature within workflow screens. Enabling this parameter will hide the Role Advisor from users during the workflow process, affecting how users select and manage roles throughout the approval or modification steps in the workflow.

**Business Impact:**

Hiding the Role Advisor can streamline the workflow process for users by reducing the amount of information and options available, leading to potentially quicker decision-making. However, it may also limit the ability to make informed decisions regarding role assignments, as the Role Advisor provides valuable insights and recommendations based on the organization's security, compliance, and risk management practices.

**Technical Impact when configured:**

- **Visibility:** The Role Advisor will not be visible to users in workflow screens, affecting how roles are assigned, updated, or removed during workflow processes.
- **User Experience:** Simplifies the user interface by removing additional options that may not be necessary for all users or workflows.
- **Decision Making:** May impact users' ability to make informed decisions regarding role assignments due to the absence of recommendations from the Role Advisor.

**Examples Scenario:**

An organization implements the `HideRoleAdvisorInWorkflowScreens` parameter to streamline the process of role assignment during user access review workflows. As a result, users reviewing access requests are presented with a simplified interface, allowing for quicker decision-making. However, they no longer receive automated recommendations on whether a specific role should be assigned, requiring them to rely on existing knowledge or external guidance.

**Related Settings:** 

- WorkflowAffectedRole: This setting is involved in the logic for determining roles affected by workflows and might interact with how roles are displayed or managed in the context of hiding the Role Advisor.
  
**Best Practices:** 

- **Configure when:** You aim to simplify the workflow screens for users who are familiar with the role assignment process or when the Role Advisor's input is not considered necessary for certain types of workflows.
- **Avoid when:** The Role Advisor's insights and recommendations are critical for maintaining security, compliance, and proper risk management during the role assignment process within workflows.