# Sms Sender Provider

**Technical Name:** SmsSenderProvider

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

The `SmsSenderProvider` parameter specifies the service provider used for sending SMS notifications. It is a critical component within the Pathlock Cloud GRC platform, enabling the system to dispatch SMS messages as part of various workflows, notably during user creation and security alerts. 

**Business Impact:**

Choosing the right SMS Sender Provider impacts the reliability and speed of notification delivery to users. It ensures critical information related to security, compliance, and risk management is promptly delivered, facilitating timely responses to potential threats or necessary actions.

**Technical Impact when configured:**

When properly configured, the `SmsSenderProvider` facilitates seamless communication between the Pathlock Cloud GRC platform and the chosen SMS gateway. This configuration directly influences the success rate and latency of message delivery, affecting user experience and operational efficiency.

**Examples Scenario:**

- **User Onboarding:** When a new user is created in the system, an SMS notification is sent to confirm the account creation and provide initial access instructions.
  
**Related Settings:**

- `HttpUser`
- `HttpPassword`

**Best Practices:** 

- **Configure when:** Setting up the platform for the first time or when changing the SMS service provider to ensure uninterrupted and reliable SMS notification services.
- **Avoid when:** Lack of information about the service provider's API requirements and credentials could lead to misconfiguration and failure in sending SMS notifications. Ensure all provider-specific parameters are correctly set.