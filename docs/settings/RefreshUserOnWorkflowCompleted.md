# Refresh User On Workflow Completed

**Technical Name:** RefreshUserOnWorkflowCompleted

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether a user's information is refreshed in the system upon the completion of a workflow process. This includes updating the user's status, roles, permissions, or any other related attributes based on the outcome of the workflow.

**Business Impact:**

Ensuring user information is accurate and up-to-date post-workflow completion is crucial for maintaining operational integrity and compliance. This parameter can significantly impact access control and audit trails, making it essential for security policies and compliance practices.

**Technical Impact: when configured**

When configured, this parameter initiates a process to refresh and update the user details in the Pathlock GRC system database immediately after a workflow is marked as completed. This ensures that any changes made during the workflow process are accurately reflected in the user’s profile and access rights.

**Examples Scenario:**

- A user has been granted additional roles as part of a role assignment workflow. Once the workflow is completed, the `RefreshUserOnWorkflowCompleted` parameter ensures the user's profile is immediately updated to reflect these changes.
- After a user's request for increased access rights is approved in a workflow, this parameter ensures their access rights are updated in real-time, allowing for seamless access to the new resources.

**Related Settings:**

- **SendApprovalInformationToRequester** - works in conjunction to notify the requester about the approval status, which may trigger user information refresh when combined with `RefreshUserOnWorkflowCompleted`.

**Best Practices:** 

- **Configure when:** there are dynamic user roles and permissions that change frequently through workflow processes. It ensures user access rights are immediately updated upon workflow completion.
- **Avoid when:** workflows frequently update user roles or permissions, and immediate reflection of these changes in the system could lead to performance issues. In such cases, scheduling the refresh process during off-peak hours might be more appropriate.