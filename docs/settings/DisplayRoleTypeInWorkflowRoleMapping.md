# Display Role Type In Workflow Role Mapping

**Technical Name:** DisplayRoleTypeInWorkflowRoleMapping

**Category:** Workflow UI

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of role types within the workflow role mapping interface. Enabling it will allow for a more granified control and visibility over different types of roles during the workflow process, enhancing the user's ability to tailor the workflow according to their specific needs.

**Business Impact:**

Enabling this feature ensures that during the workflow configuration, specific role types are visible and distinguishable. This visibility is critical in maintaining proper access control and compliance, as it allows for a more precise setup of permissions and approvals necessary in sensitive environments.

**Technical Impact when configured:**

Once enabled, administrative users will have the capability to see and differentiate between role types directly within the workflow UI. This setup facilitates the correct mapping of roles to actions or decisions points in the workflow, thereby reducing errors and ensuring a more effective access control mechanism.

**Example Scenario:**

A company wants to ensure that during the approval process of access rights, department heads can only approve roles specific to their department. By enabling DisplayRoleTypeInWorkflowRoleMapping, the workflow UI can be adjusted to display only the relevant roles for each department head, thus streamlining the process and minimizing the risk of inappropriate access being granted.

**Related Settings:**

- DisplayDeniedWorkflowStep

**Best Practices:** Enable this feature whenever your organization requires detailed visibility and control over role mapping in workflows. Avoid enabling this feature if there is no need for differentiation between role types in your workflow processes, as it might unnecessarily complicate the UI.