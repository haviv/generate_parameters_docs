# Workflow Action Send Mail For Each Employee

**Technical Name:** WorkflowActionSendMailForEachEmployee

**Category:** Workflow

**Default Value:**

**Impact Level:** High

**Description:**

The `WorkflowActionSendMailForEachEmployee` parameter is designed to enable or disable the sending of emails to each employee involved in a workflow action, particularly when a specific action is designated for help desk notification. This functionality is crucial for organizations seeking to automate communication and ensure timely notifications during various workflow actions.

**Business Impact:**

Enabling this parameter enhances transparency and communication efficiency within an organization, ensuring that employees are promptly informed about relevant workflow actions affecting them or requiring their attention. This can directly impact the company's operations by reducing response times, improving the tracking of action items, and ultimately contributing to a more efficient and compliant organizational process.

**Technical Impact when configured:**

When configured, this setting will automatically trigger emails to be sent to all relevant employees for each action required within a specific workflow. This includes automatically determining when a single help desk group is involved and sending a consolidated notification to that group, thereby simplifying the communication process and ensuring all involved parties are informed.

**Examples Scenario:**

For instance, if an action to update user permissions is initiated and requires verification or approval, enabling `WorkflowActionSendMailForEachEmployee` would ensure that emails are sent out to every individual whose permissions are to be changed, as well as to the help desk group responsible for executing the change. This ensures everyone is informed and can take necessary actions or provide approvals promptly.

**Related Settings:**

- `RefreshUserOnWorkflowCompleted`
- `CUAPrefixForRfcDestinations`

**Best Practices:** 

- Configure this parameter to enhance communication and transparency within workflow processes, especially in complex or sensitive actions requiring attention from multiple employees or departments.
- Avoid enabling this feature for actions that are too trivial or frequent, which could lead to email overload and reduce the effectiveness of communication.