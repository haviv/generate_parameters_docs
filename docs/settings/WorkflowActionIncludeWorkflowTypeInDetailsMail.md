# Workflow Action Include Workflow Type In Details Mail

**Technical Name:** WorkflowActionIncludeWorkflowTypeInDetailsMail

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:** The 'WorkflowActionIncludeWorkflowTypeInDetailsMail' parameter controls whether the type of workflow is included in the details mail. This is relevant when automated mails are sent out as part of workflow actions to provide recipients with better context about the workflow process.

**Business Impact:** Including the workflow type in emails can significantly enhance the understanding and responsiveness of the email recipients. It ensures that individuals involved in a process are aware of the context and can act accordingly, potentially reducing the time taken to complete a workflow and improving compliance and governance practices.

**Technical Impact when configured:** When enabled, this parameter ensures that emails related to workflow actions include a clear reference to the workflow's type, encouraging more efficient communication and process handling among the team members and stakeholders involved. 

**Example Scenario:** Consider a scenario where an organization has multiple workflows for processing different types of requests, such as access requests, incident reports, and change requests. Enabling this parameter ensures that each email notification sent as part of these workflows clearly indicates the type of request or process it relates to, helping recipients to prioritize their actions.

**Related Settings:** EnableDigitalSignForWorkflow

**Best Practices:** 
- **Configure when:** Communication clarity in process workflows is deemed critical for your organization. Particularly useful in environments where multiple workflow types exist, and distinguishing between them quickly can aid in prompt and appropriate actions by the recipients.
- **Avoid when:** Including extra data in emails could contravene company policies on email content, or if it's determined that such information does not add significant value to the recipients.