# Sap Users System

**Technical Name:** SapUsersSystemId

**Category:** User Management

**Default Value:** null

**Impact Level:** High

**Description:** The `SapUsersSystemId` parameter uniquely identifies the SAP system associated with user data and activities within the Pathlock Cloud GRC platform. This setting is essential for correctly mapping SAP user information and enforcing governance, risk management, and compliance (GRC) policies.

**Business Impact:** Proper configuration of the `SapUsersSystemId` ensures accurate user management, security policies, and compliance reporting in SAP environments. Misconfiguration could lead to security breaches, non-compliance penalties, and inaccurate risk assessment.

**Technical Impact when configured:** When configured, the `SapUsersSystemId` enables the Pathlock Cloud GRC platform to accurately align SAP user activities and data with the correct SAP system, ensuring the enforcement of appropriate GRC controls and policies.

**Examples Scenario:** If an organization has multiple SAP systems for different business units, configuring `SapUsersSystemId` with the correct identifier for each unit allows for precise monitoring, reporting, and enforcement of security and compliance measures per system.

**Related Settings:** 

- `LogWorkflowRequestsFromEmailAccounts`
- `TechnicalNameForUserCreatedManually`

**Best Practices:** configure when setting up SAP user management within the Pathlock Cloud GRC platform to ensure accurate mapping and governance. Avoid configuration errors by double-checking system IDs against your SAP environment setup.