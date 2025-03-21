# SMS Error Texts

**Technical Name:** SMSErrorTexts

**Category:** User Management

**Default Value:** 

**Impact Level:** Medium

**Description:**

The SMSErrorTexts parameter is used for configuring custom error messages that are sent to users in the event an SMS (Short Message Service) notification fails. This parameter ensures that users are adequately informed about the status of critical notifications related to security, compliance, or operational events.

**Business Impact:**

Properly configuring SMSErrorTexts has a significant impact on operational transparency and user communication within an organization. It enhances the reliability of notification systems by ensuring that users are promptly informed about any issues in SMS delivery, thereby allowing for quick corrective measures. This can be crucial in situations requiring urgent attention, such as security breach alerts or compliance violation notifications.

**Technical Impact when configured:**

When configured, the system uses the defined error texts to communicate SMS delivery failures more effectively to recipients. This improves user experience and trust in the system's ability to deliver critical communications. Additionally, it assists in troubleshooting by providing clearer insights into the nature of SMS delivery issues.

**Examples Scenario:**

1. A compliance officer needs to be instantly notified via SMS of any non-compliant activities detected within the system. If the SMS fails to send due to a network issue, the custom error text configured through the SMSErrorTexts parameter can inform the user about the delivery failure, prompting alternative follow-up actions.

2. During a security breach, an SMS notification is triggered to inform the IT security team. A delivery failure would result in a custom error message being sent, alerting the team to the communication issue and potentially leading to an alternative method of notification.

**Related Settings:** 

- UseOneUserNameForAllRebuildUsernameForCasing

**Best Practices:** configure when all users need to be informed of SMS delivery issues to ensure they are aware of notifications failures and can act accordingly; avoid when SMS delivery failure messages are not necessary for the end user or could cause unnecessary alarm.