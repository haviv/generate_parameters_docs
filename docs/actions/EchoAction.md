# EchoAction

**Category:** Workflow

**Description:** 
The EchoAction is a fundamental workflow component designed to receive input from a user or another action and return that input as the result. When executed, it reads a specific value, identified by the parameter "MyValue", from the supplied WorkflowActionParameters. It then sets this value as the action's result without any transformation. This simple flow enables the EchoAction to serve as a validation or feedback mechanism within a broader workflow, confirming the successful receipt of expected input.

**Parameters:** 

_Basic:_

- Name: MyValue
- Description: The value that is echoed back by the action. This can be any string provided by the caller or preceding actions within the workflow.
- Default value: None
- Mandatory: Yes

_Advanced:_

_None_

**Business impact:** 
Though simple, the EchoAction plays a critical role in workflow debugging and validation. By confirming the presence and correctness of specific inputs, it helps in verifying that upstream components in the workflow are operating as expected. This can be particularly useful in complex identity, access, or compliance workflows, where each step's output directly impacts subsequent operations.

**Example of usage:**
In a user onboarding workflow, the EchoAction could be used to confirm the receipt of a necessary input, such as a user ID or access level request, before proceeding to more complex actions such as provisioning access or evaluating risk.

**Prerequisites:** 
No specific prerequisites are required to execute the EchoAction beyond the general ability to initiate workflows within the Pathlock Cloud platform and provide the necessary input parameter ("MyValue").

**Error Handling and Troubleshooting:** 

- **Error:** "Parameter 'MyValue' not found."
    - **Cause:** The required parameter "MyValue" was not supplied in the WorkflowActionParameters.
    - **Solution:** Ensure that the "MyValue" parameter is included in the action parameters with a valid value.

- **Error:** "Unexpected error."
    - **Cause:** General catch-all for unexpected exceptions during the execution of the action.
    - **Solution:** Verify the workflow configuration and inputs are correct. If the problem persists, consult Pathlock Cloud documentation or support for further assistance.