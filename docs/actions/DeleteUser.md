Action name: DeleteUser

**Category:** User Management

**Description:** 

The DeleteUser action in the Pathlock Cloud Workflow Engine is designed to remove a user from the system securely and update the workflow instance accordingly. Upon invocation, this action performs a series of checks to ensure compliance with security protocols. The workflow instance and associated user information are retrieved, followed by a system code validation to ensure the action is executed in the correct context. It verifies that the user being deleted is not essential for the ProfileTailor Dynamics (PTD) operational integrity. If the checks pass, the user is deleted from the ProvisionService. Additionally, if the workflow instance contains an "OriginalUserId", the action updates the instance with the user corresponding to this ID. Logs are maintained for error tracking, especially in scenarios where an attempt is made to delete a prohibited user.

**Parameters:**

  - Basic Parameters:
    - Name: SystemId
      Description: The identifier for the system to which the user belongs. This parameter ensures that the deletion is executed within the correct system context.
      Default value: Derived from the user’s systemId.
      Mandatory: Yes
    - Name: SapUserName
      Description: The username of the user to be deleted. It's utilized to prevent the deletion of the system user, ensuring the integrity of the system’s operational user.
      Default value: Extracted from ProfileTailorContext.
      Mandatory: Yes
  
  - Advanced Parameters:
    - Name: OriginalUserId
      Description: An optional ID to revert the user details in the workflow instance after a deletion is performed. This allows for maintaining historical user data within the workflow context.
      Default value: None
      Mandatory: No

**Business impact:** 

Deleting a user from the system is a critical operation that impacts system access, security, and regulatory compliance. It ensures that only authorized personnel have access to the system, preventing unauthorized access and potential security breaches. Efficient management of user lifecycles contributes to maintaining operational integrity and compliance with internal and external policies.

**Example of usage:** 

A scenario where an employee leaves the company, and their system access needs to be revoked to maintain security protocols. The DeleteUser action is executed within a workflow to remove the user's access systematically and update the company's records accurately.

**Prerequisites:** 

The user executing the DeleteUser action must have administrative privileges to manage users within the system. Additionally, the workflow where this action is integrated should have access to the necessary user and system ID data to execute correctly.

**Error Handling and Troubleshooting:** 

- **Error:** "system user cannot be deleted"
  - **Cause:** Attempting to delete a user essential for the operation of the system.
  - **Solution:** Ensure that the user being deleted is not required for any system operations. Review the user’s role and dependencies before attempting to delete.
  
- **General Troubleshooting:**
  - Verify the SystemId and SapUserName parameters are correct and correspond to the user intended for deletion.
  - Check the workflow instance for integrity and proper configuration, ensuring that the OriginalUserId, if provided, is accurate and relevant.
  - Consult the system logs for any errors or warnings that may provide more context on the failure.
