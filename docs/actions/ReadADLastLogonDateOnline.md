# ReadADLastLogonDateOnline

**Category:** User Management

**Description:** The ReadADLastLogonDateOnline action retrieves the most recent logon date for a specific user from Active Directory. It leverages an Active Directory Connector to access logon information across multiple Domain Controllers (DCs), identifying the most recent logon instance. This action is crucial for monitoring user activity, identifying inactive accounts, and enhancing security protocols by tracking user access patterns. Upon execution, it updates a user's record with the latest logon date and generates a custom output based on a specified template.

**Parameters:**
- Basic:
  - Name: OutputTemplate
  - Description: This is the template string for formatting the output of the action. It can include placeholders like `$$LastLogon$$`, `$$DC$$` for the last logon date and the domain controller, respectively. This parameter allows for customizable outputs depending on the administrator's needs, enabling easy integration with reports or user notifications.
  - Default value: "Last logon is: $$LastLogon$$ , on DC: $$DC$$"
  - Mandatory: No

**Business impact:** Implementing the ReadADLastLogonDateOnline action within Pathlock Cloud significantly enhances the visibility of user activities across enterprise systems. By accurately tracking the last logon dates, businesses can improve their security posture through detecting and managing stale or potentially compromised accounts. Additionally, this action supports compliance with various regulatory standards that mandate strict control and auditing of user access logs. 

**Example of usage:** 
An administrator needs to audit user activities within the organization's network. By executing the ReadADLastLogonDateOnline action, they can quickly identify users who have not logged in for an extended period, potentially flagging those accounts for further investigation or deactivation to reduce security risks.

**Prerequisites:** 
1. The user executing this action must have administrative privileges in the Pathlock Cloud platform.
2. An active link with the enterprise's Active Directory system must be configured correctly in Pathlock Cloud.
3. Necessary permissions to query user logon data from Active Directory.

**Error Handling and Troubleshooting:**
- Error: "User not found for the provided SystemId."
  - Cause: The specified SystemId does not match any users in the current context.
  - Solution: Verify the SystemId parameter corresponds to a valid user in the system.
  
- Error: "Cannot connect to the Active Directory."
  - Cause: There could be an issue with the Active Directory Connector or network connectivity.
  - Solution: Check the connectivity between Pathlock Cloud and the Active Directory system. Ensure the Active Directory Connector is set up correctly and operational.

- Error: "Failed to update the user logon data."
  - Cause: This could be due to permission issues or a problem accessing the database.
  - Solution: Ensure the executing user has the necessary permissions to update records in the data store. Check the database connectivity and health.