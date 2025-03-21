# Enable Rich Text Comment In Workflow Approval

**Technical Name:** EnableRichTextCommentInWorkflowApproval

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter allows for the inclusion of rich text formatting within comments made during the workflow approval process. This enhances clarity, emphasis, and organization of feedback or instructions provided by approvers or reviewers in the context of workflow actions.

**Business Impact:**

Implementing rich text comments enhances communication effectiveness in approval workflows. It allows approvers to use formatting tools such as bold, italics, and underlining to highlight critical information, leading to better understanding and faster decision-making. This feature is especially beneficial in complex workflow scenarios where detailed instructions or feedback is necessary.

**Technical Impact when configured:**

Once enabled, this setting impacts the workflow approval process by allowing the entry of formatted text within the comments section. This can include HTML tags for styling purposes. It requires that the user interface supporting the workflow approval process is capable of rendering and editing rich text.

**Examples Scenario:**

An approver needs to reject a workflow item due to missing information but wants to provide detailed instructions on what is missing and how to correct it. By using rich text comments, the approver can structure the feedback more effectively, using bullet points, bold for emphasis, or underlining key sections to ensure the submitter understands the action items clearly.

**Related Settings:** 

- `IsApproveAsyncForActions`: This setting, when enabled, determines if the approval process for actions within the workflow should be handled asynchronously.

**Best Practices:** 

- **Configure when:** Rich text comments are essential for improving clarity and emphasis in feedback during complex workflow approvals. This is particularly useful in environments where workflows are complex and require detailed instructions or feedback.
  
- **Avoid when:** Simple, straightforward workflows are in use, and there is no need for enhanced text formatting capabilities, which might introduce unnecessary complexity for users.