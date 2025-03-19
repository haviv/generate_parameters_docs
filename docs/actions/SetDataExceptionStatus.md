Action name: SetDataExceptionStatus

**Category:** Workflow

**Description:** The `SetDataExceptionStatus` action is designed to update the status of data exceptions within the Pathlock Cloud platform. This action targets exceptions identified by their unique identifier and updates their statuses based on predetermined values stored within the system. If the `ForceClose` parameter is set to true and the new status allows for workflow continuation, this action also triggers the closure of the identified exception. The action operates within the context of transaction monitoring, enabling administrators or automated systems to manage exception statuses efficiently, ensuring compliance with internal procedures and regulatory requirements.

**Parameters:** 

- Basic:
    - Name: ExceptionId
      Description: The unique identifier of the data exception to be updated. It is used by the `Perform` method to locate the exception record in the database.
      Default value: None
      Mandatory: yes
    
    - Name: NewStatus
      Description: The new status value to be applied to the data exception. It maps to a specific `SodStatus` within the system and determines the next steps in the handling of the exception.
      Default value: None
      Mandatory: yes

- Advanced:
    - Name: ForceClose
      Description: A boolean parameter that, when true and if the new status permits, forces the closure of the identified exception. This is used in scenarios where immediate resolution of the exception is required.
      Default value: False
      Mandatory: no

**Business impact:** The `SetDataExceptionStatus` action plays a crucial role in the maintenance of data integrity and the enforcement of governance, risk management, and compliance (GRC) standards within the Pathlock Cloud platform. By enabling automated or manual updates to exception statuses, it assists in the swift resolution of issues, reduces the time and resources needed for manual oversight, and ensures a more consistent application of policies across the board.

**Example of usage:** An example scenario could involve an automated review process that identifies exceptions requiring immediate attention. Upon detection, the `SetDataExceptionStatus` action could be invoked to update the status of each exception to "Review Required" and, if the situation demands, force close the exception to halt further processing until reviewed by a human operator.

**Prerequisites:** The user or system account performing this action must have adequate permissions to update exception statuses and initiate closures. This typically includes roles such as Administrator, Compliance Officer, or a service account with specific rights within the Pathlock platform.

**Error Handling and Troubleshooting:** 

- *Error: Exception ID not found* 
    - Cause: The specified `ExceptionId` does not match any records in the database.
    - Solution: Verify the `ExceptionId` for accuracy and ensure it corresponds to an existing data exception.

- *Error: Invalid NewStatus value*
    - Cause: The `NewStatus` provided does not exist within the system's status values.
    - Solution: Check the permitted values for the `NewStatus` parameter and ensure a valid value is being used.

- *General Troubleshooting Tips:* 
    - Ensure that all mandatory parameters (`ExceptionId`, `NewStatus`) are correctly provided and valid.
    - Verify that the specified status allows for the desired action (e.g., force close) and that the `ForceClose` parameter is appropriately set.
    - In case of unexpected behavior, consult the system logs for more detailed error messages or contact Pathlock support for assistance.