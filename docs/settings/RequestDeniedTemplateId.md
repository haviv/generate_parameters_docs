# Request Denied Template

**Technical Name:** RequestDeniedTemplateId

**Category:** Workflow

**Default Value:** 

**Impact Level:** High

**Description:** 

The Request Denied Template parameter is utilized within the Pathlock Cloud GRC platform to define the template ID for messages sent when a workflow request is denied. This setting ensures that users receive a consistent and clear notification regarding the denial of their requests.

**Business Impact:**

Employing a well-defined Request Denied Template significantly improves the communication process within the governance, risk management, and compliance (GRC) workflows. It ensures that users are promptly and clearly informed about the status of their requests, thereby minimizing confusion and enabling quicker response to denied requests.

**Technical Impact when configured:**

Upon configuration, the RequestDeniedTemplateId impacts the system by defining the specific messaging template used for denied requests. This customization allows organizations to tailor the denial message content according to their internal policies and communication standards, ensuring that the message content is both relevant and aligned with the organization’s tone and guidelines.

**Examples Scenario:**

- **Scenario 1:** An employee submits a request for access to sensitive financial data. The request is reviewed and denied due to the employee not having the necessary clearance. The configured Request Denied Template ensures the employee receives a detailed and clear denial notification, including the reason for denial and possible next steps or contacts for further inquiries.

**Related Settings:** 

- `Send Workflow Mails`
- `RemoveRolesActivitiesWorkflowTypeId`
- `ReplaceTemplateForWorkflowParameter`

**Best Practices:** configure when establishing clear communication protocols for denied requests, avoid when there is no need for customization or in scenarios where default denial messages are sufficient.