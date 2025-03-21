# Workflow Comments Email Template

**Technical Name:** WorkflowCommentsEmailTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** The Workflow Comments Email Template ID parameter specifies the unique identifier of the email template used for sending notifications related to workflow comments. This configuration is utilized when automated emails need to be dispatched as part of workflow actions, such as when a request is approved.

**Business Impact:** Proper configuration of this parameter ensures that stakeholders and participants in a workflow are appropriately notified about updates, comments, or approvals, facilitating better communication and efficiency in the process management. Misconfiguration could result in the failure to communicate critical information, leading to delays or misunderstandings in the workflow process.

**Technical Impact when configured:** Once configured, this parameter determines the template for emails sent in relation to workflow comments across various scenarios like request approvals within the Pathlock GRC platform. This ensures that all notifications adhere to a standardized format, contributing to a consistent user experience and effective information dissemination.

**Examples Scenario:** A user submits a request for access rights within the GRC platform. Upon approval, an automated email is dispatched to the requester using the template specified by the WorkflowCommentsEmailTemplateId. This email notifies the requester of the approval, any comments made during the review process, and subsequent actions they may need to take.

**Related Settings:** `EmailType.RequestApproved` 

**Best Practices:** Configure when you have a standardized email template that should be used for all workflow-related communications to maintain consistency and clarity in message dissemination. Avoid configuration with an incorrect ID to prevent email notification failures.