# Enable System Selection Narrow By Assigned Roles

**Technical Name:** EnableSystemSelectionNarrowByAssignedRoles

**Category:** User Management

**Default Value:** 0

**Impact Level:** Medium

**Description:**

This setting allows for the filtering of systems based on the roles assigned to a user. When enabled, users will only see systems in reports and selections where they have assigned roles, thereby narrowing down the visible selections to relevant ones.

**Business Impact:**

Improving the usability of the system for end users by simplifying their choices to those systems where they have role assignments. This can reduce confusion and enhance security by ensuring that users are focusing solely on systems relevant to their permissions and duties.

**Technical Impact when configured:**

When configured, this parameter dynamically filters the systems that users can select or view within reports, based on the roles assigned to them within each system (e.g., SAP). It ensures users interact only with data pertinent to their assigned roles, potentially decreasing the risk of unauthorized access or actions in unassigned systems.

**Example Scenario:**

A user with roles assigned in the SAP Finance system but not in the HR system will only see the SAP Finance system in their reports or system selection options, thereby avoiding any unnecessary information overload or potential security risks from accessing unauthorized systems.

**Related Settings:**

- UserGroupAutomaticRolesDeletionPrecentageToleranceMinGroupSize

**Best Practices:** 

- Configure when: It is beneficial to streamline users' focus on systems relevant to their job functions, thereby enhancing navigation efficiency and reinforcing system security.
- Avoid when: Users require visibility across multiple systems regardless of their role assignments, or when the organizational policy dictates equal visibility for auditing or cross-functional work requirements.