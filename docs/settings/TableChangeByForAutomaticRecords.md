# Table Change By For Automatic Records

**Technical Name:** TableChangeByForAutomaticRecords

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter governs the behavior of how automatic records are acknowledged and processed within the Pathlock Cloud GRC platform. It appears to be specifically related to the mechanism of tracking changes, additions, or removals of user group assignments or permissions, possibly in a workflow context or while updating user profiles based on dynamic rules.

**Business Impact:**

The correct configuration of this parameter ensures that automated processes, like user group assignments and permissions updates, are accurately tracked and recorded. This impacts both the operational integrity and audit capabilities of an organization by ensuring that all automatic adjustments made by the system are documented and can be reverted or audited if necessary.

**Technical Impact when configured:**

- Ensures automated records such as new employee group assignments or permission changes are accurately captured.
- Helps in maintaining the integrity of workflow approvals and group import definitions.
- Facilitates better tracking of user access and permissions adjustments over time, aiding in compliance and audit trails.

**Examples Scenario:**

A scenario where this parameter is crucial could be in the automated assignment of employees to specific permission groups based on their role changes within the organization. For example, if an employee moves from the sales department to the HR department, the system automatically updates their group memberships to reflect this change, ensuring they gain the necessary access for their new role while revoking irrelevant permissions.

**Related Settings:**

There is no direct mention of related settings in the provided references; hence, they cannot be listed with certainty.

**Best Practices:** 

- **Configure when:** Setting up or making significant changes to workflows involving automatic user group assignments or permissions updates. It's crucial when you want to enhance the traceability of system-automated changes for compliance and auditing purposes.
- **Avoid when:** If your organization does not utilize automated mechanisms for user group management or if such processes are managed manually, the significance of this parameter might be reduced.