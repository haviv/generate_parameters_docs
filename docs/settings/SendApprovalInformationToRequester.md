# Send Approval Information To Requester

**Technical Name:** SendApprovalInformationToRequester

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether approval information related to role assignment workflows is sent to the requester upon the completion of the approval process.

**Business Impact:**

Enabling this feature ensures transparency and keeps the requester informed about the status of their requests, which can enhance trust and communication within the organizational processes. It is particularly beneficial in scenarios where role assignments are critical to timely access for completing business tasks.

**Technical Impact when configured:**

When configured, this parameter triggers notifications to be sent to the requester with details about the approval or rejection of their requests. This includes information on newly assigned roles, promoting efficient communication and minimizing delays in workflow processes.

**Examples Scenario:**

A user requests access to a specific SAP role required for completing a quarterly financial report. Once the request is processed and a decision is made, the SendApprovalInformationToRequester parameter ensures that the user is promptly informed about the approval status, enabling them to proceed with their responsibilities without unnecessary delays.

**Related Settings:**

- NewRoleName

**Best Practices:** 

- **Configure when:** Immediate feedback to requesters is essential for maintaining operational efficiency and transparency.
- **Avoid when:** In cases where notification volume could overwhelm the requester or when the approval process outcome is communicated through other means.