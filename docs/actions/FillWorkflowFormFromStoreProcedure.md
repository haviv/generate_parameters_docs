# FillWorkflowFormFromStoreProcedure

**Category:** Workflow

**Description:** The FillWorkflowFormFromStoreProcedure action automates the filling of workflow forms using data retrieved from a specified stored procedure. This action takes a procedure name and a set of parameters as inputs, executes the stored procedure, and then maps the results to form fields in the workflow. The action supports dynamic parameter resolution and can work with complex data types, allowing for flexible form filling strategies that can adapt to different workflow requirements.

**Parameters:** 

*Basic:*
- Name: procedureName
  - Description: The name of the stored procedure to be executed. This parameter is used to identify which stored procedure's data will populate the form fields.
  - Default value: none
  - Mandatory: yes

- Name: procedureParameters
  - Description: A comma-separated list of parameters to pass to the stored procedure. These parameters are dynamically parsed and used within the stored procedure call to fetch the relevant data.
  - Default value: none
  - Mandatory: yes

*Advanced:*
- Name: procedureParameter_[dynamicParameter]
  - Description: Represents dynamic parameters that are specific to the stored procedure. These are prefixed with `procedureParameter_` and mapped according to the stored procedure's requirements.
  - Default value: varies based on dynamic values
  - Mandatory: no

**Business impact:** This action streamlines the process of populating workflow forms with necessary data by automating data retrieval and mapping operations. It reduces manual data entry errors, ensures data consistency, and improves efficiency in workflows that require complex data collection and processing, such as Access Management, Risk Calculation, and Policy Management scenarios.

**Example of usage:** Suppose you have a workflow that requires user details to start a User Access Review process. By using the FillWorkflowFormFromStoreProcedure action with a stored procedure named `GetUserDetails` and appropriate input parameters (e.g., UserID), the workflow form can be automatically filled with the user's details pulled from the database, thus kickstarting the review process efficiently.

**Prerequisites:** The user must ensure that the stored procedure exists in the database and is accessible to the workflow engine. Necessary database permissions must be configured to allow execution of the stored procedure from the workflow engine.

**Error Handling and Troubleshooting:** 

- Error: Stored procedure does not exist.
  - Cause: The specified stored procedure name is incorrect or the procedure does not exist in the database.
  - Solution: Verify the stored procedure name and ensure it exists in the database.
  
- Error: Procedure executed with errors.
  - Cause: Missing or incorrect procedure parameters.
  - Solution: Check the parameter list for accuracy and completeness according to the stored procedure requirements.

- Error: Data mapping errors.
  - Cause: The result set columns do not match the workflow form fields.
  - Solution: Review the stored procedure's result set and ensure it aligns with the form fields needing population. Adjust either the form fields or the procedure as necessary.