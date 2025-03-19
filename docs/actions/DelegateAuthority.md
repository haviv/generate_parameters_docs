# DelegateAuthority

**Category:** User Management

**Description:** 

The DelegateAuthority action is designed to temporarily delegate a user's approval authority to another user within the Pathlock Cloud system. This action is particularly useful in scenarios where a primary approver is unavailable (e.g., due to vacation or leave) and a temporary substitute needs to be granted the approval powers to ensure business continuity. The delegation involves adding a substitute user to the approval groups of the original approver for a specified period. This action automates the process, seamlessly transferring responsibilities without affecting the workflow's integrity or security.

**Parameters:**

- Basic:
    1. Name: originalUser
       Description: The username of the original approver whose authority is being delegated. This parameter identifies the user from whom the approval authority is transferred.
       Default value: N/A
       Mandatory: no
    2. Name: username
       Description: The username of the substitute approver to whom the authority is being delegated. This parameter defines the recipient of the temporary approval authority.
       Default value: N/A
       Mandatory: yes

- Advanced:
    1. Name: fromDate
       Description: The start date from which the delegation will be effective. This parameter marks the beginning of the substitute's authority period.
       Default value: Current date
       Mandatory: no
    2. Name: toDate
       Description: The end date until which the delegation remains effective. This parameter designates when the substitute's temporary authority will expire.
       Default value: N/A
       Mandatory: no

**Business impact:** 

Delegating approval authority ensures that there are no delays in the approval processes during an original approver's absence, maintaining operational efficiency. It supports adherence to compliance requirements by ensuring that proper approvals are in place, thereby mitigating any risk associated with unauthorized access or actions. This feature enhances the flexibility and resilience of the workflow system by allowing organizations to adapt to unforeseen circumstances without compromising on security or operational performance.

**Example of usage:**

A scenario where "JohnDoe," the original approver, is going on vacation and "JaneDoe" will act as the substitute approver during his absence:

- The administrator executes the DelegateAuthority action.
- "originalUser" is set as "JohnDoe".
- "username" is set as "JaneDoe".
- "fromDate" and "toDate" are set according to JohnDoe's vacation period.

This will add JaneDoe to JohnDoe's approval groups for the specified period, allowing her to perform the necessary approvals in his stead.

**Prerequisites:**

1. The executing user must have administrative privileges to perform delegation actions.
2. Both the original and substitute approvers must be registered users in the Pathlock Cloud system.
3. Appropriate groups and permissions need to be pre-defined to ensure accurate delegation.

**Error Handling and Troubleshooting:**

**1. Error Scenario:** Failure to delegate authority due to the absence of the substitute user in the system.
- **Probable Cause:** The username provided for the substitute approver does not match any user in the system.
- **Solution:** Ensure the substitute's username is correctly spelled and registered in the Pathlock Cloud system.

**2. Error Scenario:** Delegation not effective within the specified period.
- **Probable Cause:** Incorrect dates provided for the delegation period (e.g., "toDate" is earlier than "fromDate").
- **Solution:** Verify and correct the fromDate and toDate parameters to reflect the intended delegation period.

**3. Error Scenario:** Unable to record delegation action.
- **Probable Cause:** Database connection issues or write permissions problems.
- **Solution:** Check the database connection and ensure the Pathlock Cloud system has appropriate permissions to make changes. Review system logs for specific error messages and contact technical support if the issue persists.