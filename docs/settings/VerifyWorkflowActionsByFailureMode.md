# Verify Workflow Actions By Failure Mode

**Technical Name:** VerifyWorkflowActionsByFailureMode

**Category:** Workflow

**Default Value:** True

**Impact Level:** High

**Description:**

This parameter controls whether workflow actions are verified based on their failure modes. It ensures that workflows are only approved when all actions meet the predefined criteria for success, thereby increasing the integrity and reliability of workflow processes. 

**Business Impact:**

Enabling this parameter reinforces the security and compliance posture of the organization by ensuring that only workflows with actions that have been thoroughly verified as successful are advanced. This minimizes the risk of errors, fraud, or non-compliance affecting business operations.

**Technical Impact when configured:**

When configured, this setting applies strict checks on workflow actions, filtering out any that have failed or not met specified requirements. This may lead to an increase in workflow rejections or delays if actions frequently fail to meet the verification criteria.

**Examples Scenario:**

- In a scenario where a workflow is set up for financial approvals, enabling this parameter ensures that every step of the approval process is verified for success. If any action within this workflow does not meet the expected criteria (e.g., insufficient documentation, failed cross-checks), the entire workflow is flagged for review or rejection.
  
**Related Settings:**

- SwitchBackToOriginalUserAfterEmergencyAccess

**Best Practices:** configure when,
- High-level integrity and compliance checks are critical to the business process.
- The organization requires strict verification of workflow actions to mitigate risks.

avoid when,
- Workflow processes need to prioritize speed and efficiency over strict verification processes.
- The organization has a high tolerance for risk and prefers to manually review workflows rather than relying on automated verifications.