# Event On Employee Job Title Change

**Technical Name:** EventOnEmployeeJobTitleChange

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is designed to monitor and act upon changes in an employee's job title within an organization. It is a part of the Pathlock Cloud GRC platform and helps in maintaining accurate and up-to-date employee records, thereby ensuring that access rights and responsibilities are correctly aligned with the employee's current position.

**Business Impact:**

The Event On Employee Job Title Change parameter plays a crucial role in internal security and compliance processes. By ensuring that an employee's access rights are appropriate for their current job title, organizations can minimize the risk of unauthorized access and potential internal fraud. This parameter supports compliance with various regulatory requirements related to access control and user management.

**Technical Impact when configured:**

Once configured, any change in an employee's job title triggers a workflow or a series of actions defined within the Pathlock platform. These actions can include, but are not limited to, updating access rights, sending notifications to relevant stakeholders, and logging the change for audit purposes. This automated process reduces manual effort and helps in maintaining operational efficiency.

**Examples Scenario:**

- **Promotion:** When an employee is promoted, the system automatically updates their access rights to include new permissions required for the higher position.
- **Role Change:** If an employee's role within the organization changes, the system adjusts their access rights to reflect their new responsibilities, removing access that is no longer relevant.
- **Termination of Employment:** Upon changing an employee's job title to a status that reflects termination, the system can initiate a process to revoke access, ensuring that former employees no longer have access to the system.

**Related Settings:**

- `IsActive`: Determines if the event monitoring is active.
- `Enable`: Enables the specific event type for monitoring.
- `Visible`: Controls the visibility of the event type within the platform interface.

**Best Practices:** 

- **Configure when:** Immediate oversight of job title changes is crucial for maintaining security and compliance standards.
- **Avoid when:** If job titles within the organization are frequently revised without substantial changes to role or access requirements, constant monitoring may generate excessive notifications and workflow actions, potentially leading to alert fatigue.