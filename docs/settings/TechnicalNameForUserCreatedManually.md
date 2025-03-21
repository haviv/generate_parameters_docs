**Technical Name: TechnicalNameForUserCreatedManually**

**Category:** Workflow

**Default Value:** Null

**Impact Level:** Medium

**Description:** This parameter is used to define or modify technical names for user attributes manually within the workflow context. It enables administrators to specify technical names that align more closely with the business semantics or organizational terminologies that are not covered by the default settings.

**Business Impact:** Proper utilization of this parameter can streamline the workflow configuration by ensuring that technical names are meaningful and recognizable within business processes. This can lead to improved audit trails, easier identification of workflow components, and enhanced user adoption due to clearer terminology.

**Technical Impact when configured:** Configuring this parameter modifies how user attributes are referenced within the platform's workflows. This can affect conditions, actions, and any other workflow part that utilizes technical names. Incorrect configurations can lead to misidentification of workflow elements or failure in workflow execution.

**Examples Scenario:** An organization might use the term "EmpID" instead of the default "EmployeeLastName" for referring to employees within their workflows. By configuring this parameter to use "EmpID," workflows that involve employee identification can be aligned with the organization's internal naming conventions, thus reducing confusion.

**Related Settings:** GenderField, GenderMaleValue

**Best Practices:** configure when standard technical names do not align with organizational terminology or when custom workflow attributes are introduced. Avoid when the default technical names meet the organizational needs to prevent unnecessary complexity.