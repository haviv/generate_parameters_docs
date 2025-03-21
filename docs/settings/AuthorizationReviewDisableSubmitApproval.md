# Authorization Review Disable Submit Approval

**Technical Name:** AuthorizationReviewDisableSubmitApproval

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:**

This parameter controls whether users can submit approval decisions during the authorization review process within Pathlock's Cloud GRC platform. It is specifically relevant in environments where authorization decisions are scrutinized and require an additional layer of approval before finalization.

**Business Impact:**

Enabling this setting can significantly impact how quickly user access rights and permissions are updated in the system. It adds an extra layer of security and oversight, ensuring that only validated and approved changes are implemented, thus minimizing the risk of unauthorized access or erroneous permissions assignment.

**Technical Impact when configured:**

When enabled, this setting prevents users from directly submitting their approval or rejection decisions. Instead, these decisions must be reviewed and approved by another authorized party, thereby introducing a dual control mechanism that enhances security and compliance by ensuring all changes are deliberate and authorized.

**Examples Scenario:**

In a scenario where an organization is undergoing an external audit for compliance with industry regulations, enabling this parameter ensures all authorization changes are double-checked and validated, offering auditors clear evidence of rigorous access controls and review processes.

**Related Settings:** 

- `ShowIsApprovedDialog`

**Best Practices:** configure when undergoing audits or in highly regulated environments, avoid when quick access changes are necessary and low risk.