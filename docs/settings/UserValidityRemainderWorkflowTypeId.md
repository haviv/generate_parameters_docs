**Technical Name:** UserValidityRemainderWorkflowTypeId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The `UserValidityRemainderWorkflowTypeId` parameter is designed to manage and automate the notifications for user account validity reminders within the Pathlock Cloud GRC platform. It ensures that administrators are promptly alerted to users whose account validity is approaching expiry, allowing for timely review and action to maintain system security and compliance.

**Business Impact:**

Effectively managing user account validity is crucial for maintaining the integrity and security of the GRC system. By automating reminders, organizations can ensure that no user account with potentially elevated permissions remains active beyond its intended period, reducing the risk of unauthorized access and potential compliance issues.

**Technical Impact when configured:**

When this parameter is configured, the system will automatically trigger workflow actions based on the specified Workflow Type ID. These actions can include sending notifications to administrators or initiating a review process for user accounts nearing the end of their validity period.

**Examples Scenario:**

A company has set the UserValidityRemainderWorkflowTypeId to trigger reminders 30 days before a user's account is set to expire. Two weeks prior to expiry, the responsible manager has not yet extended the account. The workflow triggers an escalated reminder to both the manager and the IT security team, ensuring that the user's access is reviewed and actioned upon promptly.

**Related Settings:**

- ReadUsageFromSM20Enable
- ReadUsageFromSM20TcodeFilter

**Applicable Workflows Actions:** 

**Best Practices:** 

- **configure when**: It is critical to have oversight and proactive management over user account validities, especially in environments subject to stringent security and compliance standards.
- **avoid when**: If user validity is managed through another system or process which makes this parameter redundant or could conflict with existing workflows.