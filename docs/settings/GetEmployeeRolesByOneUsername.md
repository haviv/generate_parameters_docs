# Get Employee Roles By One Username

**Technical Name:** GetEmployeeRolesByOneUsername

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether the system retrieves employee roles based on a single username, focusing on integrating various user identities (e.g., Active Directory, SAP) for role assignment. It enables a unified approach to managing user roles across different platforms within the organization.

**Business Impact:**

Enabling this parameter enhances security and compliance by ensuring accurate role assignment and access control. It streamlines user management processes, reduces the risk of unauthorized access, and aligns with compliance requirements regarding user access rights.

**Technical Impact when configured:**

When enabled, the system will perform checks against Active Directory and other user databases to match usernames with their corresponding roles. This process ensures that access rights and roles are accurately assigned according to the user's identity across different systems.

**Examples Scenario:**

- **Scenario 1:** An organization wishes to enforce access control by assigning roles based on the user's identity in Active Directory and SAP systems. By enabling this parameter, the system will automatically fetch and assign roles to users, ensuring consistency in access control across platforms.
  
- **Scenario 2:** To streamline user management and ensure compliance with internal access policies, a compliance officer enables this setting. This allows for automatic role assignments based on unified username identification, simplifying audits and compliance checks.

**Related Settings:**

- `NotifySubmitterInEmergencyAccessStep`: While not directly related, it complements this parameter by notifying submitters in emergency access situations, enhancing the organization's security and compliance posture.

**Best Practices:** 

- **Configure when:** You aim to simplify user management across disparate systems and ensure accurate role assignments based on a unified user identity.
  
- **Avoid when:** Your organization does not require unified role management across different platforms, or if there are concerns about the performance impact of additional checks against multiple user repositories.