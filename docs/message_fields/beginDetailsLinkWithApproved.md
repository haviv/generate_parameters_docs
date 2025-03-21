**Field Name:** beginDetailsLinkWithApproved

**Description:** The `beginDetailsLinkWithApproved` field is a placeholder used in email templates within Pathlock Cloud. This placeholder is likely replaced by a hyperlink that directs the email recipient to a detailed view of a workflow request. The "approved" suffix suggests that this link may guide the user to a specific view or section where approval details are prominently presented, or that it is relevant in contexts where the request has been approved.

**Usage Context:** This field is typically used in email templates that are part of a workflow process. It appears in contexts where a detailed view of a request with an approved status is required, potentially allowing users to follow up on or manage requests that have recently been approved. These templates are most likely dispatched during various notification events related to workflow changes or updates.

**Example:**

Approve directly: $$beginDetailsLinkWithApproved$$

After rendering:

Approve directly:  
<a href="https://cloud.pathlock.com/requests/details?instanceGuid=abc123&p2=uniqueEmailId&p3=hashedUniqueEmailId">Approve</a>