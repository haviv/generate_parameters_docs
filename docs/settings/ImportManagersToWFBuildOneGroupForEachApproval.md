# Create One Approval Group For Each Approver

**Technical Name:** ImportManagersToWFBuildOneGroupForEachApproval

**Category:** Workflow

**Default Value:** Not Provided

**Impact Level:** Medium

**Description:** This parameter controls the process of importing approvers into the Pathlock Cloud GRC platform. When enabled, it specifically targets the creation of unique approval groups for each imported approver, ensuring a streamlined and organized workflow for approval processes.

**Business Impact:** Enabling this parameter enhances the approval workflow by creating distinct groups for each approver within an organization. This organization aids in clarifying the approval hierarchy and simplifies the task of managing permissions and approvals, thus enhancing governance, risk management, and compliance (GRC) within the organization.

**Technical Impact when configured:** Once configured, the system will automatically generate dedicated approval groups for each approver imported into the workflow system. This separation aids in the granular management of approvals and permissions, streamlining the workflow process.

**Examples Scenario:** In a scenario where multiple managers need to approve various compliance documents, this parameter, when enabled, would create a distinct group for each manager. This setup ensures that documents are routed correctly for approval based on the organization's compliance workflow, thus avoiding any confusion or mismanagement in the approval process.

**Related Settings:** 

- `AuthorizationReviewDisableSubmitApproval`
- `AuthorizationReviewShowPartialApprovalIcon`

**Best Practices:** 

- **Configure when:** You have a complex approval hierarchy within your organization and need to distinctly manage approvals by each approver. It is also beneficial when clear audit trails of approval processes are required.
- **Avoid when:** Your organization's approval process is straightforward or involves a small number of approvers. In such cases, creating separate groups for each approver might complicate the workflow unnecessarily.