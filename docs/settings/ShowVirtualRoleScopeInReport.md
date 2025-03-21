# Show Virtual Role Scope In Report

**Technical Name:** ShowVirtualRoleScopeInReport

**Category:** Reporting

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `ShowVirtualRoleScopeInReport` parameter controls whether the scope of virtual roles is displayed in specific Pathlock Cloud GRC platform reports. This parameter ensures that reports accurately reflect the real and virtual roles within the system, providing a comprehensive overview of role usage and composition.

**Business Impact:**

Enabling this parameter helps in understanding the distribution and utilization of virtual roles across the organization. It offers insights into role optimization for enhanced security and compliance, thereby facilitating better decision-making in access governance.

**Technical Impact when configured:**

Once configured, the `ShowVirtualRoleScopeInReport` parameter affects the generation of certain reports by including detailed information about virtual roles. This could lead to an increased clarity in role analytics, aiding in the identification of redundant roles and streamlining the role management process.

**Example Scenario:**

- **Situation:** An organization needs to audit user access and role assignments for compliance with internal policies and external regulations.
- **Without the parameter:** Reports generated might only show direct role assignments, missing the context on how virtual roles aggregate these permissions.
- **With the parameter enabled:** The audit reports include both direct and virtual role assignments, offering a complete picture of user access rights, simplifying compliance audits, and identifying unnecessary role assignments.

**Related Settings:** 

- `RoleAttribute1` through `RoleAttribute7`: Attributes defining the properties of real and virtual roles.
- `GenerateFields`: Part of reporting functionalities, where role scope can influence the content of reports.

**Best Practices:** 

- **Configure when:** A comprehensive understanding of both real and virtual role distribution within the organization is required, especially for audit and compliance purposes.
- **Avoid when:** If the inclusion of virtual role information complicates report analysis or when such detail is not necessary for specific report audiences.