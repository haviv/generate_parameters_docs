**Event Subscription Type Quarterly Day Of Month**

**Technical Name:** EventSubscriptionTypeQueterlyDayOfMonth

**Category:** Workflow

**Default Value:** Not provided in the code references.

**Impact Level:** Medium

**Description:**

This parameter determines on which day of the month the system should trigger quarterly event subscription workflows. It is crucial for timely sending of workflow reminders and aligning with organizational compliance practices on a quarterly basis.

**Business Impact:**

The correct configuration of this parameter ensures that workflow reminders and notifications related to various compliance, risk, and audit events are dispatched in a timely and consistent manner every quarter. This can significantly affect the organization's ability to stay compliant with internal and external policies and regulations.

**Technical Impact when configured:**

When configured correctly, it enables the Pathlock GRC platform to automate the process of sending out notifications and reminders for events subscribed to on a quarterly basis, aligned with the specified day of the month. Misconfiguration can lead to delays or failure in sending these crucial reminders, affecting compliance and audit readiness.

**Example Scenario:**

An organization seeks to send out reminders for a quarterly review of access rights within its IT systems. By setting the EventSubscriptionTypeQueterlyDayOfMonth to the appropriate day, such as the 15th of the first month in each quarter, it ensures that the stakeholders receive these reminders in a timely manner, allowing sufficient time for review and any required action.

**Related Settings:**

- `SendWorkflowReminder`
- `CustomerSystemWideSystemId`
- `SendWorkflowReminderOnDays`

**Best Practices:** Configure this parameter at the beginning of your deployment to align with your organizational quarterly compliance cycles. Avoid setting this parameter too close to the end of a month to ensure there is sufficient lead time for action to be taken before the quarter ends.