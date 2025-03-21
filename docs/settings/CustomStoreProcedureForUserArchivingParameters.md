# Custom Store Procedure For User Archiving Parameters

**Technical Name:** CustomStoreProcedureForUserArchivingParameters

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter defines the custom stored procedure that is executed during the user archiving process. It allows for additional, organization-specific logic to be applied, ensuring that user data handling complies with internal policies and regulations.

**Business Impact:**

By configuring this parameter, organizations can ensure that the archiving of user accounts is compliant with internal policies and regulatory requirements. This can significantly affect compliance status, data security, and risk management practices.

**Technical Impact when configured:**

When this parameter is configured, the system triggers the specified custom stored procedure during the user archiving process. This can include checks for unique conditions, data cleanup, or any other custom logic required by the organization.

**Examples Scenario:**

A company requires that when a user is archived, a check is performed against custom criteria (e.g., department, last login date) to decide if additional actions (such as notifying a manager or exporting user data) are necessary. By setting this parameter to the name of a custom stored procedure, these actions can be automated as part of the user archiving process.

**Related Settings:**

- HasCustomLogicForUserArchiving
- CheckUniqueCustomLogicForUserArchiving

**Best Practices:** 

- **Configure when:** There is a need for custom logic during the user archiving process that is not covered by the default functionality. This could include organizational-specific compliance checks, notifications, or data handling requirements.
  
- **Avoid when:** The default user archiving process meets the organization's requirements, or if custom logic might introduce unnecessary complexity or potential security risks.