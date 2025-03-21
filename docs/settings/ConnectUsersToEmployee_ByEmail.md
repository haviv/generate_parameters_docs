# Connect Users To Employee By Email

**Technical Name:** ConnectUsersToEmployee_ByEmail

**Category:** User Management

**Default Value:** N/A

**Impact Level:** High

**Description:**

The parameter "ConnectUsersToEmployee_ByEmail" is utilized within the Pathlock Cloud GRC platform for mapping system users to employees based on email addresses. This is particularly relevant in environments where the employee ID is not available or when the mapping needs to be derived from another system of record, such as an HR system. This is part of the platform's broader capability to manage and synchronize user identities across various systems to ensure compliance and streamline user access management.

**Business Impact:**

Ensuring users are correctly mapped to their corresponding employee records is critical for maintaining accurate access controls and compliance reporting. Misalignment between user accounts and employee records can lead to inappropriate access rights, potential security breaches, and non-compliance with regulatory requirements. Utilizing this parameter aids in mitigating these risks by improving the accuracy of user-employee mappings.

**Technical Impact when configured:**

When enabled, the system will attempt to map system user accounts to employee records using email addresses as the key identifier. This is particularly useful when direct employee ID to user account mappings are incomplete or unavailable. If a match is found based on email, the corresponding user and employee records are linked, enabling more accurate access management and compliance reporting.

**Examples Scenario:**

For instance, when a new user is created in an external system, and there is no immediate employee ID available to map the user to an employee in the Pathlock platform, this parameter allows for the user to be automatically mapped based on a matching email address present in both the user’s account information and the employee’s HR record.

**Related Settings:**

- ReadEmployeeToUserMappingForAllSystemsFromHRSystem

**Best Practices:** configure when the employee ID is not consistent across systems or is not available, avoid when more accurate methods of user-employee mapping are available and can be utilized without relying on email addresses alone.