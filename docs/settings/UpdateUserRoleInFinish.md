# Update User Role In Finish

**Technical Name:** UpdateUserRoleInFinish

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

The `UpdateUserRoleInFinish` parameter is designed to be used in the final step of a workflow action, specifically when updating a user's role. It governs whether or not the user's role should be updated at the completion of the workflow.

**Business Impact:**

By enabling this parameter, organizations can ensure that user roles are dynamically updated based on workflow outcomes, maintaining compliance and enhancing security posture by aligning access rights with current responsibilities or statuses.

**Technical Impact when configured:**

When activated, this feature triggers a role update mechanism at the finish step of a workflow, ensuring that the user’s access rights are in line with their latest role and responsibilities. This can prevent both over-privileged access and under-privileged access, enhancing operational efficiency and security.

**Examples Scenario:**

- An employee transitions from one department to another, and the workflow for department change includes a role update step at the end to ensure the employee's access rights are aligned with the new role.
- A promotion process workflow that concludes with an update to the user's role, granting them enhanced access rights appropriate for their new position.

**Related Settings:** Not explicitly provided in the provided code references.

**Best Practices:** Configure this parameter as part of role change and user status update workflows to automate the process of access rights allocation, ensuring they remain current and minimize the risk of unauthorized access or privilege escalation. Avoid using this parameter in workflows that do not result in a change to user roles or where manual review of role changes is preferred for additional oversight.