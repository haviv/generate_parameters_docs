**Technical Name: ExistingStringPattern**

**Category: Events**

**Default Value:**

**Impact Level: Medium**

**Description:**

The `ExistingStringPattern` parameter is used to define or recognize patterns within strings that are typically associated with event names or identifiers in the Pathlock Cloud GRC platform. It plays a crucial role in event subscriptions and workflow triggers, allowing for more granular and specific event handling based on string matches.

**Business Impact:**

Configuring the `ExistingStringPattern` correctly can significantly enhance the platform's ability to monitor and respond to specific events critical to security, compliance, and risk management processes. By enabling precise event handling, organizations can automate responses to compliance requirements, security incidents, or risk assessment criteria, thereby reducing manual overhead and improving overall GRC posture.

**Technical Impact when configured:**

Upon configuration, the `ExistingStringPattern` directly influences the event detection and subscription mechanism within the Pathlock Cloud GRC platform. This results in the dynamic triggering of workflows or alerts based on events that match the defined string pattern, ensuring that specific, pattern-matching events are appropriately logged, audited, or actioned according to the platform's configuration.

**Examples Scenario:**

For instance, an organization might set up `ExistingStringPattern` to detect specific events related to unauthorized access attempts or unusual data access patterns. By defining a string pattern that matches these events, the organization can automatically initiate a review workflow or send out notifications whenever such events are detected, thereby streamlining the response to potential security threats.

**Related Settings:**

- `EventSubscriptionTypeYearlyDayOfYear`
- `NotifyAuthorizationReviewStartedTemplateId`

**Best Practices:** 

- **Configure when:** You have specific events or actions within the GRC process that require automated detection and response. This optimizes your monitoring and alerting mechanism for events critical to your organization's security and compliance posture.
- **Avoid when:** Your event identification needs are better served through broader, non-string-based detection methods, or when overly specific string patterns could result in missed or false positive event triggers, potentially overwhelming administrators with unnecessary alerts.