# Handle Open Requests

**Category:** Workflow

**Description:** The "Handle Open Requests" action is designed to automate the management of open workflow requests within the Pathlock Cloud platform, focusing particularly on actions like approving or declining specific steps in a workflow or entirely closing requests. This action evaluates the workflow instance and its parameters to decide whether to approve or decline the workflow steps or requests based on predefined criteria such as the workflow type, specific steps, or child workflows. By leveraging information about the user, workflow instance, and additional parameters, it ensures targeted and efficient workflow management.

**Parameters:** 

- Basic:
  - Name: WorkflowOperationToPerform
    Description: Defines the operation to be performed on the workflow, either to approve the current step or to close all current requests.
    Default value: N/A
    Mandatory: yes
    
  - Name: WorkflowTypeOfOpenWorkflow_WorkflowTechnicalName
    Description: The technical name of the workflow type being managed. This parameter helps in identifying the specific type of workflow requests to act upon.
    Default value: N/A
    Mandatory: yes
  
- Advanced:
  - Name: CommentForWorkflowOperation
    Description: Allows the operator to provide a comment when closing the workflow, which can be used for audit trails or providing context for the action taken.
    Default value: N/A
    Mandatory: no
  
  - Name: ActOnChildWorkflows
    Description: Determines whether the action should be applied to all open child workflows of the current request.
    Default value: false
    Mandatory: no

  - Name: WorkflowTypeOfOpenWorkflow_FilterByFieldTechnicalName
    Description: Specifies a technical name of a field to filter the workflows that this action should apply to.
    Default value: N/A
    Mandatory: no
  
  - Name: ActOnStepName
    Description: Specifies a step name to target the action to only those workflows that are currently on a specific named step.
    Default value: N/A
    Mandatory: no

**Business impact:** The "Handle Open Requests" action is crucial for maintaining the integrity and effectiveness of the identity and governance, risk, and compliance workflow within Pathlock Cloud. By automating the approval or closure of open requests, this action plays a key role in ensuring that workflows are processed efficiently, reducing manual intervention and potential errors, and helping maintain compliance with internal policies and external regulations.

**Example of usage:** To automatically decline all open requests of a specific workflow type that have not yet been closed and are associated with a specific user, set `WorkflowOperationToPerform` to "Close," define the `WorkflowTypeOfOpenWorkflow_WorkflowTechnicalName` to match the specific workflow, and optionally specify a comment for auditing purposes. 

**Prerequisites:** User must have the necessary permissions to perform workflow actions such as approving or closing workflow instances. The user should also have access to the technical names of workflow types and optionally the specific fields or steps if filtering is required.

**Error Handling and Troubleshooting:**

- Error: Workflow instances not found.
  Probable Cause: Incorrect or non-existing `WorkflowTypeOfOpenWorkflow_WorkflowTechnicalName`.
  Recommended Solution: Verify the technical names of the workflow types and ensure they match those configured within the Pathlock Cloud platform.
  
- Error: No effect on workflow instances.
  Probable Cause: Filter parameters (`WorkflowTypeOfOpenWorkflow_FilterByFieldTechnicalName`, `ActOnStepName`) are too restrictive or mismatched.
  Recommended Solution: Review the applied filters and parameter values to ensure they accurately reflect the intended targets among the open requests.
  
- Error: Unauthorized action attempt.
  Probable Cause: User lacks necessary permissions.
  Recommended Solution: Ensure the user has appropriate permissions to approve or close workflow instances. Consult with your Pathlock Cloud administrator to adjust user permissions as needed.