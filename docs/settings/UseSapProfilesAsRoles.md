# Use Sap Profiles As Roles

**Technical Name:** UseSapProfilesAsRoles

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter indicates whether SAP profiles should be considered as roles within the Pathlock Cloud GRC platform. When enabled, SAP profiles are used to determine user access and permissions, aligning SAP user management practices with Pathlock's GRC strategies.

**Business Impact:**

Enabling this parameter can streamline user access management by leveraging existing SAP profiles, thus reducing administrative overhead and enhancing compliance with internal and external regulations by ensuring a unified access management strategy across SAP and Pathlock platforms.

**Technical Impact when configured:**

When this parameter is enabled, user roles within Pathlock Cloud GRC will be mapped to SAP profiles, affecting how access rights and permissions are determined and managed. This alignment may impact user access reviews, compliance audits, and role-based access controls, among other areas.

**Examples Scenario:**

A company wishes to synchronize its SAP user management practices with the Pathlock Cloud GRC platform to maintain a single source of truth for user roles and permissions. By enabling the UseSapProfilesAsRoles parameter, the company can ensure that any changes in SAP profiles directly reflect in the user’s access rights within Pathlock, simplifying user access management and compliance auditing.

**Related Settings:**

- SapComapny
- City
- Department
- Building
- InvalidDate
- ValidFrom
- EmployeeId
- LastLogon
- UserType
- CreateDate
- PositionChangedDate

**Best Practices:** configure when SAP is the primary source for user role management to ensure consistent access rights across platforms. Avoid when SAP profiles do not align with the desired access control structure within Pathlock Cloud GRC.