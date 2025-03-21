**Field Name:** requestRole

**Description:** The `requestRole` field is used to represent the role name associated with a workflow authorization request. It is employed in email templates to provide details about the specific role for which access or permission is being requested. This allows recipients of the email to quickly identify the role in question and understand the context of the request.

**Usage Context:** This field is typically used in email templates as part of workflow notifications, particularly in scenarios where users need to be informed about role-based access requests within the system. It is applicable in contexts such as request received, request approved, request denied, and waiting for approval notifications. The value assigned to `requestRole` comes from the role name defined in the workflow authorization request, which helps in providing clarity and context to the email recipients.

**Example:**

    Approve directly: $$beginApproveStepLink$$

    After rendering:

    Approve directly:  
    <a href="https://cloud.pathlock.com/approve?id=45321&action=1">Approve</a>