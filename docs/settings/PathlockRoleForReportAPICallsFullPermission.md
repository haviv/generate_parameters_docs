# Pathlock Role For Report APICalls Full Permission

**Technical Name:** PathlockRoleForReportAPICallsFullPermission

**Category:** Security

**Default Value:** None

**Impact Level:** High

**Description:**

This parameter is used to manage access control for executing and accessing custom reports through the API. It defines a security role which a user must have to run specific reports, ensuring that only authorized personnel can access sensitive data through report API calls.

**Business Impact:**

Restricting access to report generation and data retrieval to authorized users helps in maintaining the confidentiality and integrity of sensitive organizational data. It ensures that critical information is not exposed to unauthorized users, hence supporting compliance with data protection regulations and internal security policies.

**Technical Impact: when configured**

When configured, this parameter acts as a gatekeeper for API calls related to report generation and access. It ensures that only users with the specified role can make API calls to run custom reports, thereby providing an additional layer of security and access control within the Pathlock GRC platform.

**Examples Scenario:**

A company has developed a set of custom reports that contain sensitive financial data. To mitigate the risk of data exposure, the company uses the `PathlockRoleForReportAPICallsFullPermission` parameter to specify a role, say "FinanceAPIAccess", which is required to execute these reports. Only users with this role assigned can access and generate the reports through API calls, ensuring that sensitive information remains secure.

**Related Settings:**

- HideRefreshButtonInInbox

**Best Practices:** 

- **Configure when**: You need to restrict access to sensitive reports and their generation to a certain group of users. Assign the permission to roles associated with users who require API access for report generation based on their job responsibilities.
- **Avoid when**: All users require equal access to report generation and there's no sensitivity or risk associated with the data being accessed via the reports.