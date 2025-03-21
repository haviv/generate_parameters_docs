# Verify Workflow Actions Not Done Text

**Technical Name:** VerifyWorkflowActionsNotDoneText

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**
This parameter is used to verify if specific actions within a workflow have been completed. It is a critical component in oversight and monitoring workflows to ensure all required actions are performed. It checks against a list of actions that are expected to be done and flags any that could not be verified as complete.

**Business Impact:**
Ensuring workflow actions are completed as required is vital for regulatory compliance, internal controls, and efficient operation. Missing actions could lead to security breaches, non-compliance with regulations, and potential financial loss. This parameter helps in identifying such lapses.

**Technical Impact when configured:**
When configured, this parameter actively assesses the completeness of specified actions within a workflow. If all actions are verified, the result is positive. However, if some actions cannot be verified, it alerts the system or responsible personnel to take necessary actions, enhancing the system's integrity and compliance posture.

**Example Scenario:**
In a scenario where a financial institution uses workflows for the approval process of credit applications, this parameter can verify whether all required checks (e.g., identity verification, credit check, and fraud check) are completed. If any of these checks cannot be verified as completed, the parameter can trigger an alert for further review, preventing potential fraud or compliance issues.

**Related Settings:**
- AuthorizationReviewTransaction

**Best Practices:** 
- **Configure when:** Setting up any workflow that requires stringent checks and verifications to ensure compliance and security, especially in financial, healthcare, and regulatory environments.
- **Avoid when:** Workflows do not have critical actions whose completion needs to be verified or in simple workflows where manual checking is viable and cost-effective.