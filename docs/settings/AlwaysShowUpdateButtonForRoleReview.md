# Always Show Update Button For Role Review

**Technical Name:** AlwaysShowUpdateButtonForRoleReview

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This configuration parameter controls the visibility of the "Update" button within the Role Review workflow. When enabled, it ensures that the button is always visible to users regardless of the current stage of the review process, allowing for continuous updates to role assignments.

**Business Impact:**

Ensuring that the update button is always visible during role reviews can significantly streamline the process of making role adjustments in real-time. This can lead to more efficient role governance and compliance by allowing immediate action, thus reducing the risk associated with delayed role assignment adjustments.

**Technical Impact when configured:**

When this parameter is set to true, it overrides the default behavior of hiding the update button under certain conditions in the role review workflow. This ensures that users can update role assignments at any point, enhancing flexibility and responsiveness in managing user access and permissions.

**Examples Scenario:**

In a scenario where an organization is undergoing a compliance audit, having the ability to quickly update role assignments can be crucial. For example, if an auditor identifies a user with excessive privileges, the Always Show Update Button For Role Review setting allows an administrator to immediately revise the user's role assignments, helping to maintain compliance with least privilege principles.

**Related Settings:** DisableUpdateUsernameInUsersAdministration

**Best Practices:** configure when ongoing role reviews require high levels of flexibility and immediate action is necessary. Avoid when the process benefits from having structured stages of review without the option for constant updates, to ensure each review stage is completed before changes are made.