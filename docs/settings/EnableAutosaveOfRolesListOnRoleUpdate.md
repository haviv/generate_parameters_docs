# Enable Autosave Of Roles List On Role Update

**Technical Name:** EnableAutosaveOfRolesListOnRoleUpdate

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the automatic saving of the roles list whenever a role is updated. This feature ensures that all modifications to roles are immediately preserved, enhancing data integrity and consistency across the system.

**Business Impact:**

Automatically saving the roles list upon modification reduces the risk of data loss and ensures that role updates are immediately reflected across the system. This improves the efficiency of managing role-based access controls, facilitating swift updates to user permissions and enhancing the organization's ability to adapt to changing access requirements.

**Technical Impact when configured:**

When enabled, any update made to a role within the platform will trigger an automatic save action for the entire roles list. This behavior ensures that all changes are captured and stored without requiring manual intervention, streamlining the administration process and reducing the potential for human error.

**Examples Scenario:**

1. An administrator modifies a role to include additional permissions needed for a specific compliance requirement. With this configuration enabled, the system automatically saves these changes, immediately applying the updated permissions to all users assigned to that role.
2. A role is updated to exclude certain access rights that are no longer necessary. The autosave feature ensures that this critical security change is promptly reflected in the system, mitigating potential security risks.

**Related Settings:**

**Applicable Workflows Actions:** 

**Best Practices:** Configure this setting in environments where roles are frequently updated to ensure that all changes are automatically preserved. Avoid enabling in scenarios where role updates undergo a review process before being formally saved to reduce potential conflicts or unintended permission assignments.