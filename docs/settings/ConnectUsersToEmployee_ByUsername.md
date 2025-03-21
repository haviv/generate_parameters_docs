# Connect Users To Employee By Username

**Technical Name:** ConnectUsersToEmployee_ByUsername

**Category:** User Management

**Default Value:** None provided in the provided references.

**Impact Level:** Medium

**Description:** This setting determines whether users are automatically connected to employee records based on matching usernames. When enabled, the system attempts to link each user account in Pathlock Cloud GRC to an employee entity if the usernames between the user account and the employee record are identical.

**Business Impact:** Enabling this parameter streamlines user management processes by automating the association between user accounts and employee records. It ensures that user data is consistently managed and reduces the administrative overhead involved in manually linking users to employee entities. This can be particularly beneficial in large organizations with frequent personnel changes, as it ensures access rights and responsibilities are accurately reflected in the GRC platform.

**Technical Impact when configured:** When configured, the system will use the username as a key to automatically connect users to their corresponding employee records in the database. This facilitates more efficient user account management, auditing, and compliance processes by ensuring that all user actions can be accurately attributed to the correct employee.

**Examples Scenario:** A company uses Pathlock Cloud GRC to manage access and permissions for its SAP system. Upon hiring a new employee, an account is created in the company's Active Directory with a username that matches their employee record in the HR system. With Connect Users To Employee By Username enabled, Pathlock automatically links the new user account to the employee record, streamlining the process of granting appropriate access rights and permissions based on the employee's role.

**Related Settings:** 
- ConnectUsersToEmployee_ByWindowsUser

**Best Practices:** Configure this parameter in environments where username conventions are consistently applied across user accounts and employee records. Avoid using this setting in environments where multiple systems have inconsistent naming conventions that could result in erroneous associations.