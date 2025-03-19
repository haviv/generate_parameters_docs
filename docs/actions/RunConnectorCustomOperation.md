# RunConnectorCustomOperation

**Category:** Workflow

**Description:**
The RunConnectorCustomOperation action is a versatile component designed to execute custom operations within the Pathlock Cloud's workflow engine. It allows for the automation of various tasks like Privileged Access Management (PAM), access requests, and risk calculation by interfacing directly with system connectors. This action can dynamically adapt to execute specific operations based on provided parameters, such as system ID or operation type, and can handle complex inputs like business roles and collections for bulk processing. Additionally, it supports form filling, enabling seamless data integration across systems.

**Parameters:**

_Basic Parameters:_

- Name: SystemId
  Description: Identifies the target system on which the operation is to be performed. This parameter determines the context in which the custom operation executes.
  Default value: N/A
  Mandatory: Yes

- Name: Operation
  Description: Specifies the custom operation to execute. It must correspond to one of the available operations in the system connector.
  Default value: N/A
  Mandatory: Yes

_Advanced Parameters:_

- Name: CollectionName
  Description: Specifies a collection name for operations that process bulk data. Used to identify the collection within the request data to apply the action on multiple elements.
  Default value: N/A
  Mandatory: No

- Name: EnableFillForm
  Description: Determines whether to fill a form with the output of the custom operation. Useful for operations that need to capture or display output data in a structured format.
  Default value: false
  Mandatory: No

- Name: FillFormMapping
  Description: Defines the mapping between the operation output and the form fields. Required if EnableFillForm is true, mapping ensures the correct placement of data in form fields.
  Default value: N/A
  Mandatory: No

**Business impact:**
Enabling custom operations through the RunConnectorCustomOperation action significantly enhances the flexibility and efficiency of identity and GRC-related workflows. It provides a mechanism to automate specific, often complex, business processes directly within the Pathlock Cloud platform. For example, dynamically managing user access or processing risk assessments, tailored to the unique requirements of an organization, directly impacts operational security, compliance, and overall risk management posture.

**Example of usage:**

```csharp
// Assuming the existence of a predefined workflow setup
WorkflowActionParameters parameters = new WorkflowActionParameters {
    {"Operation", "CreateUserAccessRequest"},
    {"SystemId", "1001"},
    {"BusinessRole", "FinanceManager"},
    {"EnableFillForm", true},
    {"FillFormMapping", "UserId,AccessLevel"}
};

runConnectorCustomOperation.Perform(parameters);
```

**Prerequisites:**
- The user executing the action must have sufficient permissions to perform the desired operation within the specified system.
- The specified system must be configured and accessible within the Pathlock Cloud platform.
- Necessary mappings and configurations for the operation and form filling must be predefined.

**Error Handling and Troubleshooting:**

- **Error: Operation failed to execute**
  Cause: The specified operation might not exist, or the system ID could be incorrect.
  Solution: Verify the operation name and system ID.

- **Error: Form filling failed**
  Cause: Incorrect FillFormMapping configuration.
  Solution: Ensure the FillFormMapping accurately matches the output of the custom operation to the form's fields.

For further troubleshooting or assistance, consult the Pathlock Cloud support documentation or reach out to technical support.