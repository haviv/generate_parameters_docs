# System Stopped Body

**Technical Name:** SystemStoppedBody

**Category:** Audit

**Default Value:**

**Impact Level:** High

**Description:**

The `SystemStoppedBody` parameter is used to configure the body content of notification messages sent to users when critical technical issues are detected in the operation of ProfileTailor™ Dynamics. This parameter ensures that detailed information regarding system interruptions or failures is effectively communicated to the relevant stakeholders for immediate action.

**Business Impact:**

Having a well-defined `SystemStoppedBody` message ensures that users are promptly informed about technical issues, enabling quick responses to mitigate any potential risks to business operations, data integrity, and compliance standards. It aids in maintaining transparency and accountability within the organization's GRC framework.

**Technical Impact when configured:**

- **User Notification:** Ensures administrators and users are promptly notified about system issues, preventing delays in addressing critical errors.
- **Clarity and Urgency:** Improves the clarity and perceived urgency of the message, encouraging faster response times to system alerts.
- **Audit Trail:** Serves as part of an audit trail, demonstrating proactive steps taken by the organization to communicate and address system issues.

**Examples Scenario:**

A critical failure occurs within ProfileTailor Dynamics, causing an unexpected system stop. The `SystemStoppedBody` parameter has been configured with a message template that includes instructions for checking the server log and contacting IT support. When the failure is detected, the system automatically sends an email containing the predefined message to all affected users, facilitating a quick response to the situation.

**Related Settings:**

- `ProfileTailorDataClassesDataContext`
- `V_UserAuthorization`

**Best Practices:** configure when, avoid when 

- **Configure when:**
  - You have identified specific users or roles that should be notified in the event of system failures.
  - You need to ensure that messages related to system issues contain all the necessary information for recipients to understand the issue and take appropriate action.
- **Avoid when:**
  - If system failures are not critical to your operations, or if all system issues are handled internally by a specific team who are not reliant on email notifications.