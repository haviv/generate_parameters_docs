# Events Summary Mail - Subject

**Technical Name:** DailyEmailSubject

**Category:** Reporting

**Default Value:**

**Impact Level:** High

**Description:**

The `DailyEmailSubject` parameter controls the subject line of daily summary emails sent out by the Pathlock GRC platform. This parameter is crucial for users to quickly identify the content and importance of the email among other messages in their inbox.

**Business Impact:**

Having a clear and descriptive email subject ensures that critical notifications are promptly noticed and acted upon by the recipients. It enhances user engagement with the platform's reporting features and ensures that governance, risk, and compliance (GRC) events do not go unnoticed.

**Technical Impact when configured:**

Configuring this parameter allows organizations to customize the subject line based on the content of the email, the target audience, or the priority of the messages being sent. A well-configured subject line can increase the visibility of the emails, leading to quicker response times to compliance or security issues highlighted in the events summary.

**Example Scenario:**

- **Scenario:** A company wants to ensure that its IT team immediately notices reports containing critical security breaches.
- **Configuration:** The `DailyEmailSubject` is set to include tags such as [Critical] or [Security Alert] for emails that report events of high severity.
- **Outcome:** IT team members are more likely to open and address these emails promptly, reducing the potential impact on the organization’s IT infrastructure.

**Related Settings:**

- DailyEmailFooter

**Best Practices:** 

- **Configure when:** you need to ensure that emails from the Pathlock GRC platform stand out in the recipients' inboxes, especially for critical alerts or compliance issues.
- **Avoid when:** you prefer to use a generic, uniform subject line for all communications from the platform. However, this is not recommended due to the potential for high-impact messages to be overlooked.