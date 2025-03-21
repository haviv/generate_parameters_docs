**Technical Name:** MailTemplateFormating

**Category:** Configuration

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The `MailTemplateFormating` parameter controls the formatting aspects of email notifications generated within the Pathlock Cloud GRC platform, specifically regarding how email templates handle the inclusion and formatting of attached files.

**Business Impact:**

Proper configuration of this parameter ensures that email notifications are delivered with the intended format and attachments. This has direct implications on the efficiency of communication for security, risk management, and compliance workflows, affecting how quickly and effectively team members and stakeholders are informed about relevant issues and updates.

**Technical Impact when configured:**

When configured correctly, the `MailTemplateFormating` parameter ensures that email messages are formatted properly, including the correct handling and inclusion of attachments. This improves the clarity and utility of the emails, ensuring that recipients receive all necessary information in the most accessible manner.

**Examples Scenario:**

A compliance officer needs to send an email notification through the Pathlock platform to various department heads within an organization, attaching a critical compliance report. Proper configuration of the `MailTemplateFormating` ensures that the email is not only sent with the correct information but also includes the report as a properly formatted attachment, facilitating immediate access and review.

**Related Settings:**

- `saveAttachmentNames`: This setting, when enabled, saves the names of attachments for email templates, working in tandem with `MailTemplateFormating` to manage email attachments.

**Best Practices:** 

- **Configure when:** Setting up automated email notifications that require consistent formatting and include attachments, such as reports or documents relevant to GRC activities.
  
- **Avoid when:** If emails sent by the platform do not require attachments or if the default formatting meets the organizational needs without further customization.