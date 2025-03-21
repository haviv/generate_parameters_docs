# Run SoD Check

**Technical Name:** RunSoDCheck

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The 'Run SoD Check' parameter is responsible for initiating a Segregation of Duties (SoD) check within the Pathlock Cloud GRC platform. This check is crucial for identifying and preventing conflicts of interest within an organization's operations by ensuring that no single individual has control over multiple conflicting tasks.

**Business Impact:**

Enabling the 'Run SoD Check' functionality can significantly enhance an organization's security posture. By preventing the assignment of conflicting roles or permissions to a single user, it helps in mitigating the risk of fraud, errors, and unauthorized access, thereby protecting sensitive information and maintaining compliance with regulatory requirements.

**Technical Impact when configured:**

When configured, the system will automatically perform checks for segregation of duties conflicts as part of its authorization loading process. This ensures ongoing compliance and security by vetting user roles and permissions against predefined rules and criteria to identify potential conflicts.

**Examples Scenario:**

- **Finance Department:** To prevent financial fraud, the system can ensure that the roles responsible for creating vendors and the roles responsible for approving payments are not held by the same user.
- **IT Department:** To secure the IT infrastructure, it can prevent a single user from both creating access rights and approving those rights.

**Related Settings:**

- RolesSplitterRolesChildRolePattern
- RequestApprovedTemplateId
- RequestDeniedTemplateId

**Best Practices:** configure when setting up roles and permissions to ensure that SoD checks are part of the initial security and compliance strategy. Avoid when roles are too granular, leading to operational inefficiency without significantly enhancing security or compliance posture.