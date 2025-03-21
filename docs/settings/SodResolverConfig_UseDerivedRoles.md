# Include derived roles

**Technical Name:** SodResolverConfig_UseDerivedRoles

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether derived roles (roles acquired through inheritance or other indirect means) should be considered when resolving Separation of Duties (SoD) conflicts within the Pathlock Cloud GRC platform. Enabling this feature ensures a more thorough and comprehensive SoD conflict detection by including not only directly assigned roles but also those obtained through role hierarchies or other indirect relationships.

**Business Impact:**

Taking into account derived roles enhances the organization's ability to manage and mitigate risks associated with improper access rights distribution and potential SoD violations. By enabling a deeper inspection of user access, it supports tighter security and compliance standards, helping prevent fraudulent activities and ensuring that internal or external regulations are adhered to effectively.

**Technical Impact when configured:**

Configuring the `SodResolverConfig_UseDerivedRoles` parameter to include derived roles in SoD conflict checking extends the scope of analysis to a wider array of role assignments. This can lead to the identification of SoD conflicts that would otherwise remain undetected if only direct role assignments were considered, thereby enhancing the platform's ability to safeguard against risks related to access rights and permissions.

**Examples Scenario:**

For instance, in a scenario where an employee is indirectly assigned a role through departmental membership that, combined with a directly assigned role, results in an SoD violation, having this parameter enabled ensures such a conflict is identified. This is crucial in complex organizational structures where indirect role assignments are common, ensuring comprehensive risk and compliance management.

**Related Settings:**

- `SodResolverConfig_ExcludeRolesWithSoD`
- `SodResolverConfig_ExtraHighRiskFactor`

**Best Practices:** configure when comprehensive SoD conflict detection is required, especially in complex organizational structures with nested or indirect role assignments; avoid when minimal compliance checking suffices or in simpler organizational setups to reduce processing overhead.