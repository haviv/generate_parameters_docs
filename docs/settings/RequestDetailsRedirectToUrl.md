# Request Details Redirect To Url

**Technical Name:** RequestDetailsRedirectToUrl

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:** This parameter controls the redirection URL to which a user is sent upon taking specific actions within workflows, such as approval or movement of requests. It is designed to enhance navigational efficiency and user experience in workflow management.

**Business Impact:** Proper configuration improves the flow of managing requests by ensuring users are directed to the appropriate subsequent page, thereby streamlining the workflow process, reducing time spent on navigational tasks, and minimizing user error.

**Technical Impact when configured:** Configuring this parameter affects how the system responds after a workflow decision is made (e.g., request approval, denial, or revert actions), redirecting users to a predefined URL which could be tailored to lead them to their next logical step or task.

**Examples Scenario:** 
- When a user approves a request in the workflow, the system uses this parameter to redirect them to a confirmation page, enhancing the user's understanding of the action taken and providing clear next steps.
  
**Related Settings:** WorkflowInboxShowRequestDataTemplateText

**Best Practices:** 
- Configure this parameter to redirect users to relevant informational or action-oriented pages post workflow actions to enhance user experience and efficiency.
- Avoid using generic landing pages or URLs that do not contribute to the user's workflow process, as it could lead to confusion or inefficiency.