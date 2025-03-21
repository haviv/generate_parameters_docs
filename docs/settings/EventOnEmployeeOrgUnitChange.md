# Event On Employee Org Unit Change

**Technical Name:** EventOnEmployeeOrgUnitChange

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**
Triggers an event when an employee's organizational unit changes within the Pathlock Cloud GRC platform. It monitors changes in employees' departmental affiliations or positions to ensure timely updates to access rights and compliance statuses.

**Business Impact:**
Ensuring employees' access rights in the system are accurately aligned with their current organizational units is crucial for maintaining operational security and compliance. Misalignment may lead to unauthorized access or inadequate permissions, affecting daily operations and audit readiness.

**Technical Impact when configured:**
Activating this parameter enables the system to automatically trigger workflows or alerts whenever there is a change in an employee's organizational unit. This helps maintain accurate user access levels, supports compliance with internal policies and regulatory requirements, and reduces the administrative burden of manually tracking and validating organizational changes.

**Example Scenario:**
Suppose an employee is promoted from a department with limited access rights to one with broader access needs. If the EventOnEmployeeOrgUnitChange parameter is activated, the system identifies this change and can automatically initiate an update to the employee's access rights, ensuring they have the permissions needed for their new role without delay.

**Related Settings:** 
- AutomaticLockUserCommentTemplate
- AutomaticLockUserNeverLoggedInText

**Best Practices:** 
- **Configure when:** regular changes in employee roles or organizational structures are common within your organization to ensure proper access rights are maintained.
- **Avoid when:** your organization has a very static structure with infrequent changes to employee roles or departments, or where manual updates to employee access rights are preferred for auditing or control reasons.