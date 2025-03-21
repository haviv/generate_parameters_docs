# Mail Listener Check Emails Every XMinutes

**Technical Name:** MailListener_CheckEmailsEveryXMinutes

**Category:** Workflow Configuration

**Default Value:** 

**Impact Level:** Medium

**Description:**

The `MailListener_CheckEmailsEveryXMinutes` parameter is designed to configure the frequency at which the Mail Listener service checks for new emails. This is crucial for ensuring timely processing of incoming communications related to governance, risk, and compliance (GRC) activities within the Pathlock platform.

**Business Impact:**

Adjusting the value of this parameter affects how quickly the system responds to new email-based notifications or requirements. A shorter interval might be necessary for high-priority areas needing immediate action, while a longer interval could suffice for less critical areas, optimizing system resource utilization.

**Technical Impact when configured:**

Proper configuration ensures efficient email processing, preventing delays in workflow executions or notifications. Misconfigurations could lead to either unnecessary load on email servers (if set too low) or delays in processing critical compliance and security-related tasks (if set too high).

**Examples Scenario:**

A compliance department requires immediate notification of any compliance breaches reported via email. Setting the `MailListener_CheckEmailsEveryXMinutes` to a lower value ensures prompt retrieval and processing of these emails, enabling swift action.

**Related Settings:** 

- EmployeesNotSavedHeader
- EmployeesNotSavedBody

**Best Practices:** configure when high responsiveness is required for GRC-related email communications; avoid when the system is under heavy load or email notifications are non-critical.