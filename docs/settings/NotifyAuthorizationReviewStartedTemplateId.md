# Notify Authorization Review Started Template

**Technical Name:** NotifyAuthorizationReviewStartedTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**
This parameter defines the ID of the email template to be used when an authorization review has been initiated within the Pathlock Cloud GRC platform.

**Business Impact:**
Proper configuration ensures that stakeholders are promptly notified when an authorization review process starts, enabling timely participation and decision-making. It supports compliance with internal policies and external regulations by ensuring that all relevant parties are aware of the review process.

**Technical Impact when configured:**
When this parameter is correctly configured, the system automatically sends notifications using the specified email template to relevant stakeholders at the initiation of an authorization review process. This helps in streamlining the workflow and ensuring that the authorization review is conducted efficiently and transparently.

**Examples Scenario:**
In a scenario where an organization has set up a periodic review of user access rights, configuring this parameter ensures that, at the start of each review cycle, a notification is sent out using the pre-defined template. This notification can inform managers or IT admins that a review process has begun, prompting them to log into the Pathlock platform to perform their designated review tasks.

**Related Settings:**
- `RequestApprovedTemplateId`
- `RequestDeniedTemplateId`
- `RequestReceivedTemplateId`

**Best Practices:** 
- **Configure when:** You have a clear process for authorization reviews and stakeholders who need to be notified at the commencement of these reviews.
- **Avoid when:** The notification process for authorization reviews is managed outside the Pathlock Cloud GRC platform or if automated emails are not part of the organization's process workflow.