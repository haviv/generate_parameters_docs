# Send Mail On Workflow Declined To Current Approvers

**Technical Name:** SendMailOnWorkflowDeclinedToCurrentApprovers

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:** This parameter controls whether an email notification is sent to the current approvers when a workflow is declined. It ensures that all relevant parties are promptly informed about the decision, enabling them to take necessary actions or to be aware of the workflow's status.

**Business Impact:** Activating this parameter can significantly enhance communication and transparency throughout the workflow approval process. It provides immediate feedback to approvers, which is crucial for maintaining operational efficiency and for timely responses in dynamic business environments.

**Technical Impact when configured:** When set to true, the system triggers an email notification to the current approvers if a workflow associated with them is declined.

**Examples Scenario:** If a user requests access to a sensitive system and the request is declined by a manager, setting this parameter to true would ensure that all approvers in the workflow receive an email notification about this decline. This is especially useful in scenarios where quick reallocation or reassessment of access rights is necessary.

**Related Settings:** N/A

**Best Practices:** Configure this parameter to true in environments where immediate notification is essential for maintaining workflow momentum and oversight. Avoid enabling it in contexts where email notifications might overwhelm approvers or where such immediacy is not necessary.