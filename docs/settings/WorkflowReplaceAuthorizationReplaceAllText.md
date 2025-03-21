# Workflow Replace Authorization Replace All Text

**Technical Name:** WorkflowReplaceAuthorizationReplaceAllText

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:** This parameter controls whether the authorization replacements within the workflow should include all relevant text replacements, ensuring that role mappings and user authorizations are accurately reflected in workflow actions.

**Business Impact:** Proper use of this parameter can significantly streamline the authorization management process, reducing the risk of unauthorized access and enhancing compliance with security policies. Misuse or misconfiguration, on the other hand, might lead to security breaches or compliance issues.

**Technical Impact when configured:** If enabled, this setting ensures that during workflow actions, all instances of role names that do not match current role mappings are identified and processed for potential updates or replacements. This is crucial for maintaining the integrity of role-based access controls within the system.

**Examples Scenario:**
1. During the `StartStep` of a workflow, a user's role is evaluated, and it's determined that their current role does not align with the new role mappings defined in the workflow. If the `WorkflowReplaceAuthorizationReplaceAllText` parameter is active, the system will flag this user's role for update or replacement, ensuring that their access rights are correctly aligned with the new organizational policies.
2. In the `ApplyAuthorizationAction`, this parameter ensures that authorization replacements cover all text entities related to roles and permissions, not leaving behind any outdated references that could lead to incorrect access levels being maintained.

**Related Settings:** N/A

**Applicable Workflows Actions:** 
- StartStep
- ApplyAuthorizationAction

**Best Practices:** 
- Configure when: Implementing or updating workflow processes that involve changes to user roles and authorizations to ensure that all associated texts and permissions are correctly updated.
- Avoid when: The workflow processes in question do not involve changes to authorizations or when the cost of updating all text and permissions outweighs the benefits, such as in very small or static environments.