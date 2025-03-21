# Notify Authorization Review Will Start Template

**Technical Name:** NotifyAuthorizationReviewWillStartTemplateId

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

The NotifyAuthorizationReviewWillStartTemplateId parameter is used to define the template ID for sending notifications that an authorization review process will soon commence. This setting is crucial in informing relevant parties about the upcoming access review activities, ensuring participation and compliance with internal security policies and regulatory requirements.

**Business Impact:**

Implementing this parameter streamlines the communication process for authorization reviews, enhancing the organization's ability to maintain a robust security posture. Timely notifications ensure that all stakeholders are aware of and can prepare for their roles in the review process, ultimately supporting compliance efforts and minimizing risks associated with unauthorized access.

**Technical Impact when configured:**

When configured, this parameter triggers the system to use the specified template ID for sending out notices about upcoming authorization reviews. This customization allows for tailored messages that align with the organization's procedures and language, improving the clarity and effectiveness of communications.

**Examples Scenario:**

1. **Pre-Audit Preparation:** Ahead of a planned internal or external audit, a financial services company configures the NotifyAuthorizationReviewWillStartTemplateId to send out detailed notifications to department heads about the review of access rights. This ensures that each department is adequately prepared, supporting successful audit outcomes.

**Related Settings:**

- `RequestApprovedTemplateId`
- `RequestDeniedTemplateId`
- `RequestRecievedTemplateId`

**Best Practices:** configure when the organization is about to undertake a comprehensive review of user access and permissions to ensure all stakeholders are informed in advance. Avoid when the organization does not have a structured process for authorization review, or the communication needs are better served through other channels.