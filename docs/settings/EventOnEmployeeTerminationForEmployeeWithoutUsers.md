# Event On Employee Termination For Employee Without Users

**Technical Name:** EventOnEmployeeTerminationForEmployeeWithoutUsers

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether an event is saved in the system for employees who are terminated but do not have corresponding user accounts in Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature ensures that terminations of all employees, including those without user accounts, are recorded and tracked. This enhances audit trails and helps in compliance with internal and regulatory requirements regarding employee management and data integrity.

**Technical Impact when configured:**

When enabled, this parameter triggers the system to log an event for every employee termination, even for those who have no user account. This expands the coverage of audit and compliance checks to include all employees, not just those with direct system access.

**Examples Scenario:**

An organization requires a comprehensive log of all employee terminations, including contractors and temporary staff who may not have been granted access to the organization's systems. By enabling this parameter, HR and compliance teams can ensure no employee termination goes unrecorded, thereby enhancing the organization's risk management and compliance posture.

**Best Practices:** 

- Configure when: Complete oversight and documentation of all employee terminations are required for compliance or internal audit purposes.
  
- Avoid when: The organization prefers to limit termination events logging to users with system accounts to reduce data volume or when such tracking is unnecessary for compliance or audit needs.