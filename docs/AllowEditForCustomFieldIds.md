**Technical Name:** AllowEditForCustomFieldIds

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter controls which custom fields within workflow requests can be edited by the user. It ensures that only authorized fields are editable, maintaining the integrity of workflow data.

**Business Impact:** Allows organizations to maintain data integrity within their workflows by ensuring only specified fields can be edited. This is crucial in scenarios where certain data should remain consistent to comply with internal policies or external regulations.

**Technical Impact when configured:** When configured, it restricts editing capabilities to the specified custom field IDs within workflow requests. This prevents unauthorized modifications, ensuring that workflow data remains accurate and consistent.

**Example Scenario:** If the organization has a workflow for access request approvals and includes custom fields for detailing the access rights required, the `AllowEditForCustomFieldIds` parameter can be set to include only those fields that the requesting user can fill or edit, such as justification or request details, while leaving fields related to approval status or reviewer comments non-editable.

**Related Settings:** WorkflowAdditionalRecipientOnRequestMail

**Best Practices:** 
- Configure when specific fields in a workflow request form need to remain constant after the initial submission to ensure compliance and data integrity.
- Avoid when users need full flexibility to edit all fields in their workflow requests, or if the workflow design includes mechanisms to track and revert unauthorized changes effectively.