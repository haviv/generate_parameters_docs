# Workflow Allow Return Request To Requester

**Technical Name:** WorkflowAllowReturnRequestToRequester

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The Workflow Allow Return Request To Requester parameter enables a workflow action that allows requests within a workflow to be returned to the requester for additional information or clarification, enhancing the request handling process.

**Business Impact:**

Incorporating this parameter into the workflow can significantly enhance the efficiency and effectiveness of request management by providing an additional layer of flexibility. It allows for clearer communication and ensures that all necessary information is provided before final approval, thus minimizing the potential for errors or misunderstandings.

**Technical Impact when configured:**

When configured, this parameter modifies the behavior of the system to allow an option for requests to be sent back to the requester. This ensures a dynamic and interactive request handling process where necessary adjustments or additional information can be solicited directly from the source.

**Examples Scenario:**

An employee submits a request for access to a specific application, but the request lacks sufficient justification or details for the access level requested. With the Workflow Allow Return Request To Requester parameter enabled, the approver can return the request to the employee with comments requesting further details or clarification, ensuring that access is granted appropriately and in compliance with company policies.

**Related Settings:**

**Best Practices:** configure when a process requires interactive feedback or additional information from requesters. Avoid when the workflow process is linear and does not require or benefit from additional input.