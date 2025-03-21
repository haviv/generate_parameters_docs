# Custom User Group Id For Excluded Users From Usage Logs

**Technical Name:** CustomUserGroupIdForExcludedUsersFromUsageLogs

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to specify a custom user group ID whose members are to be excluded from the usage logs within the Pathlock Cloud GRC platform. It is designed for organizations looking to refine their audit and monitoring capabilities by omitting specific user activities from being recorded, particularly for users who perform high-volume, routine tasks that might otherwise clutter the logs and obscure meaningful data.

**Business Impact:**

The usage of this parameter can significantly impact the organization's ability to manage and analyze audit trails effectively. By excluding certain users from the logs, organizations can streamline their review process, focus on high-priority events, and ensure compliance with data protection regulations by minimizing unnecessary data collection.

**Technical Impact when configured:**

When configured, this parameter ensures that activities performed by users within the specified group are not included in the usage logs. This can reduce the volume of logged data, making it easier to monitor for unusual or unauthorized activities and improving the performance of log analysis tools by reducing the amount of data they need to process.

**Examples Scenario:**

An organization identifies that activities performed by users in the IT department, who frequently test transaction codes as part of their routine duties, are cluttering the usage log with entries that are not relevant for audit purposes. By assigning the IT department users to a custom user group and using this parameter to exclude that group's ID from the usage logs, the organization can keep the focus of log reviews on potential security breaches, unauthorized data access, or transaction misuse by regular users.

**Related Settings:**

- EnableActiveDirectoryActivityModesMatrixCompactMode

**Best Practices:** 

- **Configure when:** You have identified user groups whose activities do not need to be monitored within usage logs, such as IT support staff, developers in testing environments, or automated service accounts performing routine tasks.
  
- **Avoid when:** All user activities are considered relevant for security and compliance purposes, or when the exclusion of any users from the logs might lead to oversight of significant activities.