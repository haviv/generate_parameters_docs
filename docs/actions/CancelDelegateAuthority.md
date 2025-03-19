Action Name: CancelDelegateAuthority

**Category:** User Management

**Description:**

The CancelDelegateAuthority action is designed to revoke previously granted delegations within the Pathlock Cloud's workflow engine, specifically around approval groups. This action allows for the removal of a user's delegated authority from specific workflow approval groups. The typical flow involves identifying the user (delegate) whose authority is to be revoked, finding the approval groups they were delegated to by the requester, and ensuring that such delegations are validly removed. This process is crucial for maintaining the integrity and security of approval processes within the platform.

**Parameters:**

- Basic:
  - Name: parameters
  - Description: This parameter contains all the necessary information for identifying the requester, origin user, and the username of the delegate whose authority is being revoked. It is used throughout the action to fetch user details and relevant approval group information.
  - Default value: None
  - Mandatory: Yes

**Business impact:**

Revoking delegated authority through the CancelDelegateAuthority action ensures that only currently authorized users have access to sensitive operations and decisions within the system. It directly impacts the security posture by preventing unauthorized actions and mitigates any associated risks with inappropriate access. This sustains the integrity of the workflow's approval processes, aligning with compliance requirements and enforcing proper governance within the system.

**Example of usage:**

Consider a scenario where an employee, previously assigned as a delegate for certain approval groups, leaves the department or the company. To maintain security and proper control, the CancelDelegateAuthority action can be used to revoke the delegations efficiently. Invocation of this action would involve passing relevant user details to identify and cancel the delegated authority appropriately.

**Prerequisites:**

- The user initiating the CancelDelegateAuthority action must have administrative privileges or sufficient permissions to modify delegation settings.
- The delegate (user to remove) must have been previously granted delegations that can be revoked.

**Error Handling and Troubleshooting:**

- If the action fails to revoke delegations, check if the input parameters accurately identify the delegate and the requester. Incorrect or missing information can lead to failure.
- Ensure that the delegate has active delegations within the specified approval groups. Attempting to cancel non-existent delegations will not impact the system.
- Database submission errors should be examined in the context of system health and connectivity. Check the system logs for specific exception details provided by the Logger.SaveExceptionToLog method for troubleshooting.