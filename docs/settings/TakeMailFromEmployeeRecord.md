# Take Mail From Employee Record

**Technical Name:** TakeMailFromEmployeeRecord

**Category:** Configuration

**Default Value:** Not provided

**Impact Level:** Medium

**Description:**

This parameter controls whether the email notifications triggered by workflow actions should use the email address from the employee's record in the system. When enabled, this setting ensures that notifications are sent directly to the email associated with the user's profile in the Pathlock GRC platform.

**Business Impact:**

Enabling this parameter ensures that communication related to workflow actions, like StartStep and EmergencyAccessStep, is accurately directed to the intended recipient's email as recorded in their employee profile. This can significantly enhance the accuracy of notification delivery, ensuring that critical information reaches the appropriate parties in a timely manner. It is particularly beneficial in scenarios where users' primary email addresses may differ from their officially registered email addresses in the GRC system.

**Technical Impact: when configured**

When configured to take the mail from the employee record, the system dynamically fetches the employee's email address from their profile for sending notifications. This affects how notifications for workflow actions, such as emergency access requests or the initiation of a workflow, are handled, ensuring they are sent to the correct email addresses as per the user's profile in the database.

**Examples Scenario:**

A company has initiated an emergency access workflow to grant temporary access rights to a user. With the "Take Mail From Employee Record" parameter enabled, the system looks up the user's profile in the Pathlock GRC platform to locate their official email address. The notification about their emergency access request, along with any approvals or rejections, is then accurately sent to this email, ensuring they're informed in real-time.

**Related Settings:**

- NotifyWorkflowRequestorAndUser: This setting is related, as it controls whether notifications are sent to the workflow requester and the user, which works in conjunction with the TakeMailFromEmployeeRecord parameter to determine the email addresses used for these notifications.

**Applicable Workflows Actions:**

- StartStep
- EmergencyAccessStep

**Best Practices:** 

Configure when accurate and direct communication with the user is essential for workflow actions. Avoid configuring this setting if users’ official email addresses in their profiles are not regularly updated or maintained, as this may lead to misdirected communications.