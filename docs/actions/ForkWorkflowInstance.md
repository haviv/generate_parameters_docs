# ForkWorkflowInstance

**Category:** Workflow

**Description:** 
The `ForkWorkflowInstance` action is designed to manage workflow instances by either updating the current workflow or duplicating it based on the conditions provided. This action checks for the specific conditions that determine whether to create a new workflow instance or update an existing one with new information. It involves parsing and utilizing user input, creating or updating workflow instances, adding workflow steps, and managing workflow actions and authorization requests. The action concludes by generating a summary output of the performed action, focusing on duplicating workflows with specific updates on comments, user IDs, and system IDs.

**Parameters:**

*Basic*

- Name: usernamesField
    - Description: Specifies the field containing the usernames involved in the workflow. It is used as a key parameter to identify the target user(s) for the workflow action.
    - Default value: N/A
    - Mandatory: Yes

- Name: commentTemplate
    - Description: A template for comments that is appended to the workflow instance or used in the creation of new instances. It provides context and additional information related to the workflow action.
    - Default value: N/A
    - Mandatory: Yes

*Advanced*

N/A

**Business impact:** 
This action plays a crucial role in managing and controlling workflow processes within the Pathlock Cloud platform. By allowing the fork of workflow instances, it enables flexible handling of access, risk calculations, and other identity-related requests, directly impacting the efficiency and responsiveness of GRC processes. It ensures that actions are taken based on the most current data and situations, enabling dynamic and adaptive management of identities and permissions.

**Example of usage:** 
A user initiates a request for access to a specific system. The `ForkWorkflowInstance` action checks whether a new workflow should be initiated or if the existing one should be updated based on the usernames and comments provided. If a new instance is warranted based on the unique conditions and parameters provided, the system duplicates the workflow, updates necessary information, and proceeds with the new workflow steps, ensuring timely and relevant handling of the access request.

**Prerequisites:** 
- The user must have sufficient permissions to initiate or update workflow instances.
- Relevant workflow types and steps must be predefined in the system.
- Necessary parameters (usernamesField and commentTemplate) must be provided accurately.

**Error Handling and Troubleshooting:** 

- **Common Error Scenario:** Failing to duplicate or update a workflow instance.
    - **Probable Cause:** Incorrect or missing parameters (`usernamesField` or `commentTemplate`).
    - **Recommended Solution:** Ensure that all mandatory parameters are provided correctly and verify the syntax and values used.

- **Common Error Scenario:** Workflow duplication does not trigger the expected next steps.
    - **Probable Cause:** Workflow configuration issues or invalid workflow steps defined.
    - **Recommended Solution:** Review the workflow configuration, ensure that all steps are correctly defined, and verify that the conditions for duplicating the workflow instance are met accurately.