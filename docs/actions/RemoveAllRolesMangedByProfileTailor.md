# Remove All Roles Managed By Profile Tailor

**Category:** User Management

**Description:**  
This action is designed to automatically remove all roles from a user that are managed by the Profile Tailor system within the Pathlock Cloud identity and GRC platform. The primary flow of this action involves identifying the user's current roles, determining if each role is managed by Profile Tailor, and if so, removing the role. Logging is implemented to record the action's progress and outcomes, ensuring transparent audit trails and facilitating troubleshooting.

**Parameters:**  
- **Basic Parameters:**
    - Name: `username`
    - Description: The username of the individual from whom roles will be removed. If not provided explicitly, it is retrieved from the user object fetched within the method.
    - Default value: `null`
    - Mandatory: no

- **Advanced Parameters:**
    - Name: `allowedRoles`
    - Description: An array of allowed roles fetched from various system configurations which signifies roles relevant to the workflow. This array is instrumental in determining whether a user's role should be removed or retained.
    - Default value: dynamically fetched array
    - Mandatory: no

**Business impact:**  
Executing this action directly impacts user access rights within the system. By automating the removal of managed roles for individuals, companies can ensure that access rights are correctly managed and mitigate risks related to unauthorized access or improper segregation of duties (SOD). It supports governance, risk management, and compliance (GRC) strategies by maintaining strict control over user roles and permissions.

**Example of usage:**  
To use this action, a workflow would be initiated for a user whose roles need reassessment or removal due to changes in their job functions or after an internal audit reveals unauthorized access issues. This action ensures that only relevant and authorized roles are assigned to the user, aligning with current access control policies and compliance requirements.

**Prerequisites:**  
- The user executing this action must have permissions to modify user roles within the Pathlock Cloud system.
- A valid WorkflowInstance and user object need to be provided to the action for role assessment and removal.

**Error Handling and Troubleshooting:**  
- **Error:** Roles not removed  
    - **Cause:** This could be due to a lack of permissions to remove roles for a user or system connectivity issues.
    - **Solution:** Verify the executing user's permissions and ensure system connectivity.

- **Error:** Invalid username or user not found  
    - **Cause:** The username provided does not match any user in the system, or no username is provided, and the system fails to retrieve the user object.
    - **Solution:** Verify that a correct and existing username is provided. If relying on automatic user fetching, ensure that the user object is correctly initialized and populated before the action execution.

- **Error:** Action fails to identify managed roles  
    - **Cause:** This could be due to an issue with fetching or processing the allowedRoles array, possibly a configuration error or a system issue.
    - **Solution:** Verify system configurations and allowedRoles fetching logic. Check for any recent changes that may have disrupted this process.