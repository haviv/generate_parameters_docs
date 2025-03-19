# ParametersUpdate

**Category:** User Management

**Description:**

The `ParametersUpdate` action is designed to update user properties either for a specified user or for the user associated with the current workflow execution context. It operates in two modes based on the availability of a specified user: if a user is found within the current system context, it updates properties for this user; if no user is found, it tries to update properties for a custom username provided via action parameters. The action first attempts to target a specific system for the update based on an ID passed as a parameter; if this fails or no ID is provided, it defaults to the system associated with the user or a pre-defined system. The main flow involves initializing the context for the target system, updating user properties through a system connector, and setting the result of the operation.

**Parameters:**

- Basic:
    - Name: actionDestSystemId
    - Description: The ID of the target system where user properties will be updated. It is used to initialize the context to the specific system before performing the update.
    - Default value: System associated with the user OR default system if no user is found.
    - Mandatory: No

    - Name: ActionDestCustomUsername
    - Description: A custom username for which the update operation will be performed. This parameter is used when the operation needs to target a user not found within the current system context.
    - Default value: null
    - Mandatory: No

**Business impact:**

The `ParametersUpdate` action plays a crucial role in managing user identities and permissions within the Pathlock cloud platform. By allowing dynamic updates to user properties across different systems, it supports streamlined access management, ensures users have the appropriate access for their roles, and aids in compliance by ensuring that user data is current and accurate. This functionality directly impacts operational efficiency, security posture, and compliance status.

**Example of usage:**

To update a user's properties in system with ID `5`, the action would be configured with the `actionDestSystemId` parameter set to `5`. If updating a user not found by the system sync, `ActionDestCustomUsername` might be set to the relevant username. As part of a workflow, this may look like:

1. Initiating the `ParametersUpdate` action.
2. Setting `actionDestSystemId` to `5`.
3. Optionally setting `ActionDestCustomUsername` if updating properties for a user not found in the system.

This configuration would instruct the action to target system ID `5` for the update, or use the custom username if provided and the user is not found in the system.

**Prerequisites:**

- The user executing this action must have permissions to update user properties in the target system.
- A valid system ID or custom username must be provided as part of the action parameters if targeting a specific system or user.

**Error Handling and Troubleshooting:**

1. **System ID not found or invalid**:
   - **Cause:** The system ID provided does not exist or is not accessible.
   - **Solution:** Verify the system ID and ensure it corresponds to a system within the Pathlock platform and that proper permissions are set.
   
2. **Custom username not found**:
   - **Cause:** The custom username provided does not match any user in the target system.
   - **Solution:** Double-check the username for typographical errors or update the synchronization settings to ensure all users are correctly imported into the system.
   
3. **Property update failure**:
   - **Cause:** An error occurred while updating properties due to system restrictions, missing permissions, or invalid property values.
   - **Solution:** Review the user properties being updated for any invalid entries and ensure that the account used to perform the action has the necessary permissions.