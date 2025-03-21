# Request Approved Template

**Technical Name:** RequestApprovedTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The RequestApprovedTemplateId parameter specifies the template identifier used for generating emails upon the successful approval of workflow requests within the Pathlock Cloud GRC platform. This parameter plays a crucial role in the customization and automation of communication related to the workflow approvals process.

**Business Impact:**

Proper configuration of the RequestApprovedTemplateId ensures that stakeholders and relevant users are adequately informed about the status of their requests, promoting transparency and efficiency in the management of security, risk, and compliance workflows.

**Technical Impact when configured:**

When configured, the RequestApprovedTemplateId triggers the use of a specific email template for notifications sent to users following the approval of their requests. This customization enhances the user experience by providing clear, relevant, and timely communication regarding the outcomes of workflow processes.

**Examples Scenario:**

- An IT administrator requests access to sensitive financial records. Upon approval of this request, an email generated using the configured RequestApprovedTemplateId is sent to the administrator, detailing the approval and next steps.

**Related Settings:**

- RemediationWorkflowsSOD
- RemoveRolesActivitiesWorkflowTypeId

**Best Practices:** 

- **Configure when:** Setting up workflow notifications for approvals to ensure that users receive consistent and informative updates regarding the status of their requests.
- **Avoid when:** There is no need for custom notifications or when default communication settings suffice.