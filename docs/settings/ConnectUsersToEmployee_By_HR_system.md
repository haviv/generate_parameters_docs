# Connect Users To Employee By HR system

**Technical Name:** ConnectUsersToEmployee_By_HR_system

**Category:** User Management

**Default Value:** Not Specified

**Impact Level:** High

**Description:**

This parameter is used to control the automation of user to employee mappings within the organization, leveraging data from an HR system. When enabled, the system automatically associates user accounts with their corresponding employee records based on the username provided by the HR system. This ensures that user accounts in the system are correctly linked to the right employee data, facilitating accurate access rights and permissions management across the organization's digital landscape.

**Business Impact:**

Enabling this parameter streamlines the process of user account management, reduces the risk of human errors during manual entries, and ensures compliance with regulatory requirements regarding access controls and audit trails. It enhances operational efficiency by automating a critical aspect of user access governance and minimizes the risk of security breaches due to mismanagement of user identities.

**Technical Impact when configured:**

- Automatically populates the `EmployeeId` field for user data objects when a corresponding entry is found in the HR system mapping.
- Reduces manual overhead for system administrators by automating the synchronization process between user accounts and employee records.
- Enhances the integrity and reliability of user to employee mappings, which is critical for access management and compliance reporting.

**Examples Scenario:**

An organization integrates its HR system with the Pathlock Cloud GRC platform. When a new employee is added to the HR system, their user account is automatically created in the GRC platform. With the `ConnectUsersToEmployee_By_HR_system` parameter enabled, the platform uses the mapping from the HR system to connect the new user account with the right employee record automatically. This ensures the employee has the appropriate access rights from day one, based on their role, without manual intervention.

**Related Settings:** 

- `ReadUsersToEmployeesMapping()`: Function to retrieve mapping details between users and employees.

**Best Practices:** 

- **Configure when:** You have a reliable, up-to-date HR system that can serve as the source of truth for employee data.
- **Avoid when:** Your organization does not have an HR system with up-to-date user information, or if manual control over user to employee mappings is required for business or regulatory reasons.