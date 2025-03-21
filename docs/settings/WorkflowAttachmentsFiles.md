# Workflow Attachments Files

**Technical Name:** WorkflowAttachmentsFiles

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The WorkflowAttachmentsFiles parameter is designed for managing file uploads within workflow actions, particularly facilitating the handling, validation, and association of files uploaded by users as part of workflow processes in the Pathlock Cloud GRC platform.

**Business Impact:**

Proper configuration of this parameter ensures secure and efficient management of file attachments in workflow processes. It impacts how users interact with workflows requiring document uploads, significantly affecting compliance documentation, evidence submission for audit trails, and any process that involves uploading documents as part of a compliance or risk management procedure.

**Technical Impact when configured:**

- Enables file attachment capabilities in designated workflow actions.
- Ensures that file attachments are correctly associated with the specific workflow instances and user actions.
- Facilitates file size, type, and other validation rules to comply with organizational policies.

**Example Scenario:**

A user is completing a compliance checklist workflow that requires uploading a documented proof of action. Through the WorkflowAttachmentsFiles configuration, the system allows the user to upload the necessary document directly within the workflow interface, ensuring the document is correctly linked and stored as part of the workflow records.

**Related Settings:**

- `ApprovalComment` (as seen in the use of `ConfigurationManager.AppSettings["ApprovalComment"]` which is indirectly related through workflow approvals where attachments might be referenced or required.)

**Applicable Workflows Actions:**

- `FileUploadElement`

**Best Practices:** 

- **Configure when:** You have workflows that require or can significantly benefit from direct file uploads by users, such as compliance documentation, risk assessments, or any process needing evidence or documentation uploads.
- **Avoid when:** There is no clear requirement for file attachments within your workflows, or if your organization does not have the infrastructure to securely manage uploaded files.