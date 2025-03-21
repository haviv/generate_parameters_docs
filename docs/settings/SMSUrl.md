**Technical Name: SMSUrl**

**Category: Configuration**

**Default Value:**

**Impact Level: Medium**

**Description:**

The SMSUrl parameter specifies the URL endpoint used by the Pathlock Cloud GRC platform for sending SMS notifications. This setting is crucial for the SMS notification feature within the system, allowing for immediate communication with users for security, risk management, and compliance notifications.

**Business Impact:**

Proper configuration of the SMSUrl ensures timely delivery of SMS notifications to users, which can include alerts about security breaches, compliance issues, or risk assessments. This immediate communication enhances the organization's ability to respond quickly to critical events, thereby reducing potential damage or compliance failures.

**Technical Impact when configured:**

When the SMSUrl is correctly configured, the system can successfully connect to the specified SMS gateway or service provider for sending text messages. This ensures that notifications are sent out without delays, contributing to effective risk communication and management processes.

**Examples Scenario:**

An organization configures the SMSUrl to use their preferred SMS gateway. When a security issue is detected, such as an unauthorized access attempt, the system immediately sends an SMS alert to the relevant security managers, allowing for a swift response to mitigate the issue.

**Related Settings:**

- SMSPass

**Best Practices:** 

- **Configure when:** Setting up the SMS notification feature during initial system configuration or when changing SMS service providers. 
- **Avoid when:** The organization does not use SMS notifications as part of its communication strategy.