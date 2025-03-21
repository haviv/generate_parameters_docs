# Workflow Reminder Authorization Certification Format

**Technical Name:** WorkflowReminderAuthoirizationCertificationFormat

**Category:** Workflow

**Default Value:** Not provided in the provided references.

**Impact Level:** Medium

**Description:** This parameter is used to define the format of the reminders for authorization certification sent in the context of Pathlock's workflow actions, specifically when sending reminders for pending approvals or certifications within the workflow process.

**Business Impact:** Proper configuration of this parameter ensures timely and effective reminders to approvers or certifiers, which in turn helps in maintaining continuous compliance and efficient handling of governance, risk, and compliance (GRC) processes within an organization.

**Technical Impact when configured:** Determines the structure and content of the emails or notifications sent as reminders within the workflow. Correct configuration can lead to faster response times from workflow participants, thus streamlining the approval processes and reducing the risk of delays in compliance-relevant decisions.

**Example Scenario:** In a scenario where an organization requires managers or compliance officers to approve certain risk assessments or compliance checks, configuring this parameter with a comprehensive and clear format can alert and remind the approvers effectively about their pending tasks, ensuring these tasks are completed in a timely manner.

**Related Settings:** 
- SendWorkflowReminderEvery (Determines the frequency of reminder emails)
- ShowEventDetailsInWorkflow (Affects if event details are shown in the workflow reminders)

**Best Practices:** 
- **Configure when:** You need to ensure that the workflow participants are reminded in a timely and effective manner about their pending actions.
- **Avoid when:** Not applicable, as reminders are critical to workflow efficiency and compliance adherence. However, the configuration should be mindful not to overwhelm participants with too frequent or irrelevant reminders.