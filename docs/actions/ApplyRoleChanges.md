# ApplyRoleChanges

**Category:** User Management

**Description:** The `ApplyRoleChanges` action automates the process of applying changes to user roles within the Pathlock Cloud Platform, specifically focusing on updating role authorizations based on dynamic parameters. When invoked, it retrieves or constructs changes pertaining to role authorizations, initializes the application context for the specified target system, and updates the role using the designated connector. Finally, it refreshes the role information to reflect the updated authorizations. This action is critical for maintaining precise control over access rights and ensuring that authorization adjustments are propagated correctly across the system.

**Parameters:** 

- **Basic Parameters:**
  - **Name:** TargetSystemIdBasedOnParameters
    - **Description:** Specifies the target system ID for which the role changes are to be applied. If not provided, the system ID associated with the user's current session is used.
    - **Default value:** Derived from the user's session
    - **Mandatory:** No
    
  - **Name:** NewRoleName
    - **Description:** Allows specifying a new role name for which the authorization changes are intended. If not provided, the action attempts to infer the role name from the request context.
    - **Default value:** None
    - **Mandatory:** No

- **Advanced Parameters:**
  - **(None)**

**Business impact:** Modifying role authorizations directly affects system security and user access control. The `ApplyRoleChanges` action enables administrators to dynamically adjust access rights, ensuring that users have appropriate access levels based on their current roles, responsibilities, and compliance requirements. It streamlines the management of complex authorization changes, which is essential for maintaining operational integrity and compliance in dynamic environments.

**Example of usage:** Suppose an administrator needs to update the role of a user to include additional transaction authorizations due to changing job responsibilities. The administrator can trigger the `ApplyRoleChanges` action, specifying the `NewRoleName` and relevant transaction IDs to update the user's access rights accordingly.

**Prerequisites:** Before executing the `ApplyRoleChanges` action, the user must have the necessary permissions to modify role authorizations within the Pathlock Cloud Platform. Additionally, the target system and role name should be correctly identified, and any specific transaction IDs that require authorization changes must be available.

**Error Handling and Troubleshooting:** 

- **Common Error:** Role name not specified
  - **Probable Cause:** The `NewRoleName` parameter was not provided and could not be inferred from the request context.
  - **Solution:** Ensure that the role name is specified either through the `NewRoleName` parameter or is inferable from the request context.

- **Common Error:** Target system ID invalid
  - **Probable Cause:** The specified target system ID does not exist or was entered incorrectly.
  - **Solution:** Verify the target system ID for accuracy. If it is based on the user's session and incorrectly determined, ensure the session information is correct.

- **Common Error:** Authorization update failure
  - **Probable Cause:** The connector could not apply the authorization changes, possibly due to system incompatibilities or network issues.
  - **Solution:** Check the system connector logs for specific errors and ensure the target system is compatible with authorization updates. Confirm network connectivity between the Pathlock Cloud Platform and the target system.