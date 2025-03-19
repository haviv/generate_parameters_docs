# ActivateUser

**Category:** User Management

**Description:** The `ActivateUser` action automates the process of re-enabling a previously disabled or new user account in the systems managed by Pathlock Cloud. This entails potentially unlocking the account, resetting the user's password, applying or updating the user's parameters such as roles and authorizations based on predefined workflows, setting expiration dates for the user, and, if necessary, removing outdated authorizations before applying new ones. The action utilizes the system’s workflow engine to execute these tasks in a sequenced manner, ensuring that each step is logged for auditing purposes.

**Parameters:**
- Basic:
    - Name: `ActivateUser_Username`
    - Description: Username of the account to be activated. It is used to locate the user in the database to perform the activation steps.
    - Default value: None
    - Mandatory: No

    - Name: `ActivateUser_RunOnRequestUser`
    - Description: A boolean parameter that determines if the action should run on the user who requested the action, primarily used when `ActivateUser_Username` is not provided.
    - Default value: False
    - Mandatory: No

- Advanced:
    - Name: `ActivateUser_OverrideUserRecord`
    - Description: Determines if the user record should be overridden during activation. This is particularly useful when activating a user who does not meet the standard validity checks.
    - Default value: False
    - Mandatory: No

    - Name: `ActivateUser_RemoveRolesForInvalidUser`
    - Description: Specifies if roles should be removed for a user considered invalid before re-applying authorization.
    - Default value: None
    - Mandatory: No

    - Name: `DisableADExpirePasswordNow`
    - Description: A flag to determine whether to disable the AD policy for password expiration for the newly set password.
    - Default value: False
    - Mandatory: No

**Business impact:** Streamlining the process of user activation significantly impacts an organization by reducing the administrative burden on IT staff, ensuring rapid access for users to critical systems and reducing downtime. Automating the activation process enhances compliance with security policies by enforcing consistent application of access controls and ensuring that only authorized users gain access to sensitive systems and information.

**Example of usage:** To activate a user whose account has been previously suspended, a workflow could be initiated with the `ActivateUser` action. By providing the username as a parameter, the system could automatically unlock the user's account, reset the password according to the policy, reapply necessary authorizations and roles, and update the user's parameters to reflect the current access needs.

**Prerequisites:** The executing user must have sufficient permissions to modify user accounts, including password resets, role management, and authorization updates. Additionally, the database should be accessible, and the specified user must exist unless the action is set to run on the requester.

**Error Handling and Troubleshooting:**
- Common error scenarios include an inability to find the specified user, failure to reset the password due to policy restrictions, or errors in applying authorizations.
- Probable causes could be incorrect username input, insufficient permissions for the executing user, or misconfiguration of role definitions.
- Recommended solutions include verifying the input parameters for accuracy, ensuring the executing user has adequate permissions, and reviewing role and authorization configurations for consistency with the current policy. In the event of persistent errors, consult the system logs for specific error messages that can aid in diagnosing the issue.