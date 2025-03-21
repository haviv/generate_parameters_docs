# Connect Users To Employee By Windows User

**Technical Name:** ConnectUsersToEmployee_ByWindowsUser

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to map and connect users to employees based on their Windows username within the Pathlock Cloud GRC platform. Its primary function is to ensure that user accounts in SAP systems are correctly linked to their corresponding employee records, allowing for accurate identity and access management. 

**Business Impact:**

Implementing this parameter influences the integrity of user data by ensuring that user accounts are consistently and accurately associated with the correct employee records. This is particularly critical for enforcing security policies, auditing, and compliance reporting, as it provides a reliable basis for identity governance.

**Technical Impact when configured:**

When enabled and configured, this parameter facilitates a match between the SAP user's Windows username and the employee's ID, ensuring that user and employee records are correctly linked in the platform. This linkage is crucial for automating user access reviews, provisioning, and de-provisioning processes, and maintaining accurate and auditable records of user access rights across the organization.

**Examples Scenario:**

An organization needs to ensure that when an SAP user is created or updated, their access rights and employee records are aligned. By enabling this parameter, the system automatically links the user account with an employee ID based on their Windows username, streamlining user management processes and enhancing security compliance.

**Related Settings:** 

- ConnectUsersToEmployee_ByEmployeeID

**Best Practices:** configure when the organization uses Windows authentication for SAP users to streamline user and employee record management. Avoid when usernames and employee IDs are managed in a disparate system or do not align with Windows usernames. 