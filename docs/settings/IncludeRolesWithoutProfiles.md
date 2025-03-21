# Include Roles Without Profiles

**Technical Name:** IncludeRolesWithoutProfiles

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter configures whether roles without associated profiles should be included in certain operations within the Pathlock Cloud GRC platform. Typically, roles in systems like SAP are expected to have associated profiles that define the permissions and access levels for users assigned those roles. By including roles without profiles, organizations can ensure comprehensive coverage in security, risk, and compliance assessments.

**Business Impact:**

Enabling this setting ensures that no role, even those without explicitly defined profiles, is overlooked in the security and compliance auditing processes. This could be particularly useful in ensuring all configurations and potential security risks are accounted for, thereby reducing the risk of unauthorized access or non-compliance with internal or external regulations.

**Technical Impact when configured:**

When configured to include roles without profiles, the system broadens its scope during security and compliance audits, configurations checks, and risk assessments. This means that even roles that might not have direct profile associations but are potentially used in the system will be evaluated, ensuring a more thorough and comprehensive audit and assessment process.

**Examples Scenario:**

A company conducts a monthly audit of their SAP system to ensure all roles conform to their strict compliance standards. By enabling IncludeRolesWithoutProfiles, they can include roles that do not have direct profile links but might still be assigned to users, ensuring these roles are also audited for compliance with their internal security policies.

**Related Settings:**

- RunUserProcessInSeperateQueue

**Best Practices:** Configure this setting to `True` when conducting comprehensive audits and assessments to ensure all roles are considered, including those without profiles. Avoid enabling this setting when performing targeted audits focused solely on roles with defined profiles to decrease processing time and complexity.