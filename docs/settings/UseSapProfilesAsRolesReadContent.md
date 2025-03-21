# Use Sap Profiles As Roles Read Content

**Technical Name:** UseSapProfilesAsRolesReadContent

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter configures the system to utilize SAP profiles as roles for the purpose of reading content within the Pathlock Cloud GRC platform. It impacts how user access and permissions are mapped and managed within SAP environments.

**Business Impact:**

Enabling this setting streamlines the integration with SAP systems by aligning SAP profile definitions with role management in Pathlock, facilitating more coherent access control and simplifying user management and audits. It directly affects compliance reporting and security posture by ensuring accurate role representation.

**Technical Impact when configured:**

When configured, SAP profiles are recognized as roles by the Pathlock platform. This effectively bridges the SAP authorization model with Pathlock's access controls, enabling detailed and accurate control over user permissions and activities based on their SAP profile assignments.

**Examples Scenario:**

- A company uses SAP for its internal processes and wants to leverage the same profile structures within Pathlock for managing access to sensitive data. By setting UseSapProfilesAsRolesReadContent to true, they can directly map SAP profiles to roles within Pathlock, ensuring that users have the appropriate level of access based on their existing SAP profiles.

**Related Settings:** 

- ActivityModesByLevel: Determines the granularity of access control within activities, which complements the role-based access control when SAP profiles are used as roles.

**Best Practices:** 

- Configure when: You have a clear mapping between SAP profiles and the access requirements within Pathlock, and you wish to streamline user management by leveraging existing SAP profiles.
  
- Avoid when: There is no direct correlation between SAP profiles and Pathlock access control requirements, or when SAP profiles do not accurately reflect the desired access levels within Pathlock.