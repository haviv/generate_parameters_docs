# Remove Invalid Approvers From Approval Groups

**Technical Name:** RemoveInvalidApproversFromApprovalGroups

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether invalid approvers are automatically removed from approval groups within the Pathlock Cloud GRC platform. An approver becomes invalid due to changes in role, permissions, or employment status. Enabling this setting ensures that only valid and authorized users can approve actions, enhancing the platform's security and compliance posture.

**Business Impact:**

Having invalid approvers in approval groups can lead to unauthorized approvals or delays in the approval process, affecting compliance and operational efficiency. Enabling this parameter reduces the risk of non-compliance with internal and regulatory standards, enhances security, and streamlines the approval process by ensuring that all approvers are current and authorized.

**Technical Impact when configured:**

When this parameter is configured to true, the system automatically identifies and removes users who are no longer eligible to approve actions within specific groups. This automation reduces the administrative burden of manually reviewing and updating approval groups, ensuring they are always up-to-date and compliant with internal policies and external regulations.

**Examples Scenario:**

- **Before enabling**: An employee who was previously an approver in an expense approval group leaves the company. Their account remains in the approval group, causing delays as approvals await action from an account that is no longer active.
  
- **After enabling**: The same scenario as above occurs, but now, the system automatically removes the former employee's account from the approval group, allowing the approval process to continue smoothly with active, valid approvers.

**Related Settings:**

N/A

**Best Practices:** 

- **Configure when**: Your organization requires high levels of compliance and security, especially in sensitive workflows where the integrity of the approver is crucial.
- **Avoid when**: All approvers are managed manually with a high degree of accuracy, or in small environments where the administrative overhead is minimal.