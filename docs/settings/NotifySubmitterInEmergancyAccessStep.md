# Notify Submitter In Emergency Access Step

**Technical Name:** NotifySubmitterInEmergancyAccessStep

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls whether the submitter is notified in the step of emergency access within the Pathlock Cloud GRC platform's workflow.

**Business Impact:**

Enabling notifications for submitters during the emergency access step ensures timely communication and oversight. It is critical for maintaining the integrity and security of access management procedures, particularly in sensitive or high-risk contexts.

**Technical Impact when configured:**

When enabled, the system will automatically send notifications to the submitter in the workflow where emergency access is granted. This ensures that the submitter is kept informed about the status of their access request, including any escalations or approvals that occur as part of emergency procedures.

**Examples Scenario:**

- In a scenario where immediate access is required to address a critical issue, enabling this parameter ensures that the individual who requested emergency access is informed once the access is granted, enhancing response times and accountability within critical operations.

**Related Settings:**

- ChangeDocumentsShowChangeTypeColumn

**Best Practices:** 

- Configure when: Immediate transparency and communication are essential for emergency access requests, especially in environments where access rights are tightly controlled or monitored for compliance and security reasons.
  
- Avoid when: If notifications could potentially overwhelm or confuse the process, or in very low-security environments where notification is not necessary for every action taken. However, given the security implications, such scenarios are rare.