**Roles Spllitter Roles Child Role Identify Common Part**

**Technical Name:** RolesSplliterRolesChildRoleIdentifyCommonPart

**Category:** Configuration

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

This parameter controls how derived roles are named in Pathlock Cloud GRC's Role Splitter functionality, particularly focusing on identifying common parts in child role names. It facilitates the differentiation of roles based on organizational levels or specific criteria, ensuring roles are accurately named and managed within the system.

**Business Impact:**

Proper configuration of this parameter is critical for maintaining clear and understandable role names, which directly impacts the efficiency of role management and audit processes. It aids in preventing role name duplication and confusion, thereby enhancing security posture by ensuring correct role assignments and easier detection of unauthorized access.

**Technical Impact when configured:**

Configuring this parameter allows for dynamic role name generation based on predefined templates or organizational values. It ensures roles derived from a master role have names that reflect their specific functions, permissions, or organizational level, aiding in systematic role governance and simplification of role review processes.

**Example Scenario:**

In a scenario where an organization creates derived roles from a master role for different departments or regions, this parameter can be used to automatically include departmental or regional identifiers in the derived role names, making it easy to identify the purpose and scope of each role at a glance.

**Related Settings:**

- RoleSplitterIncludeSoDRisksWithGroups
- RolesSplitterCopyOnlyDefaultAuthorizationObjects

**Best Practices:** 

- **Configure when:** you have a complex role structure with many derived roles and need a systematic way to manage role names.
- **Avoid when:** your organization has a simple role structure or when role names do not require differentiation based on organizational levels or specific criteria.