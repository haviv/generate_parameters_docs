# Event On Employee Position Code Change

**Technical Name:** EventOnEmployeePositionCodeChange

**Category:** Workflow

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:**

The `EventOnEmployeePositionCodeChange` parameter is used within Pathlock's cloud GRC platform to trigger specific workflow actions or notifications when there is a change in an employee's position code. This parameter is crucial in maintaining up-to-date employee data and ensuring that role-based access controls are accurately managed in real-time.

**Business Impact:**

Changes in an employee's position might necessitate updates to their access rights within systems and applications to prevent unauthorized access or insufficient privileges. Timely handling of position code changes helps in mitigating the risk of security breaches and ensuring compliance with organizational policies and regulatory requirements.

**Technical Impact when configured:**

Configuring this parameter ensures that any change in an employee's position code is detected and appropriately managed through workflows that might include updating access rights, notifying managers, or triggering compliance checks. This proactive approach helps in minimizing the time window in which an employee might either have excessive access or insufficient access, thereby enhancing security and efficiency.

**Examples Scenario:**

An employee, previously in a junior developer role, gets promoted to a senior developer position. This change in position comes with different access requirements to resources. By having the `EventOnEmployeePositionCodeChange` parameter configured, the system automatically initiates processes to update the employee's access rights according to the new role, ensuring they have the necessary tools and resources available without delay.

**Related Settings:**

- CommonSettings.Default.EmploymentStatusForNotFound
- ErrorNotificationSubject
- EventDefaultSeverity

**Best Practices:** configure when changes in employee positions are frequent or when precise control over access rights is critical. Avoid configuration if positions within the organization are relatively stable and manual updates are manageable and effective.