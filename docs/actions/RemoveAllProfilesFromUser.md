Action Name: **RemoveAllProfilesFromUser**

**Category:** User Management

**Description:** 

The `RemoveAllProfilesFromUser` action is designed to streamline the process of revoking all SAP user profiles associated with a specific user within the system. This action is part of the workflow engine of Pathlock Cloud, allowing administrators or automated processes to efficiently manage user access and permissions within an organization's SAP environment. Upon invocation, this action retrieves the designated user's details based on the system ID provided; it then proceeds to remove all associated SAP profiles from that user, ensuring a comprehensive clearance of access rights. Following the removal of profiles, the system triggers an update to refresh the user's information, reflecting the changes in access rights and profiles.

**Parameters:**

Basic:
- Name: SystemId
- Description: Unique identifier for the system from which user profiles are to be removed. It is used to retrieve the user's details relevant to the current operation.
- Default value: None
- Mandatory: Yes

**Business impact:**

Employing the `RemoveAllProfilesFromUser` action is critical for maintaining secure and compliant user access within an organization's SAP system. It effectively addresses scenarios where a user's access rights need to be rapidly revoked either due to termination, role change, or other security and compliance requirements. This action aids in preventing unauthorized access and ensuring that the principle of least privilege is adhered to, thereby reducing the organization's risk exposure.

**Example of usage:**

An administrator wishes to revoke all SAP access from a user who is leaving the company. By deploying the `RemoveAllProfilesFromUser` action within a workflow, the administrator specifies the departing user's system ID. The action then ensures that all SAP profiles linked to the user are removed, and the user's information is updated to reflect these changes.

**Prerequisites:**

- Proper permissions to execute workflow actions within the Pathlock Cloud platform.
- Access rights to manipulate user profiles and permissions within the targeted SAP system.

**Error Handling and Troubleshooting:**

Error: User Not Found
- Cause: The specified `SystemId` does not match any user within the system.
- Solution: Verify the `SystemId` for correctness and ensure the user exists within the current system context.

Error: Access Denied
- Cause: The executing account does not have the necessary permissions to perform user profile removals.
- Solution: Ensure the account executing the action has adequate permissions within both the Pathlock Cloud platform and the SAP system.

For additional troubleshooting or detailed logging, refer to the Pathlock Cloud and SAP system logs, or contact Pathlock support for further assistance.