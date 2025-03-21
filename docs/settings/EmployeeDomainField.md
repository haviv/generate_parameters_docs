# Employee Domain Field

**Technical Name:** EmployeeDomainField

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

The Employee Domain Field parameter is a critical setting in the Pathlock Cloud GRC platform that determines how employee data is extracted from an organization's Active Directory. It helps specify the domain field used to identify users, which is fundamental in filtering and managing user data effectively within the system.

**Business Impact:**

Configuring the Employee Domain Field correctly ensures that only relevant employee data is synced and managed within the Pathlock platform, enhancing security and compliance by ensuring data accuracy and preventing unauthorized access. This setting plays a crucial role in automating compliance reporting and managing risks efficiently.

**Technical Impact when configured:**

When configured, the parameter filters the employees based on their active status within the organization, which greatly aids in user management by excluding terminated employees from Pathlock's GRC processes. This leads to a more streamlined and efficient handling of user data.

**Examples Scenario:**

A GRC manager uses the Employee Domain Field to ensure that the Pathlock system only syncs active employees from the Active Directory. This prevents any terminated employee's data from being included in compliance reports or risk assessments, thereby maintaining the integrity and accuracy of these processes.

**Related Settings:**

- FilterOutTerminatedEmployeesFromEmployeesData

**Best Practices:** 

- **Configure when:** you are setting up the Pathlock platform for the first time or when you update your organizational user management policies.
- **Avoid when:** the organization does not use Active Directory for user management or if the setting does not reflect the current organizational structure accurately.