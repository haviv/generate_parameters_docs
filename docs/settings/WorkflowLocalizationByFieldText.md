**Technical Name:** WorkflowLocalizationByFieldText

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter is used to determine if workflow forms display information localized based on the content of specific fields within the form. It influences how information is presented to the user, potentially altering the workflow's language or terminology based on user preferences or data specifics.

**Business Impact:**

Enabling localization by field text can enhance user understanding and interaction with the system by presenting data in a context that is more familiar to them. It can lead to more efficient workflow processing and reduce the risks of misinterpretation, especially in globally distributed teams.

**Technical Impact when configured:**

When active, this feature dynamically adjusts the display language or terminology of workflow forms based on the user's settings or field-specific data. This might increase the complexity of form design and could affect form loading times due to the additional processing required to determine the correct localization settings.

**Examples Scenario:**

A multinational company uses the Pathlock Cloud GRC platform for processing access requests. By enabling `WorkflowLocalizationByFieldText`, when a user from the France office opens a workflow form, the field texts and instructions within the workflow could be automatically presented in French, based on either their user settings or field values indicating the request is for the France office.

**Related Settings:**

- `AutomaticRoleAssignmentsDefaultUserGroupTypeId`
- `RequestsWaitingForApprovalGetDataFromStoredProcedure`

**Best Practices:** Configure this parameter to enhance user experience in environments with diverse user bases. Avoid using it in simple or uniform linguistic environments to keep the system's complexity and processing requirements minimal.