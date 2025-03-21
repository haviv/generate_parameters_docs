# Take Workflow Mail From Requester

**Technical Name:** TakeWorkflowMailFromRequester

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls whether the email notification related to the workflow action should take the mail from the requester involved in the workflow. It's specifically used in scenarios where communication clarity and directness are paramount, like in ChangeUserPassword actions within the workflow.

**Business Impact:**

Enabling this feature ensures that emails regarding critical workflow actions, such as password changes, are sent directly from the requester, increasing transparency and trust in the communication process. It helps in reducing confusion and makes the audit trails regarding such sensitive actions clearer.

**Technical Impact when configured:**

When enabled, this will alter the default behavior of the email notification system within the workflow action to use the requester's email address. This can affect the perception of the legitimacy and source of the email, potentially improving open rates and compliance with the requested action.

**Examples Scenario:**

- In a scenario where a user's password needs to be changed as part of a workflow, enabling this parameter would ensure that the notification email sent to involved parties (like the user themselves or IT support) appears to come directly from the user who initiated the request, rather than a generic system email. This can be particularly important in sensitive HR or security-related workflows where clear sources of requests are necessary.

**Related Settings:**

- DefaultUserForProfileTailorWorkflow
- AutomaticSubmitGroupName

**Best Practices:** 

- **Configure when:** Transparency and clear lines of communication are critical, or when audit trails need to reflect the direct involvement of requesters in the communication process.
  
- **Avoid when:** The use of requester email addresses may violate privacy policies or when the generalized source of workflow notifications is preferred for consistency or policy reasons.