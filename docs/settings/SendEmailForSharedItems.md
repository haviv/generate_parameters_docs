# Send Email For Shared Items

**Technical Name:** SendEmailForSharedItems

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The **Send Email For Shared Items** parameter controls whether emails are dispatched to notify users when items are shared with them within the Pathlock Cloud GRC platform. This functionality is essential for ensuring prompt communication regarding access or information shared within the platform, which enhances collaboration and oversight among users.

**Business Impact:**

Activating this feature can significantly improve the workflow efficiency by ensuring that users are immediately informed about shared resources. This immediate notification speeds up processes that require attention or action, facilitating a more responsive and dynamic working environment. On the other hand, deactivating this feature might delay the awareness of shared items, potentially hindering timely responses to shared compliance, risk, or audit information.

**Technical Impact when configured:**

When configured, this option engages the email system within Pathlock Cloud GRC to send out notifications automatically upon the sharing of any item. This presupposes that the email template and system are correctly set up and operational, relying on the `SharedItemsEmailTemplateId` for the formatting and content of the email messages sent.

**Examples Scenario:**

A compliance officer shares a compliance report with several department heads. Upon sharing, each department head receives an immediate email notification, allowing them to review the shared report promptly. This immediate notification ensures that all relevant parties are kept up-to-date with compliance statuses, fostering a proactive compliance culture.

**Related Settings:**

- SharedItemsEmailTemplateId

**Best Practices:** 

- **Configure when:** Immediate notification is essential for your organizational workflows, especially in environments where timely access to shared information is critical for decision-making processes.
  
- **Avoid when:** Your organization prefers to minimize email notifications to reduce clutter or when another established process is in place for notifying users about shared items.