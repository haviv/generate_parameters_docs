# Disable Delete Comment From Workflow

**Technical Name:** DisableDeleteCommentFromWorkflow

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether users can delete comments from workflows. When enabled, it restricts the ability to remove comments, ensuring all user inputs and changes within the workflow are retained for auditability and traceability.

**Business Impact:**

Enabling this parameter helps maintain a comprehensive audit trail of all comments made during the workflow process. It ensures accountability and transparency, as every piece of feedback, decision rationale, and discussion is preserved. This can be critical for compliance with various regulatory standards that demand thorough documentation of internal processes.

**Technical Impact when configured:**

Once configured, this setting prevents the deletion of comments from all workflows within the Pathlock Cloud GRC platform. It modifies the user interface to either hide or disable the delete comment functionality, ensuring that all comments, once made, become a permanent part of the workflow's history.

**Examples Scenario:**

- **Audit Preparation:** In preparation for an audit, an organization enables this parameter to ensure that all comments and decision-making processes are fully documented and accessible for reviewers, demonstrating compliance with internal controls.

**Related Settings:**

N/A

**Best Practices:** configure when you require stringent audit trails and regulatory compliance, avoid when workflows require flexibility in comment management due to evolving discussions or corrections.

