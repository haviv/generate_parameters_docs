# Message Fields Documentation for Pathlock Cloud 

## Overview

### Description
Message Fields are template placeholders used in email notifications and workflow communications within the Pathlock Cloud platform. They allow dynamic content insertion into email templates and workflow messages, making communications contextual and personalized.

### Business Usage
These fields are primarily used when:
- Configuring email notification templates
- Setting up workflow approval communications
- Creating custom messages for different workflow stages
- Building links for user actions in emails

### Example Template
Here is a sample email template using message fields:

    Subject: Access Request #$$requestId$$ Requires Your Approval
    
    Dear $$groupOrManager$$,
    
    A new access request requires your review and approval:
    
    Request ID: $$requestId$$
    Requester: $$userName$$
    Request Type: $$requestType$$
    Comments: $$comment$$
    
    Click here to approve: $$beginApproveStepLink$$
    Click here to reject: $$beginRejectStepLink$$
    
    Thank you,
    $$adminName$$

**Field Name:** requestId

**Description:** The `requestId` field represents the unique identifier of the workflow instance. It is used in email templates to reference specific requests within the Pathlock Cloud system. This field helps recipients and workflow participants identify and track specific workflow requests in email communications.

**Usage Context:** The `requestId` field is typically used in email templates related to workflow processes. It appears in emails to indicate the ID of a particular request that is pending approval, has been approved, denied, or requires some action within a workflow.

**Example:**

    Approve directly: $$requestId$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/request?id=12345">Request Details</a>
-----------------------------------
**Field Name:** userName

**Description:** The `userName` field represents the full name of the user associated with a particular workflow instance. It is inserted into email templates to personalize messages by identifying the recipient or subject of the workflow action.

**Usage Context:** This field is typically used in email templates related to workflow processes, such as notifications for approval requests, request statuses, and other workflow actions. It helps identify the user for whom the workflow action is relevant, ensuring the email communication is clear and personalized.

**Example:**

    Hi $$userName$$, your request is being processed.

    After rendering:

    Hi John Doe, your request is being processed.
-----------------------------------
**Field Name:** adminName

**Description:** The `adminName` field represents the name of the workflow administrator. Its purpose is to personalize email templates by including the administrator's name, particularly in email notifications sent when there are no recipients specified and the email is sent to the workflow administrator as a fallback.

**Usage Context:** This field is typically used in email templates when there are no recipients available to receive an email notification related to a workflow process. In such cases, the email notification is directed to the workflow administrator, and the `adminName` is used to address the administrator within the message, maintaining a personal touch in the communication. 

**Example:**

    Admin Contact: $$adminName$$

    After rendering:

    Admin Contact: John Doe
-----------------------------------
**Field Name:** beginWaitingForApproveLink

**Description:** This field represents a placeholder for generating hyperlinks that direct users to the approval status page of a specific workflow instance. It is used to guide the recipients to view the details, status, and actions required for pending approvals within the Pathlock Cloud platform.

**Usage Context:** The `beginWaitingForApproveLink` field is typically used in email templates within workflow processes to notify managers or other stakeholders that a particular request is awaiting approval. It provides a direct link for approvers to access the workflow's status page, enabling them to act on requests that require their attention.

**Example:** 

    Approve directly: $$beginWaitingForApproveLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/status?workflowId=12345&recipient=uniqueUserId&hash=abcdef123456">View Approval Status</a>
-----------------------------------
**Field Name:** beginRequestStatusLink

**Description:** The field `beginRequestStatusLink` is a placeholder used in email templates to insert a hyperlink. This link directs the user to a webpage where they can view the status of a specific workflow request. It is used to provide users with a direct and convenient way to access request status information within workflow-related email notifications.

**Usage Context:** This field is typically used in email templates that notify users about actions taken on their workflow requests, such as approvals, rejections, or when a request has been received. It's particularly used to enhance communication in workflow processes by providing direct access to detailed request status.

**Example:**

    Check request status: $$beginRequestStatusLink$$

    After rendering:

    Check request status:  
    <a href="https://cloud.pathlock.com/requestStatus?id=45321&p2=&p3=">Request Status</a>
-----------------------------------
**Field Name:** endLink

**Description:** The `endLink` field is used to denote the closure point of a hyperlink in email templates. It functions as a placeholder in templates that are formatted using a specific email template system within Pathlock Cloud. Once rendered, it typically translates to the closing anchor tag in HTML, completing an actionable link in the email content.

**Usage Context:** This field is typically used in email templates that are part of workflow processes where it's essential to provide recipients with direct, actionable links pertaining to their tasks or notifications. Common scenarios involve approving requests or accessing specific pages within the platform. This ensures that emails can include dynamic links directed towards specific recipients or actions.

**Example:**

    Link to Approver Page: $$beginApproveStepLink$$

    endLink

    After rendering:

    Link to Approver Page:  
    <a href="https://cloud.pathlock.com/approvedetail?id=45321">Here</a>
-----------------------------------
**Field Name:** groupOrManager

**Description:** This field represents the name of the group or manager responsible for handling a specific workflow step. It is used to provide recipients with information about who has the authority or oversight over the workflow in question.

**Usage Context:** The `groupOrManager` field is typically used in email templates as part of communication during workflow processes. It is inserted to inform recipients about which group or manager is associated with a workflow step, adding context and clarity to the approval or decision-making processes. This might be particularly important in approval emails where the recipient needs to understand the hierarchy or responsibility chain associated with the workflow item.

**Example:**

    Approve Step: $$beginApproveStepLink$$  
    Group Responsible: $$groupOrManager$$

    After rendering:

    Approve Step:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>  
    Group Responsible: Finance Manager Smith
-----------------------------------
**Field Name:** beginApproveStepLink

**Description:** The `beginApproveStepLink` field is a placeholder used in email templates to provide a link for recipients to approve a step within a workflow. This link, when rendered, dynamically generates a URL that directs the user to the approval page for a specific step in the workflow process. The inclusion of query parameters ensures that the appropriate step and user context is considered when the link is created.

**Usage Context:** The `beginApproveStepLink` is typically used in email notifications sent during workflow processes where a recipient needs to take an approval action. This is commonly used in situations where a step in a workflow requires approval from a manager or group. The inclusion of this link in an email template ensures a streamlined approach for users to directly perform the necessary approval actions without needing to navigate manually through the system.

**Example:**

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
-----------------------------------
**Field Name:** beginRejectStepLink

**Description:** The `beginRejectStepLink` field is used in email templates within the Pathlock Cloud platform to insert a hyperlink that allows users to reject a step in a workflow process. This field is part of the mechanism for handling workflow step approvals and rejections. When rendered, it provides an actionable link that a recipient can click to directly execute a rejection action on the corresponding workflow instance step.

**Usage Context:** This field is typically used in workflow-related email notifications that require user interaction to reject a workflow step. It's included in emails aimed at managers or other stakeholders who can either approve or reject requests within the workflow. The link is dynamically generated based on the current context of the workflow step and allows for immediate interaction directly from the email.

**Example:**

    Reject Request: $$beginRejectStepLink$$

    After rendering:

    Reject Request: 
    <a href="https://cloud.pathlock.com/approve?id=45321&action=2">Reject</a>
-----------------------------------
**Field Name:** beginMoveBackStepLink

**Description:** The `beginMoveBackStepLink` field in Pathlock Cloud's email template system is used to generate a hyperlink within an email that allows users to move a step within a workflow process back to a previous step. This feature is a part of the workflow management system, enabling users to revisit earlier stages of an approval or a review process.

**Usage Context:** This field is typically used in email templates that are sent as part of various workflow processes. It is particularly applicable in scenarios where action needs to be taken on a step in the workflow, such as moving a step back to a prior stage, to facilitate revisions or re-evaluations in workflow processes.

**Example:** 

    Move step back: $$beginMoveBackStepLink$$

    After rendering:

    Move step back:  
    <a href="https://cloud.pathlock.com/stepMoveBack?id=45321&action=3">Move Back</a>
-----------------------------------
**Field Name:** comment

**Description:** The `comment` field is used to insert specific messages or notes associated with a workflow instance in email templates. These comments are typically user-generated inputs or notes entered during workflow steps and are intended to provide context or additional information relevant to the workflow process.

**Usage Context:** This field is typically used in email notifications related to workflows to convey user comments or important notes that were provided during a workflow step. It is commonly included in messages that inform users or administrators about the ongoing status or details of a workflow process, such as when a request is received, awaiting approval, or completed.

**Example:**

    User Comment: $$comment$$

    After rendering:

    User Comment: The request requires additional documents before approval.
-----------------------------------
**Field Name:** requestTransaction

**Description:** The `requestTransaction` field represents a formatted description of the transaction involved in a workflow process. This field provides context and details regarding the transaction for which the approval or other actions are being requested in the workflow. It is used to inform recipients of the specific transaction details that are under review or action in the email templates.

**Usage Context:** The `requestTransaction` field is typically used in email templates associated with the workflow process to notify users about a transaction that requires approval or has been initiated. It is included in emails as part of the necessary information to give recipients insight into what transaction is being referred to without requiring them to access the workflow system directly. It is particularly relevant when transactions are related to specific requests, roles, or SAP activities processed within Pathlock Cloud workflows.

**Example:** 

    Transaction Details: $$requestTransaction$$

    After rendering:

    Transaction Details: Travel Expense Approval for Q3 2023
-----------------------------------
**Field Name:** requestRole

**Description:** The `requestRole` field is used to represent the role name associated with a workflow authorization request. It is employed in email templates to provide details about the specific role for which access or permission is being requested. This allows recipients of the email to quickly identify the role in question and understand the context of the request.

**Usage Context:** This field is typically used in email templates as part of workflow notifications, particularly in scenarios where users need to be informed about role-based access requests within the system. It is applicable in contexts such as request received, request approved, request denied, and waiting for approval notifications. The value assigned to `requestRole` comes from the role name defined in the workflow authorization request, which helps in providing clarity and context to the email recipients.

**Example:**

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
-----------------------------------
**Field Name:** requestType

**Description:** The `requestType` field represents the type of request being processed within a workflow. It helps categorize the nature of the workflow request, such as a general action, specific activity, or role assignment. This field is used to provide context about the workflow request in email notifications, ensuring recipients have a clear understanding of the action being taken or requested.

**Usage Context:** The `requestType` field is typically used in email templates that are part of the workflow process. It is included in notifications sent out to users, providing them with a short, descriptive label about the type of request being processed. This field is populated based on the transaction or role associated with the workflow request.

**Example:** 

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
-----------------------------------
**Field Name:** stepStart

**Description:** The `stepStart` field represents the starting time of a specific step within a workflow process in Pathlock Cloud. It is a DateTime value captured at the initiation of a step and is used as a parameter in email templates to convey timing information related to the workflow steps.

**Usage Context:** This field is typically used when sending email notifications as part of the workflow process to provide details about when a particular step in the workflow was started. The `stepStart` field can be included in various email notifications for different workflow scenarios, aiding recipients to understand the timeline and state of the workflow action.

**Example:**

    Workflow step started at: $$stepStart$$

    After rendering:

    Workflow step started at:  
    2023-10-19T14:30:00Z

-----------------------------------
**Field Name:** stepEnd

**Description:** The `stepEnd` field represents the date and time at which a specific workflow step is completed in the Pathlock Cloud workflow process. It is used to capture and display the completion time of an action or approval step within a workflow.

**Usage Context:** The `stepEnd` field is typically used in email templates that notify users about the completion of workflow steps. It provides recipients with a timestamp for when a particular step in the workflow process is finalized, thereby helping users track the progress and history of workflow actions. This is especially useful in contexts where a timestamp of completion is critical for auditing or tracking purposes, such as in compliance or certification processes.

**Example:**

    Completion Time: $$stepEnd$$

    After rendering:

    Completion Time:  
    2023-09-21 15:30:00
-----------------------------------
**Field Name:** stepTargetEndTime

**Description:** The `stepTargetEndTime` field represents the target end time for a step in a workflow process. It indicates when a particular step is expected to be automatically approved or concluded if it is not completed before this time.

**Usage Context:** This field is typically used in email templates related to workflow processes. It is relevant in contexts where the automatic transition or conclusion of a workflow step is involved, such as in emergency access reporting. It provides the recipients with information on the deadline by which a workflow step is expected to be automatically processed.

**Example:**

    Approve directly: $$stepTargetEndTime$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
-----------------------------------
**Field Name:** requestInformation

**Description:** The `requestInformation` field combines the type and relevant details of a user's workflow request. It's used to provide a concise description of the request within email templates. This field is part of a dictionary that holds various message parameters, forming part of the content in notification emails.

**Usage Context:** The `requestInformation` field is used in email templates associated with workflow steps in Pathlock Cloud. It captures a summary of the request, including its type (e.g., "Free Request", "Role", "Activity") and additional comments, enhancing the clarity of email communications concerning the workflow status.

**Example:**

    Request details: $$requestInformation$$

    After rendering:

    Request details:  
    Role - Administrator Access
-----------------------------------
**Field Name:** sapUserName

**Description:** The `sapUserName` field represents the SAP user name associated with a workflow instance. It is used in email templates to personalize content related to SAP user-specific actions or notifications during workflow processes.

**Usage Context:** This field is typically used in email templates for workflows that involve actions or notifications directly related to a SAP user. For instance, it is included to personalize messages sent to users or administrators concerning workflow instances specific to SAP user activities, such as approvals, rejections, or reviews.

**Example:**

    Approve directly: $$sapUserName$$

    After rendering:

    Approve directly: john.doe.sapuser
-----------------------------------
**Field Name:** beginDetailsLink

**Description:** The `beginDetailsLink` field in an email template is used to insert a hyperlink for users to navigate to the detailed view of a specific workflow instance. When rendered, it generates a URL that directs the recipient to a webpage displaying all pertinent details of the workflow, allowing them to review the instance's information.

**Usage Context:** This field is typically used in email templates during the workflow communication process where providing access to detailed information is necessary. It is included in notifications where the user needs to view some aspects of the workflow to make informed decisions or to review progress.

**Example:**

    Details link: $$beginDetailsLink$$

    After rendering:

    Details link:  
    <a href="https://cloud.pathlock.com/details?id=29712">View Details</a>
-----------------------------------
**Field Name:** previousApprover

**Description:** The `previousApprover` field represents the user or group that was responsible for handling the last step in a workflow process before the current one. It is used to provide context about who previously managed the request, allowing recipients of the email to understand who last handled the approval.

**Usage Context:** The `previousApprover` field is typically used in email templates sent during workflow processes, especially when a step in the workflow is reverted or moved back, and users need to know who previously managed the request. It provides transparency and continuity by indicating the last handling authority when notifications are sent out about workflow updates.

**Example:**

    Approver Information: $$previousApprover$$

    After rendering:

    Approver Information: John Doe
-----------------------------------
**Field Name:** previousApproverComments

**Description:** The `previousApproverComments` field represents the comments provided by the approver in the previous step of a workflow process. It is used to convey any feedback, decisions, or notes made by the approver regarding the workflow item they processed.

**Usage Context:** This field is typically used in email templates that notify users or stakeholders about the status or progression of a workflow. It informs recipients about the previous approver's input, which can be crucial for understanding the context or reasons behind the workflow's current status. It is often included in emails triggered when a request has been moved back, declined, or requires further action from other approvers.

**Example:**

    Previous Approver's Comments: $$previousApproverComments$$

    After rendering:

    Previous Approver's Comments:  
    The request requires additional documentation. Please provide the missing information for a more comprehensive review.
-----------------------------------
**Field Name:** reapprove

**Description:** The `reapprove` field is a placeholder used in email templates to generate a link that enables users to reapprove a previously denied or modified request within a workflow. This link is essential for workflows where requests can be returned for reapproval due to changes or additional information.

**Usage Context:** The `reapprove` field is typically used in email templates for informing approvers when a request requires reapproval. This happens in scenarios where a request has been returned to a previous step in the workflow, and the original decision needs to be reassessed.

**Example:**

    Reapprove this request: $$reapprove$$

    After rendering:

    Reapprove this request:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=4">Reapprove</a>
-----------------------------------
**Field Name:** beginRequestsWaitingLink

**Description:** This field serves as a placeholder for inserting a hyperlink in email templates. The hyperlink directs the workflow participant to a page where they can view all their pending requests awaiting approval. The link provides a convenient entry point for users to manage and track their workflow activities within the Pathlock Cloud platform.

**Usage Context:** The `beginRequestsWaitingLink` field is used in email templates sent during workflow processes, particularly in notifications related to request status updates. It's typically included in emails that inform users about action items waiting for their attention, such as tasks they need to approve as part of the workflow process.

**Example:** 

    Review pending requests: $$beginRequestsWaitingLink$$

    After rendering:

    Review pending requests:  
    <a href="https://cloud.pathlock.com/requests?id=currentUserId">Pending Requests</a>
-----------------------------------
**Field Name:** beginRequestsWaitingLinkForCurrentInstance

**Description:** The `beginRequestsWaitingLinkForCurrentInstance` field is used to create a hyperlink in email templates that directs the recipient to a page where they can view all waiting requests for a specific workflow instance. This field helps in providing a direct access link to the relevant section of Pathlock Cloud where the waiting requests are listed.

**Usage Context:** This field is typically used in workflow-related email notifications when it's necessary to inform a user about pending requests awaiting their attention for a specific instance. It is primarily employed in scenarios related to process management and needs for immediate action or review by the recipient.

**Example:** 

    View all pending requests: $$beginRequestsWaitingLinkForCurrentInstance$$

    After rendering:

    View all pending requests:  
    <a href="https://cloud.pathlock.com/requests-waiting?id=12345">View Requests</a>
-----------------------------------
**Field Name:** beginAuhtorizationReviewPortalLink

**Description:** The `beginAuhtorizationReviewPortalLink` field represents a placeholder within email templates that is used to generate a hyperlink directing users to the Authorization Review Portal in Pathlock Cloud. It is used to provide recipients with easy access to begin or review authorization processes directly from their email.

**Usage Context:** This field is typically used in email templates related to workflow processes, specifically when notifying users about tasks requiring them to access the Authorization Review Portal. It is employed in scenarios where recipients need to verify or review authorization details, ensuring they have a direct link to the relevant portal page.

**Example:**

    Visit the Authorization Review Portal: $$beginAuhtorizationReviewPortalLink$$

    After rendering:

    Visit the Authorization Review Portal: 
    <a href="https://cloud.pathlock.com/AuthorizationReviewPortal">Authorization Review Portal</a>
-----------------------------------
**Field Name:** beginDetailsLinkWithThankYou

**Description:** The `beginDetailsLinkWithThankYou` field represents a hyperlink that, when rendered in an email template, allows users to click and view details of a workflow instance step. This link is unique because it includes a "Thank You" acknowledgment as part of the URL, indicating that the user should be shown appreciation for reviewing the details.

**Usage Context:** This field is typically used in email templates sent during or after workflow processes, especially in contexts where it is important to acknowledge the user's contribution or action. It is used in situations where the email recipient is expected to review or interact with steps of a workflow, with an added note of thanks included in the interaction link.

**Example:**

    View details: $$beginDetailsLinkWithThankYou$$

    After rendering:

    View details:  
    <a href="https://cloud.pathlock.com/details?id=45321&thanks=1">View details with Thanks</a>
-----------------------------------
**Field Name:** requestOpenedOrReturned

**Description:** The `requestOpenedOrReturned` field is used within email templates to indicate the status of a workflow request. Specifically, it is intended to convey whether a request has been newly opened or has been returned in the course of a workflow process.

**Usage Context:** This field is typically used in email notifications sent to users involved in workflow processes. The specific context in which this field is employed includes scenarios where a request is either first initiated or returned to a previous step in the process. The field helps to inform the recipient of the current status of the request, which is crucial for tracking and managing tasks within a workflow.

**Example:** 

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>
-----------------------------------
**Field Name:** beginDetailsLinkGeneral

**Description:** The `beginDetailsLinkGeneral` field is used to insert a hyperlink in email templates that directs the recipient to the general details page of a specific workflow request. This field is typically used to enable email recipients to access more information about a workflow instance.

**Usage Context:** This field is used in email notifications sent during various stages of workflow processes in Pathlock Cloud. The link generated by this field allows workflow participants to review details pertaining to the workflow instance, helping them make informed decisions or take necessary actions.

**Example:**

    View details: $$beginDetailsLinkGeneral$$

    After rendering:

    View details: 
    <a href="https://cloud.pathlock.com/details?id=12345&p2=emailRecipientId&p3=hashValue">Details</a>
-----------------------------------
**Field Name:** beginDetailsLinkWithThankYouGeneral

**Description:** This field represents a placeholder in email templates used to generate a link to the details of a workflow request. It appends a query string to include identifying information of the email recipient for personalized tracking. The link is meant to be a general link format commonly used in "Thank You" scenarios after user actions.

**Usage Context:** This field is typically utilized in scenarios where the email template requires a link pointing to details of a related workflow request. The link includes a personalized aspect, identifying the recipient in contexts where a user might be expecting a confirmation or follow-up, such as after completing a specific action within a workflow process.

**Example:** 
  
    View Details: $$beginDetailsLinkWithThankYouGeneral$$

    After rendering:

    View Details:  
    <a href="https://cloud.pathlock.com/workflowdetails?guid=abc123&action=thankyou&user=xyz">View Details</a>
-----------------------------------
**Field Name:** beginApproveStepLinkGeneral

**Description:** The `beginApproveStepLinkGeneral` field in email templates represents a placeholder for generating a generic approval link within a workflow process. This link is intended for recipients to approve a step in the workflow without specific restrictions, careful of its usage of universal attributes, and dynamic user-specific identifiers. The generic version excludes particular step IDs, allowing a more flexible or unrestricted approval action when rendered.

**Usage Context:** The `beginApproveStepLinkGeneral` field is typically used in email templates where a general approval link is needed without binding the link to a specific step ID. It is suited for workflows where the approval action doesn't need to reference a particular step, providing a broader application of the approval functionality. This placeholder is replaced with an actual hypertext link pointing to the general approval endpoint with dynamic query parameters.

**Example:**

    Approve directly: $$beginApproveStepLinkGeneral$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?instanceGuid=<instance_guid>&Action=1&p2=<unique_identifier>&p3=<hashed_identifier>">Approve</a>
-----------------------------------
**Field Name:** beginUserOpenRequestsLink

**Description:** The `beginUserOpenRequestsLink` field serves as a placeholder in email templates, which is replaced by a hyperlink directing users to a page listing their open requests within the Pathlock Cloud platform.

**Usage Context:** This field is utilized in email templates associated with workflow processes. It is generally included in notifications to allow users easy access to view and manage their pending or active requests.

**Example:**

    View your open requests: $$beginUserOpenRequestsLink$$

    After rendering:

    View your open requests:  
    <a href="https://cloud.pathlock.com/openrequests">Open Requests</a>
-----------------------------------
**Field Name:** beginUserOpenRequestsBootstrapLink

**Description:** The `beginUserOpenRequestsBootstrapLink` field is used as a placeholder in email templates to generate a hyperlink that directs users to the 'Open Requests Bootstrap' page on Pathlock Cloud. This link provides users with access to view their current open requests, utilizing a modern Bootstrap-styled interface.

**Usage Context:** This field is typically used in email templates sent during workflow processes where users need to be informed or reminded about their pending requests. It facilitates easy access for users to view their open requests directly from the email, enhancing user experience and engagement with the workflow platform.

**Example:** 

    View your open requests: $$beginUserOpenRequestsBootstrapLink$$

    After rendering:

    View your open requests:  
    <a href="https://cloud.pathlock.com/OpenRequestsBootstrap">Open Requests</a>
-----------------------------------
**Field Name:** beginExtendStepLink

**Description:** The `beginExtendStepLink` field represents an HTML hyperlink in the email template that is generated for actions related to extending a workflow step. This link is dynamically populated to direct users to a specific step in the Pathlock Cloud platform where they can take further actions related to extending the workflow.

**Usage Context:** This field is typically used within email templates that are part of the identity and governance risk compliance (GRC) workflow processes. Specifically, it is included in workflows that allow or require users to take actions relative to extending a specific step. The link guides the recipient to a URL on Pathlock Cloud where they can perform actions necessary for the extension of a workflow step.

**Example:**

    Extend Step: $$beginExtendStepLink$$

    After rendering:

    Extend Step:  
    <a href="https://cloud.pathlock.com/stepExtend?guid=abc123def456">Extend</a>
-----------------------------------
**Field Name:** beginDetailsLinkWithApproved

**Description:** The `beginDetailsLinkWithApproved` field is a placeholder used in email templates within Pathlock Cloud. This placeholder is likely replaced by a hyperlink that directs the email recipient to a detailed view of a workflow request. The "approved" suffix suggests that this link may guide the user to a specific view or section where approval details are prominently presented, or that it is relevant in contexts where the request has been approved.

**Usage Context:** This field is typically used in email templates that are part of a workflow process. It appears in contexts where a detailed view of a request with an approved status is required, potentially allowing users to follow up on or manage requests that have recently been approved. These templates are most likely dispatched during various notification events related to workflow changes or updates.

**Example:**

    Approve directly: $$beginDetailsLinkWithApproved$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/requests/details?instanceGuid=abc123&p2=uniqueEmailId&p3=hashedUniqueEmailId">Approve</a>
-----------------------------------
**Field Name:** beginDetailsLinkWithDeclined

**Description:** The `beginDetailsLinkWithDeclined` field is used to produce a hyperlink in an email template which directs the recipient to a page detailing a request that has been declined within a workflow process. This link provides additional context or necessary information regarding the declined request, utilizing unique identifiers to ensure a secure and direct path specific to the user's session.

**Usage Context:** This field is typically used in email templates that are triggered during workflow processes, specifically those related to notifications about declined requests. The link assists recipients in quickly accessing detailed information about the decline decision, streamlining communication and follow-up actions related to the workflow.

**Example:**

    Decline details: $$beginDetailsLinkWithDeclined$$

    After rendering:

    Decline details:  
    <a href="https://cloud.pathlock.com/request/details?id=45321&Decision=0&WaitingRequests=0&p2=user123&p3=hashvalue">View Decline Details</a>
-----------------------------------
**Field Name:** beginApproveStepLinkThankYou

**Description:** The `beginApproveStepLinkThankYou` field is utilized in email templates to generate a hyperlink allowing the email recipient to approve a workflow step directly. This link, when clicked, will lead the recipient to an approval page, and will include a "Thank You" message upon successful approval.

**Usage Context:** This field is typically used in the context of workflow processes where an approver needs to verify and approve an action item. It is specifically employed in scenarios where the approval action is conditional on not needing further approval or processing. This field is rendered as part of the email template whenever an email is sent, alerting the recipient about the action they can take (i.e., approval) and making it more convenient by including a direct link.

**Example:**

    Approve here: $$beginApproveStepLinkThankYou$$

    After rendering:

    Approve here:  
    <a href="https://cloud.pathlock.com/approve?id=-1&action=1&WaitingRequests=0">Approve</a>
-----------------------------------
**Field Name:** beginApproveStepLinkGeneralForFF

**Description:** The `beginApproveStepLinkGeneralForFF` field is a placeholder used within email templates associated with workflow processes in Pathlock Cloud. This field is substituted with a hyperlink, enabling the recipient to approve a specific workflow step or request directly from the email. The URL generated includes a unique identifier and parameters specific to workflows that have an emphasis on fire-fighter (emergency) access, ensuring secure and user-specific access actions.

**Usage Context:** This field is typically used in email notifications that require an emergency or expedited approval action. It is utilized where the approver needs to take immediate direct approval actions, often in emergency scenarios linked to sensitive or high-priority requests that utilize fire-fighter access features. These emails are dispatched as part of Pathlock Cloud's workflow management system to streamline emergency decision-making processes.

**Example:**
    
    Approve directly: $$beginApproveStepLinkGeneralForFF$$

    After rendering:

    Approve directly:
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1&p2=uniqueApproverId&p3=hashedValue&StepType=FF">Approve</a>
-----------------------------------
**Field Name:** beginCreateTasksLink

**Description:** The `beginCreateTasksLink` field represents the starting HTML anchor tag for linking to the tasks associated with a specific workflow step in Pathlock Cloud. Its purpose is to provide recipients with direct access to the task page for creating or managing tasks related to the current workflow step within an email template.

**Usage Context:** This field is typically used in email templates that are part of Pathlock Cloud's workflow process notifications. It is particularly relevant when an email notification is sent out to inform a user or administrator about tasks that need to be created or managed for a given workflow instance. The field dynamically generates a link, which is injected into the email, allowing recipients to easily navigate to pertinent task information within the Pathlock Cloud platform.

**Example:**

    Create tasks directly: $$beginCreateTasksLink$$

    After rendering:
    
    Create tasks directly: 
    <a href='https://cloud.pathlock.com/Portal/WorkflowName/InstanceGuid/OpenTasks.aspx'>
-----------------------------------
**Field Name:** delegatedBy

**Description:** The `delegatedBy` field indicates the individual who delegated a particular task or responsibility. This field is used to identify when an action within a workflow has been delegated to another user, and it provides the name or identification of the person who performed the delegation.

**Usage Context:** The `delegatedBy` field is typically used in email templates related to workflow processes, specifically those that involve delegation actions. It is included in email notifications to inform recipients about the original authority or approver who delegated the task to them as part of the workflow execution. This is often relevant in steps where tasks can be assigned or passed to other personnel for approval or action.

**Example:**

    Delegated by: $$delegatedBy$$

    After rendering:

    Delegated by: John Doe
-----------------------------------
