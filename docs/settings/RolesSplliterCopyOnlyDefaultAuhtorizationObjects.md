# Roles Splitter Copy Only Default Authorization Objects

**Technical Name:** RolesSplliterCopyOnlyDefaultAuhtorizationObjects

**Category:** Security

**Default Value:** False

**Impact Level:** Medium

**Description:**

This configuration parameter controls whether only default authorization objects are copied during the role split operations within the Pathlock Cloud GRC platform. It is designed to ensure that during the process of splitting a role, only those authorization objects considered as default by the system are replicated to the new roles created as part of the split. 

**Business Impact:**

Enabling this feature ensures that unnecessary or sensitive permissions are not automatically inherited by new roles during the splitting process, reducing the risk of unintended access rights escalation and supporting a principle of least privilege policy within the organization's access control practices.

**Technical Impact when configured:**

- When set to true, any role cloning or splitting action will only replicate the default set of authorization objects, excluding any additional permissions that may have been added to the original role.
- When set to false, all authorization objects, including customized permissions beyond the defaults, are copied to the newly created role(s).

**Example Scenario:**

An organization decides to split an existing role into several more granular roles to adhere to a new access control policy aimed at reducing broad access scopes within its ERP system. By having the RolesSplliterCopyOnlyDefaultAuhtorizationObjects parameter set to true, the organization ensures that only essential permissions are cloned into the new roles, preventing the accidental inheritance of elevated privileges that were specific to the original role only. 

**Related Settings:**

- `RoleSpliterCopyAlsoInactiveAuth`
- `RoleSplitterIncludeSoD RisksWithGroups`
- `EventOnEmployeeJobCodeChangeIncludePositionTitleTexts`

**Best Practices:** 

- **Configure when:** You are looking to enforce strict access control and adhere to the principle of least privilege during role splits. Useful in tightly regulated environments or when roles with broad access are being segmented into more specific, less privileged roles.
- **Avoid when:** Roles being split require a direct one-to-one copy of all permissions, including non-default authorization objects, to maintain their operational effectiveness without manual post-split adjustments.
