# SMS User

**Technical Name:** SMSUser

**Category:** User Management

**Default Value:** None

**Impact Level:** Medium

**Description:** The SMSUser parameter is used within the Pathlock Cloud GRC platform to define user credentials for sending SMS notifications. It is a critical part of the SMS notification system, ensuring secure and precise delivery of messages to intended recipients.

**Business Impact:** Proper configuration of the SMSUser parameter directly impacts the organization's ability to reliably communicate important security, risk, and compliance information via SMS. It ensures timely alerts and notifications to the right individuals, supporting prompt action and decision-making.

**Technical Impact when configured:** Enables the SMS sending service to authenticate against the SMS provider, ensuring that messages are sent securely and reliably. Misconfiguration can lead to failure in sending notifications, potentially causing delays in communication during critical incidents.

**Examples Scenario:** A security breach is detected, and immediate notification is necessary for the security team. The system uses the SMSUser settings to authenticate and send SMS alerts to the team member's mobile numbers, ensuring rapid awareness and response to the incident.

**Related Settings:** `HttpUser`

**Best Practices:** 

- **Configure when:** You have obtained valid SMS service credentials and need to set up SMS notifications for security, risk, and compliance alerts.
- **Avoid when:** You do not have secure, validated credentials or if your organization does not utilize SMS for notifications, to prevent security risks related to misconfiguration or unauthorized access.