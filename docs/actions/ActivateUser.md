# ActivateUser

**Category:** User Management

**Description:** 

The `ActivateUser` action is designed to manage and update the status of user accounts within the Pathlock Cloud identity and GRC platform. This action automates the process of activating a user, including unlocking their account, setting parameters, resetting passwords, setting expiration dates, and applying authorizations based on predefined or dynamically determined criteria. It leverages a workflow engine to facilitate self-service requests and automate manual processes related to user account management. The action checks if a user exists based on provided credentials and parameters, then performs a series of operations to ensure the account is activated and configured according to business rules and compliance policies.

**Parameters:** 

Basic:
- Name: `ActivateUser_Username`
  Description: The username of the account to be activated. Used to identify the user in the system.
  Default value: N/A
  Mandatory: No

- Name: `ActivateUser_RunOnRequestUser`
  Description: A boolean parameter determining if the action should be performed on the user making the request.
  Default value: `false`
  Mandatory: No

Advanced:
- Name: `ActivateUser_OverrideUserRecord`
  Description: Determines if the user record should be overridden during activation. It is utilized when a user needs to be forcibly updated or reconfigured.
  Default value: `false`
  Mandatory: No

- Name: `DisableADExpirePasswordNow`
  Description: Disables immediate password expiration in Active Directory, allowing for a grace period before the user must change their password.
  Default value: `false`
  Mandatory: No

- Name: `ActivateUser_RemoveRolesForInvalidUser`
  Description: A parameter indicating whether roles should be removed from an invalid user during activation. This is primarily used in compliance scenarios where access must be tightly controlled.
  Default value: `false`
  Mandatory: No

**Business impact:** 

Activating users through the `ActivateUser` action directly impacts operational efficiency by automating and streamlining the process of enabling user access to critical systems. It supports compliance with internal and external policies by ensuring that user accounts are correctly configured and authorized before being activated. This reduces the risk of unauthorized access and enhances the overall security posture of the organization.

**Example of usage:** 

A common scenario involves activating a new employee's user account. The workflow would be initiated after the new employee is added to the company's system, triggering the `ActivateUser` action to unlock the account, reset the password to a temporary one, set parameters as defined by company policy, and apply the necessary authorizations for the employee's role.

**Prerequisites:** 

- The user or system initiating the action must have administrative privileges or equivalent permissions.
- The user account to be activated must exist in the Pathlock Cloud database, even if it is in an inactive or locked state.

**Error Handling and Troubleshooting:** 

- If the user cannot be found or is not specified, the action will log an error indicating that the username is required.
- Errors during the password reset process, including failure to meet complexity requirements or system connection issues, will be logged with a specific message detailing the cause of the failure.
- In case of failure to apply authorizations or any other action, the system will log the detailed error message, and it is recommended to review these messages for troubleshooting.

For troubleshooting purposes, ensuring that all parameters are correctly set and that the system has connectivity with any external systems (e.g., Active Directory) is essential. It is also recommended to verify that the user account is correctly configured within the system before attempting activation.