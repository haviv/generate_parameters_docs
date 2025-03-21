# Send Workflow Mails

**Technical Name:** SendWorkflowMails

**Category:** Workflow

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

The Send Workflow Mails parameter controls whether emails related to workflow actions, such as notifications for workflow steps or status updates, are automatically dispatched to relevant parties.

**Business Impact:**

Enabling this parameter ensures timely notifications to workflow participants, thereby facilitating quicker decision-making and action. It supports accountability and transparency within organizational processes.

**Technical Impact when configured:**

When enabled and configured, this parameter triggers the automated sending of emails through the defined mail sender utility, utilizing provided recipient details, message content, mail priority, and file attachments. This action supports workflow steps by distributing necessary information and documents directly related to workflow instances.

**Examples Scenario:**

Scenario: A workflow is initiated for a risk assessment process. Upon reaching a specific step that requires managerial approval, an email notification is automatically sent to the manager(s) with details of the request and any relevant attachments. The manager can quickly provide the necessary approval or feedback directly through the email or linked system, ensuring the workflow continues efficiently without unnecessary delays.

**Related Settings:** 

- ShowPortalLinkOnRequestSubmittedPage: Displaying a portal link on the request submission confirmation page can complement the email notifications by providing direct access to the workflow details for further action or review.

**Best Practices:** 

- **Configure when:** Immediate or automated notifications are necessary for efficient workflow movement, especially in processes where time-sensitive actions are critical.
  
- **Avoid when:** The workflow process is simple or involves steps where manual intervention is preferred for sending customized communications or in scenarios where notification overload is a concern.