# Read Active Directory Employee

**Technical Name:** ReadActiveDirectoryEmployeeId

**Category:** User Management

**Default Value:**

**Impact Level:** High

**Description:**

The `ReadActiveDirectoryEmployeeId` parameter is designed to manage how employee identifiers are read and interpreted from Active Directory within the Pathlock Cloud GRC platform. It prioritizes the use of the EmployeeId attribute and defaults to the SamAccountName if EmployeeId is not provided.

**Business Impact:**

Accurate identification and management of Active Directory user accounts are crucial for maintaining enterprise security and compliance. Misidentification or duplication might result in incorrect access rights assignments, potentially leading to unauthorized access or breaches.

**Technical Impact when configured:**

Upon configuration, the system will either use the EmployeeId as the primary identifier for users or fallback to SamAccountName if EmployeeId is not available. This ensures a consistent and reliable method for identifying user accounts across an organization's digital landscape.

**Examples Scenario:**

- In an organization where Employee IDs are the primary identifiers but not all accounts in Active Directory have this attribute set, the system will automatically use SamAccountName, ensuring no user is left unidentified.
- During an audit, ensuring each account can be precisely matched to an employee by their unique identifier aids in demonstrating compliance with access control policies and regulations.

**Related Settings:**

- **LastLogon:** Indicates the last time a user logged on. Relevant for tracking inactive accounts.
- **LastChange:** Reflects the last change made to the user account. Used for monitoring and auditing changes.
- **IncorrectLogons:** Tracks the number of failed login attempts. Important for identifying potential unauthorized access attempts.

**Best Practices:** 

- **Configure when:** EmployeeId is uniformly assigned to all users within the Active Directory. It ensures the most accurate user account identification and management.
- **Avoid when:** EmployeeId attributes are not consistently available or populated. In such cases, relying on SamAccountName prevents identification issues.