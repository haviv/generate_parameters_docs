# Enable Import Approvers

**Technical Name:** ImportManagersToWF

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

Enables the functionality to automatically import and assign managers as approvers within specific workflows. This is particularly used in organizational unit-based group generation processes.

**Business Impact:**

Automating the approver assignment process reduces manual errors and ensures that the appropriate managers are always set as approvers in compliance and governance workflows. This can significantly streamline organizational processes, especially in large or dynamically changing structures.

**Technical Impact when configured:**

When enabled, this parameter automatically fetches manager information (e.g., from Active Directory) and assigns them as approvers in designated approval groups. This automation also includes ensuring that these managers have the necessary user group authorizations.

**Examples Scenario:**

- An organization wants to ensure that expense approvals are always reviewed by the correct department manager without manually updating workflow configurations whenever there are changes in the management structure.

**Related Settings:**

- AuthorizationsForUserGroup

**Best Practices:** 

- Configure when the organization has dynamic changes in leadership or management roles to ensure workflows are always up-to-date without manual intervention.
- Avoid when organizational structures are very static, or when specific workflows require non-manager approvers for effective governance.