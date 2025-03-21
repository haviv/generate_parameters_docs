# Force Workflow Role Update Display

**Technical Name:** ForceWorkflowRoleUpdateDisplay

**Category:** Workflow

**Default Value:** None specified

**Impact Level:** Medium

**Description:** This parameter controls the display visibility of workflow role updates in the ProfileTailor application, contingent upon the AutoSave feature being enabled for role updates.

**Business Impact:** When enabled, this setting can streamline the workflow role update process, mitigating the risk of manual error and ensuring that role changes are automatically saved. This improves the efficiency of managing user roles and permissions, enhancing overall security and compliance posture.

**Technical Impact when configured:** If the AutoSave of roles list on role update feature is enabled through `CommonSettings`, the display of certain UI elements related to workflow role updates will be hidden, thus enforcing an automatized process.

**Examples Scenario:** In a scenario where an organization requires frequent updates to user roles within the Pathlock platform, enabling this parameter alongside AutoSave can reduce the time and effort needed for manual saves after each update, preventing potential oversights or errors in role management.

**Related Settings:** `EnableAutosaveOfRolesListOnRoleUpdate`

**Best Practices:** 
- **Configure when:** there is a high volume of role updates, and there is confidence in the automatic processes to manage roles correctly.
- **Avoid when:** manual review of each role update is necessary before saving due to complex compliance or security requirements that the autosave feature may not fully address.