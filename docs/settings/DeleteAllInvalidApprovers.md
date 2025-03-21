# Delete All Invalid Approvers

**Technical Name:** DeleteAllInvalidApprovers

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether or not invalid approvers are automatically removed from workflow approval groups. When set to true, any approvers that do not meet the current validation rules will be excluded from the approval process.

**Business Impact:**

Ensuring that only valid approvers are part of the approval process streamlines workflow operations and enhances security and compliance by preventing unauthorized access or actions.

**Technical Impact when configured:**

When enabled, this setting iterates through all approvers designated by dynamic calculated user group rules, verifying their validity. If an approver is invalidated by current standards or rules, they are automatically removed from the workflow approval group, ensuring that all participants in the approval process are valid and authorized at the time of each workflow execution.

**Example Scenario:**

For instance, if an employee's role changes and they no longer hold the permissions necessary to approve certain actions, this setting, when enabled, will automatically remove them from the approval groups they are no longer authorized to participate in. This preemptively prevents potential security risks or compliance issues.

**Related Settings:**

- RemoveInvalidApproversFromApprovalGroups

**Best Practices:** 

- **Configure when:** it is critical to ensure that all approvers in the workflow have current, valid permissions and roles. Particularly useful in dynamic organizations where roles and responsibilities frequently change.
  
- **Avoid when:** there may be exceptional cases where an approver temporarily fails validation checks due to system updates or role transitions. In such cases, a more nuanced, manual review of approver validity may be preferred.