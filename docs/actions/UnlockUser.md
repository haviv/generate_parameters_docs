# UnlockUser

**Category:** User Management

**Description:**  
This action is designed to unlock user accounts in multiple systems and assess their validity status within the Pathlock Cloud environment. When executed, it performs the following steps:

1. Retrieves a user account based on the system ID provided in the parameters.
2. Initializes the context for the targeted system to facilitate communication with the system's user management connectors.
3. Calls the `UnlockUser` method from the `ProvisionService` to unlock the specified user in the system.
4. If the `EnableExpiredUser` parameter is set to true and the user is identified as invalid, it sets the user's validity state to a default valid status using the system connector's `SetUserValidity` method.

**Parameters:**  
- Basic:
    - Name: SystemId
      Description: The identifier for the system in which the user account exists and needs to be unlocked. This parameter is used to initialize the context and retrieve user details for the action.
      Default value: None
      Mandatory: Yes
- Advanced:
    - Name: EnableExipredUser
      Description: A boolean flag that determines whether an expired or invalid user should be set to a valid state after unlocking. This parameter influences the final step of the workflow, potentially altering user validity status.
      Default value: False
      Mandatory: No

**Business impact:**  
Using the UnlockUser action has a significant impact on operational efficiency and security compliance within an organization. It ensures that users who are locked out of their accounts due to password entry errors or other security measures can quickly regain access, thereby minimizing downtime and productivity loss. Moreover, by automating the unlock process and providing an option to reset validity status, it streamlines user account management and enhances the organization's adherence to access control policies.

**Example of usage:**  
Consider a scenario where a user from the SAP system, identified by SystemId `101`, gets locked out. An administrator wants to unlock this account and ensure it is marked as valid automatically if it was previously expired:

1. The administrator sets the `SystemId` parameter to `101`.
2. The `EnableExipredUser` parameter is set to `true` to ensure the user's account is active post-unlocking.
3. The UnlockUser action is executed with these parameters to unlock the user’s account and update its validity status as needed.

**Prerequisites:**  
- Administrative privileges for the Pathlock Cloud Dashboard.
- Valid SystemId corresponding to the user's locked account system.
- The system connector must be correctly configured and able to communicate with the targeted system for user management operations.

**Error Handling and Troubleshooting:**  
- **Error:** Action fails to unlock the user.
  - **Cause:** SystemId incorrect or not provided.
  - **Solution:** Verify the SystemId for accuracy and ensure it is provided in the parameters.
- **Error:** User validity status does not update.
  - **Cause:** The `EnableExipredUser` parameter is set to false, or there's an issue with the system connector's `SetUserValidity` method.
  - **Solution:** Ensure `EnableExipredUser` is set to true if you wish to update user validity status. Check logs for any errors regarding the system connector's operations and correct any configuration issues.