# Template for events summary email message (table)

**Technical Name:** EventsDetailsTableText

**Category:** Reporting

**Default Value:** N/A

**Impact Level:** Medium

**Description:** This parameter is used to configure the formatting and content of the summary email messages sent out by the system, containing details about specific events. It allows for the inclusion of event names, user details, and timestamps in a structured table format within the email body.

**Business Impact:** Proper configuration of this parameter can significantly enhance the clarity and effectiveness of communication around event notifications. It ensures that stakeholders are promptly informed about critical events, aiding in swift decision-making and response.

**Technical Impact when configured:** When configured, this parameter dynamically populates the email template with specific event details such as the event name, full name of the user involved, username, event timestamp, and the host from where the event was triggered. This enhances the informational value of notifications, making them more useful for audit, monitoring, and security response purposes.

**Example Scenario:** Imagine a situation where an employee's job title changes within the organization, potentially affecting their access rights and responsibilities. By configuring this parameter, the system can automatically send an email to relevant authorities, summarizing the event's details including the employee's full name, username, the time of the change, and the system from which the change was made. This helps in keeping a track of significant events without manually sifting through logs or reports.

**Related Settings:** 
- EventOnEmployeeJobCodeChange
- EventOnEmployeeJobTitleChange

**Best Practices:** 
- configure when you require detailed notifications for audit trails or security event monitoring, to ensure all relevant stakeholders are kept informed with comprehensive details.
- avoid when minimal notifications are preferred to prevent information overload.