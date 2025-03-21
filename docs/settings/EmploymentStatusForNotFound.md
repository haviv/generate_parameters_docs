# Employment Status For Not Found

**Technical Name:** EmploymentStatusForNotFound

**Category:** User Management

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

This parameter is used within the synchronization process of organizational data from secondary data providers (like Active Directory) to manage and mitigate discrepancies in employment status data. It specifies a default employment status to be assigned to users who are found in the secondary provider's data but not in the primary data source. This helps in ensuring that employment statuses are accurately represented across integrated systems.

**Business Impact:**

Improper configuration of this parameter can lead to misclassification of users' employment statuses, affecting access control, compliance reporting, and risk assessment processes. Correct configuration ensures that users' access rights are in alignment with their actual employment status, thereby reducing security risks and maintaining regulatory compliance.

**Technical Impact when configured:**

When configured appropriately, it helps to maintain accurate user status across systems by providing a default fallback status. This assists in the automation of access rights management and compliance processes, reducing manual overhead and the potential for human error.

**Examples Scenario:**

- An employee is terminated in the HR system but this update is not yet reflected in the secondary user data provider. This parameter would determine the default employment status assigned to the user during synchronization, thereby preventing unauthorized access.

**Related Settings:** N/A

**Best Practices:** configure when the organization uses multiple data sources for user management to ensure consistency in user statuses across platforms; avoid when all user data is uniformly managed and updated in real time across all systems.