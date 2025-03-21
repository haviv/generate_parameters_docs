# Disable Delete Button On Upload Files For Workflow Instance

**Technical Name:** DisableDeleteButtonOnUploadFilesForWorkflowInstance

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This setting disables the delete button for uploaded files in workflow instances. It ensures that once a file is uploaded as part of a workflow process, it cannot be deleted by users, thereby maintaining a complete record of all submissions.

**Business Impact:**

Preventing the deletion of uploaded files can significantly impact the auditability and integrity of workflow processes. For businesses, this means enhanced compliance with internal policies or regulatory requirements that mandate the preservation of all documents submitted during a workflow.

**Technical Impact when configured:**

When this parameter is set to true, the delete button becomes non-functional for any file uploaded as part of a workflow instance. This prevents the risk of accidental or intentional deletion of files, which could be crucial for audits or decision-making processes.

**Examples Scenario:**

- **Financial Approval Process:** In workflows where financial documents are uploaded for approval, disabling the delete button ensures that all submitted documents remain available for review or audit, reducing the risk of financial discrepancies or fraud.
  
- **HR Onboarding:** During the HR onboarding process, candidates might upload several documents. Keeping these files undeletable ensures that HR can always access submitted records, aiding in background checks and compliance.

**Related Settings:** N/A

**Best Practices:** Configure this setting to true in workflows where document integrity and auditability are of utmost concern, such as legal, HR, and financial processes. Avoid enabling it in less critical workflows to keep the user experience flexible.