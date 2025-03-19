Action Name: AskForHelp

**Category:** Workflow

**Description:**  
The `AskForHelp` action is designed to facilitate communication between different stakeholders in a workflow process by creating an alternative step within the current workflow instance. When invoked, this action dynamically requests assistance or approval from a specified approver (or group) by generating a new workflow step. This step is appended with a custom message and an alternative step name to distinguish it from standard workflow steps. The process leverages the existing workflow infrastructure, ensuring that the request for help is seamlessly integrated into the overall workflow process, thus maintaining the flow's integrity and auditability.

**Parameters:**  
_Basic:_  
- Name: Approver  
  Description: The name of the approver or approval group that the help request is directed to. This parameter is essential for identifying the recipient of the request within the workflow. The approver is fetched from the `WorkflowApprovalGroups` based on the name provided.  
  Default value: None  
  Mandatory: Yes  

- Name: Message  
  Description: Custom message or request details sent to the approver. This parameter allows the requester to convey additional context or instructions relevant to the help request.  
  Default value: None  
  Mandatory: Yes  

_Advanced:_  
- Name: AskForHelp_StepName  
  Description: An optional parameter that specifies a custom step name prefix for the help request step. This is concatenated with the existing step name to generate a unique identifier for the new step created by this action. If not provided, a default prefix is used.  
  Default value: "need your help for"  
  Mandatory: No  

**Business impact:**  
The `AskForHelp` action plays a pivotal role in enabling fluid communication and collaboration within workflow processes, particularly in complex identity and GRC platforms like Pathlock Cloud. By empowering users to request assistance directly within the workflow, organizations can ensure that processes are not stalled due to uncertainties or the need for additional approvals. This contributes to more efficient operations, better compliance posture through maintained oversight, and enhanced risk management as potential issues are addressed proactively.

**Example of usage:**  
In a scenario where a user is executing a workflow for access review and requires additional approval from the compliance team, the `AskForHelp` action can be invoked to add a step requesting this approval. The action parameters would include the `Approver` set to the compliance team's group name, and a `Message` detailing the need for their input.

**Prerequisites:**  
- The user invoking the `AskForHelp` action must have permissions to modify the workflow or initiate help requests based on the platform's access control policies.
- The specified approver or approval group must exist within the system.

**Error Handling and Troubleshooting:**  
- **Error:** Approval group not found  
  **Cause:** The specified approver name does not match any groups in the system.  
  **Solution:** Verify the approver's name and ensure it exactly matches an existing approval group in the system.  

- **Error:** Message parameter not provided  
  **Cause:** The action was invoked without a `Message` parameter, which is mandatory for contextualizing the help request.  
  **Solution:** Ensure a meaningful message is provided when invoking the action to clearly communicate the assistance needed.  