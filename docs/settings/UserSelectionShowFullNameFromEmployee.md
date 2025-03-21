# User Selection Show Full Name From Employee

**Technical Name:** UserSelectionShowFullNameFromEmployee

**Category:** User Management

**Default Value:** (not specified in the references provided)

**Impact Level:** Medium

**Description:**

This parameter controls whether the full name of an employee is displayed to the user from within the platform's auto-completion fields or data selection queries. When enabled, it enhances the user's ability to accurately identify and select the correct employee records by displaying more detailed information.

**Business Impact:**

Enabling this feature improves user experience and operational efficiency by reducing errors in employee selection, which is crucial for managing permissions, roles, and access within the Pathlock Cloud GRC platform. It particularly benefits processes related to security, risk management, and compliance by ensuring that actions are taken against the correct employee records.

**Technical Impact when configured:**

Configuring this setting affects how employee information is presented across various modules of the Pathlock Cloud GRC platform that utilize auto-completion for employee selection. It directly impacts data retrieval and display logic in the UI, pulling full names from employee records instead of limited identifiers.

**Examples Scenario:**

In an HR compliance workflow, a user needs to assign specific compliance tasks to an employee with a common name (e.g., "John Smith"). With this parameter enabled, the platform displays the full names and possibly department descriptions, making it easier to distinguish between individuals and select the correct "John Smith" for task assignment.

**Related Settings:** Custom_Sql_Query_For_Rest_API_HR_DataSource

**Best Practices:** configure when you have a large organization with employees who may share common names, avoid when concise data presentation is preferred for speed over accuracy.