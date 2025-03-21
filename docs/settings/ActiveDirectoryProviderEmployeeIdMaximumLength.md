**Active Directory Provider Employee Id Maximum Length**

**Technical Name:** ActiveDirectoryProviderEmployeeIdMaximumLength

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to determine the maximum length of the Employee ID retrieved from Active Directory (AD) for a user. If the actual Employee ID exceeds this specified length, it may be truncated or not processed correctly, impacting the integration of user information between AD and the Pathlock Cloud GRC platform.

**Business Impact:**

Ensuring the correct length for the Employee ID is crucial for maintaining accurate user records, automating user provisioning, and de-provisioning processes, and supporting compliance requirements. Misalignment in Employee ID length can lead to issues in user identification, access management discrepancies, and potential security risks.

**Technical Impact when configured:**

Proper configuration ensures seamless synchronization of user identifiers between AD and Pathlock Cloud GRC, thereby facilitating accurate user management, reporting, and audit trails. Incorrect configuration can result in incomplete user data integration or misidentification.

**Examples Scenario:**

An organization has a standard practice of using alphanumeric Employee IDs with a specific length, e.g., up to 15 characters. This parameter must be set accordingly to ensure all Employee IDs are fully captured and accurately reflected in the Pathlock Cloud GRC platform for user management and audit purposes.

**Related Settings:**

- DisableUpdateUsernameInUsersAdministration

**Best Practices:** configure when the standard length of Employee IDs in your Active Directory schema is known and stable. Avoid configuring this parameter without understanding the impact on user information integration and compliance requirements.