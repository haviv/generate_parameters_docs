# Disable Approval By Submitter In Role Owner Step

**Technical Name:** DisableApprovalBySubmitterInRoleOwnerStep

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter is designed to prevent the initiator of a request from being able to approve their own submission in any role owner steps within the workflow. Its purpose is to ensure segregation of duties by eliminating potential conflicts of interest, thereby enhancing the integrity of the approval process within the Pathlock GRC platform.

**Business Impact:**

Applying this setting reinforces compliance and auditability within an organization's GRC processes by ensuring that approval responsibilities are appropriately segregated. It helps prevent scenarios where users could potentially approve their own actions, reducing the risk of unauthorized activities and reinforcing internal controls.

**Technical Impact when configured:**

When enabled, this setting systematically excludes the request submitter from the pool of potential approvers during role owner workflow steps, effectively enforcing a segregation of duties policy. This might necessitate reconfiguration of workflow steps or approval groups to ensure that workflows can proceed smoothly without intervention from the submitter.

**Examples Scenario:**

In a scenario where a user requests additional access rights or permissions, enabling this parameter will safeguard the process by ensuring that the request cannot be self-approved. For example, if a finance officer requests access to sensitive payment systems, this setting will ensure that the approval must be handled by another authorized role owner, thereby maintaining adherence to internal control policies.

**Related Settings:** 

- ExtendedRequestByOriginalStepDuration

**Best Practices:** 

- Configure when segregation of duties is a critical component of your internal control environment, and where the integrity of the approval process needs to be beyond reproach.
- Avoid when workflows are designed with intentional cross-checks and balances that might allow for self-approval under very specific and controlled conditions.