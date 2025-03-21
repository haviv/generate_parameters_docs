# Populate Workflow Approval Groups With Approvers

**Technical Name:** ImportApproversFromOrganizationStrcture

**Category:** Workflow

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter is designed to automate the inclusion of approvers into workflow approval groups by importing them from the organizational structure. This process is key to maintaining an up-to-date approval process that reflects the current organizational hierarchy and personnel assignments.

**Business Impact:**

Enabling this parameter ensures that workflow approval groups are always populated with the correct approvers based on the organization's current structure, thereby enhancing the efficiency and accuracy of approval processes. This is crucial for organizations to maintain compliance with internal policies and regulatory requirements by ensuring that only designated and appropriate personnel can approve specific actions and processes.

**Technical Impact when configured:**

Upon configuration, this parameter automatically updates approval groups within workflows by fetching approver information from the organizational structure. This minimizes manual entry errors and oversight, ensuring that approval processes are streamlined and accurate.

**Examples Scenario:**

An organization undergoes frequent changes, including promotions, transfers, and departures. By configuring this parameter, the system dynamically updates workflow approval groups to reflect these changes, ensuring that approvals are always routed to the current, appropriate staff members, thereby preventing delays or compliance issues.

**Related Settings:**

- HRMitigatedUsers
- HRMovementForWorkStart
- HideDerivedRolesInSearchWindow

**Best Practices:** configure when the organization's structure is stable and there are clear hierarchies for approval processes. Avoid when organizational structures are under major overhaul or when approver roles are not clearly defined within the structure.