# Disable Preview Of Workflow Form

**Technical Name:** DisablePreviewOfWorkflowForm

**Category:** Workflow

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

This parameter configures the Pathlock Cloud GRC platform to disable the preview functionality of the workflow form during the StartStep of a workflow action. This feature is intended to restrict visibility into the form prior to or during its initiation, enhancing control over the workflow process.

**Business Impact:**

Disabling the preview of workflow forms ensures that sensitive information or workflow logic is not prematurely exposed to unauthorized users. This control is crucial in organizations where information sensitivity and access control are paramount, especially in regulated industries. By managing visibility, organizations can also control the pace at which information is disclosed during the workflow process, thereby managing expectations and avoiding potential misunderstandings or security issues.

**Technical Impact when configured:**

When this parameter is configured, users will not be able to preview the workflow form at the StartStep action. This means that until the workflow is officially initiated or reaches a subsequent step where preview is allowed, the form's contents, including fields and possibly attached roles or permissions, remain hidden from the user's view. This can affect how quickly a workflow is initiated, as users might need to start the process without full visibility of the form's contents.

**Example Scenario:**

In a scenario where a company has strict regulations around role assignment and permission grants, the Disable Preview Of Workflow Form parameter could be used to ensure that no preliminary information is visible before the official workflow initiation. This ensures that only users with the requisite authority and at the correct workflow stage can view and act upon the information contained within the workflow form.

**Related Settings:**

- `ExcludedRoleViewForReferenceUserRoles`

**Best Practices:** Configure this parameter in workflows where information sensitivity is high and preliminary visibility could lead to security or compliance implications. Avoid using it in workflows where form preview could aid in efficiency or user compliance, unless alternative measures are in place to mitigate any resultant delays or lack of visibility.