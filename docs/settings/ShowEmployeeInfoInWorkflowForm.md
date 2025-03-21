# Show Employee Info In Workflow Form

**Technical Name:** ShowEmployeeInfoInWorkflowForm

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

Enables the display of employee information directly within the workflow form. This feature assists in providing context and clarity during the execution of workflow actions, specifically at the initiation phase.

**Business Impact:**

Improves the efficiency of workflow executions by providing immediate employee-related details, which can be critical for decision-making processes within governance, risk management, and compliance activities. 

**Technical Impact when configured:**

Once enabled, employee details will be visible to the workflow initiators or participants, reducing the need to cross-reference or navigate away from the workflow form to gather necessary information. 

**Examples Scenario:**

- A manager initiating an access review workflow can see the employee's department, role, and other relevant details within the form, facilitating a more informed and efficient review process.

**Related Settings:**

- `HideUsernameSelection`
- `AuthorizationRequestOverrideUsernameText`

**Best Practices:** 

- **Configure when:** Immediate access to employee details is essential for making informed decisions during the workflow process.
- **Avoid when:** Employee information is sensitive and should not be displayed broadly within workflow forms.