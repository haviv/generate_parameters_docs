# Sap Connector Last Logon Field

**Technical Name:** SapConnectorLastLogonField

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

The `SapConnectorLastLogonField` parameter is designed to identify and filter SAP user data based on the last logon field. This parameter is crucial for maintaining and monitoring active users within the SAP system, ensuring that user access is up-to-date and aligning with security and compliance standards.

**Business Impact:**

Efficient management of the `SapConnectorLastLogonField` ensures that only active users have access to the SAP system, reducing the risk of unauthorized access. It helps in auditing and compliance by providing accurate reports on user activity, aiding organizations in adhering to security policies and regulatory requirements.

**Technical Impact when configured:**

Configuring this parameter helps in refining user data synchronization and reporting by filtering users based on their last logon date. This ensures that user management processes, such as role assignments and access reviews, are performed on an accurate and current user base, improving overall system security and performance.

**Examples Scenario:**

In a scenario where an organization needs to audit its SAP system users for compliance purposes, the `SapConnectorLastLogonField` can be used to filter out users who have not logged in within the last 90 days, focusing the audit on active users and simplifying compliance checks.

**Related Settings:**

- `UsernameFieldInCustomReports`

**Best Practices:** 

- **Configure when** initiating a system-wide review of user activity or preparing for an audit to ensure compliance with access policies.
- **Avoid when** the majority of your SAP system users are infrequent but legitimate users, as this could inadvertently filter out valid users from reports and analyses.