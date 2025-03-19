# TerminateUser

**Category:** User Management

**Description:** The TerminateUser action automates the process of deactivating or terminating a user's access to systems and services. It encompasses several steps, including locking the user account, updating pertinent system properties, and ensuring compliance with company policies on user termination. The workflow is initiated by identifying the employee user(s) needing termination, followed by locking their accounts, and updating their system properties as per predefined rules. This automated process ensures a swift and secure method of handling user termination requests.

**Parameters:**

- Basic:
  - Name: WorkflowInstance
    Description: Represents the instance of the workflow being executed. It is used to maintain the context and manage state across different actions within the same workflow.
    Default value: N/A
    Mandatory: yes

- Advanced:
  - Name: WorkflowActionToPerformId
    Description: Identifies the specific user termination action to be performed. This parameter is crucial for selecting the correct properties to update following the termination action.
    Default value: N/A
    Mandatory: yes
  - Name: SystemId
    Description: The system identifier of the user to be terminated. It is used to initiate the termination context for the specific user's system.
    Default value: N/A
    Mandatory: yes

**Business impact:** The TerminateUser action is critical for maintaining security and compliance within an organization. By automating the user termination process, it ensures that access is revoked in a timely and secure manner, minimizing the risk of unauthorized access and potential data breaches. Additionally, it helps to uphold compliance standards by ensuring that all user terminations are processed according to company policy and regulatory requirements.

**Example of usage:** To terminate a user, the workflow engine would be invoked with the TerminateUser action, specifying the WorkflowInstance, WorkflowActionToPerformId, and the user's SystemId. The action would then lock the user's account and update system properties as necessary, based on the workflows configured actions and rules.

**Prerequisites:** Before executing the TerminateUser action, the calling entity must have the appropriate permissions to initiate user terminations. Additionally, the WorkflowInstance and relevant parameters must be correctly specified to ensure the action targets the correct user and follows the intended termination procedures.

**Error Handling and Troubleshooting:**

- If the specified user cannot be found or is already terminated, verify the provided SystemId or WorkflowInstance parameters are correct.
- Should the action fail to lock the user account or update system properties, ensure the WorkflowActionToPerformId is correctly set and that the system connectors are properly configured and operational.
- In case of unexpected errors, review system logs for more detailed error messages. Ensure that all prerequisite configurations are correct and consult technical support if the issue persists.