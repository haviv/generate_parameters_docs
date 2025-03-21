# Enable Delete Comments

**Technical Name:** EnableDeleteComments

**Category:** Configuration

**Default Value:** False

**Impact Level:** Medium

**Description:**

This setting controls whether users have the ability to delete comments in the system. When enabled, it adds a delete option next to each comment, allowing for its removal.

**Business Impact:**

Enabling this feature can impact how audit trails and records of decision-making processes are kept within the organization. It is vital for maintaining a transparent and accountable record-keeping process in compliance and audit scenarios.

**Technical Impact when configured:**

When configured to true, users can remove comments from records, potentially altering the comprehensiveness of historical data and audit trails. When false, all comments are retained, ensuring a full history is available for review.

**Examples Scenario:**

- An administrator needs to comply with internal policies requiring the ability to delete inappropriate or out-of-date comments from the system records to maintain data relevance and compliance.
  
- During an audit process, it might be necessary to disable the deletion of comments to preserve the integrity of the audit trail.

**Related Settings:**

- EmergencyAccessTakeOnlyWorkflowAffectedRoles

**Best Practices:** configure when comments may contain sensitive information that needs to be removable on an ad-hoc basis, avoid when full, unalterable audit trails are required for compliance.