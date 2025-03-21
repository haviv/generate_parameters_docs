# ISHR ead Employee Number From VMA

**Technical Name:** ISHReadEmployeeNumberFromVMA

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is responsible for enabling the reading of employee numbers from the Virtual Master Address (VMA) within the Pathlock Cloud GRC platform. This functionality is pivotal for ensuring that employee information is consistent and up-to-date across different business systems that are integrated with the Pathlock platform.

**Business Impact:**

Enabling this parameter ensures that employee data, especially employee numbers, are synchronized across systems. This has a significant impact on processes such as access rights assignments, compliance reporting, and audit trails, contributing to more streamlined operations and enhanced security posture.

**Technical Impact when configured:**

When configured, this parameter allows the Pathlock Cloud GRC platform to automatically fetch and update employee numbers from the VMA, reducing manual data entry errors and enhancing data integrity. This automation also facilitates better management of user identities and access controls within integrated systems.

**Examples Scenario:**

A company uses the Pathlock Cloud GRC platform to manage access controls and compliance across its SAP environment. By enabling `ISHReadEmployeeNumberFromVMA`, the company ensures that employee numbers fetched from their HR system are automatically updated in Pathlock. This ensures that when employees are transferred or their details change, their new employee number is correctly reflected in the access controls and compliance reports, preventing unauthorized access and ensuring accurate reporting.

**Related Settings:**

- ImportManagersDisableApprovalGroupCleanup

**Best Practices:** configure when integrating Pathlock Cloud GRC with HR systems or other sources of employee data to maintain data accuracy and integrity. Avoid when there is no clear source of truth for employee numbers or when data is managed manually with no need for synchronization.