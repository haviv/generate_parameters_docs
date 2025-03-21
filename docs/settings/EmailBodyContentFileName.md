# Real Time Mail - Email body content

**Technical Name:** EmailBodyContentFileName

**Category:** Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

This parameter specifies the file name for the email body content used in real-time mail notifications. It allows for customizing the content of email messages sent by the Pathlock Cloud GRC platform to notify users about various security, risk, and compliance events.

**Business Impact:**

Customizing the email body content can significantly impact how users perceive and react to notifications. By tailoring the message, organizations can ensure that critical information is conveyed clearly and effectively, potentially increasing the speed and quality of responses to compliance, security, and risk issues.

**Technical Impact when configured:**

When this parameter is configured, the Pathlock Cloud GRC platform uses the specified file as the template for the body of email notifications. This allows administrators to design and implement customized email content that aligns with the organization's communication standards and meets specific compliance and information-sharing requirements.

**Examples Scenario:**

An organization needs to notify its user base about detected high-risk activities that require immediate attention. By customizing the EmailBodyContentFileName, the GRC team can ensure that the email notification includes organization-specific guidance on how to review and address these high-risk activities, thereby facilitating a quicker and more informed response from the recipients.

**Related Settings:** 

- `DisplayWorkflowFormViewer`
- `DisplayHighRiskActivitiesOnRolesAuthorizationReview`

**Best Practices:** 

- **Configure when:** There is a need to tailor the communication of GRC related notifications to better match organizational language, tone, or specific call-to-action requirements.
- **Avoid when:** Default notification templates meet the organization's communication and compliance requirements without further customization.