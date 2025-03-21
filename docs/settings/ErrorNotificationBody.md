# Error Notification Body

**Technical Name:** ErrorNotificationBody

**Category:** Configuration

**Default Value:**

**Impact Level:** High

**Description:**

The Error Notification Body parameter is used to configure the content of error notification emails sent by the system. It defines the body text of emails dispatched to administrators when an error occurs within the Pathlock Cloud GRC platform. This parameter allows for dynamic insertion of details such as the administrator's username and the current customer's name, ensuring personalized and informative error notifications.

**Business Impact:**

Proper configuration of this parameter ensures that system administrators are promptly and accurately informed about errors, allowing for quick response and resolution. This can significantly reduce downtime and improve system reliability, directly impacting business operations by maintaining the integrity and continuity of GRC processes.

**Technical Impact when configured:**

When configured, this parameter activates and personalizes error notification emails, enhancing the administration team's ability to monitor and troubleshoot the system effectively. It leverages the platform's notification services to send detailed emails, potentially including attachments such as log files, to provide comprehensive error context. This facilitates a more informed and efficient troubleshooting process.

**Examples Scenario:**

- **Scenario:** An unexpected error occurs in the Pathlock Cloud GRC platform that prevents users from accessing critical compliance reports. The Error Notification Body is configured to include specific error details and instructions for initial troubleshooting steps.

- **Outcome:** An email is sent automatically to the system administrators, containing the error details and suggesting immediate actions. The administrators investigate the issue promptly, minimizing the report access downtime and maintaining compliance processes.

**Related Settings:** 

- `EnableLockUserLocalyForNonActiveUser`
- `EnableMinimumPasswordAge`

**Best Practices:** 

- **Configure when:** It's crucial to keep system administrators informed about system errors, ensuring they have enough information for initial diagnosis and actions.
  
- **Avoid when:** If the system is in a development environment where frequent errors are expected and monitored through different channels.