# LockUser

**Category:** User Management

**Description:** 

The `LockUser` action is designed to facilitate user account lockouts across multiple systems, particularly aimed at enhancing security and compliance by preventing unauthorized access. This action verifies the current lock status of a user account and, based on predefined conditions, performs a lockout on the user account if it hasn't already been locked. The workflow encompasses verifying user status, initiating the lockout process for users identified within the system, and providing a fallback mechanism to lock users based on username in cases where direct user identification fails due to synchronization issues.

**Parameters:** 

- **Basic Parameters:**
  - **Name:** RunLockAsFallbackBasedOnSameUsername
  - **Description:** A boolean parameter that enables a fallback locking mechanism for cases where the intended user cannot be found due to potential synchronization discrepancies. This parameter ensures that, should direct user identification fail, the system attempts to lock a user by matching the username. It's a crucial parameter in maintaining the integrity of the lockout process by providing an alternative method to enforce security policies.
  - **Default value:** False
  - **Mandatory:** No
- **Advanced Parameters:**
  - **Name:** LockReason
  - **Description:** Although not explicitly shown in the provided code snippet, referencing common practices suggests this parameter would allow specifying a reason for the user lockout. This is crucial for audit trails and understanding the context behind security actions.
  - **Default value:** N/A
  - **Mandatory:** Yes

**Business impact:**

Implementing the `LockUser` action within Pathlock Cloud workflows directly supports compliance with security policies by ensuring that unauthorized access to sensitive systems and data is prevented. By automating the lockout process, organizations can swiftly respond to security incidents or compliance requirements, significantly reducing the risk of data breaches. The fallback mechanism also ensures that even in cases of data synchronization issues, user access can be securely managed.

**Example of usage:**

Suppose an organization needs to immediately lock out a user account due to suspicious activity. The workflow engine can be configured to automatically trigger the `LockUser` action based on alerts from monitoring systems. By setting the `RunLockAsFallbackBasedOnSameUsername` to true, the organization ensures that even if the user's account is not correctly synchronized across systems, the lockout can still be executed, bolstering their security posture.

**Prerequisites:**

- Appropriate permissions to execute lockout actions on user accounts.
- The `LockUser` action must be correctly configured within the Pathlock Cloud platform’s workflow engine.
- Necessary synchronizations and system connectors must be established and functioning correctly for accurate user identification and lockout.

**Error Handling and Troubleshooting:**

- **Error:** Failure to lock user account.
  - **Probable Cause:** The user account cannot be found due to synchronization issues.
  - **Solution:** Ensure that the `RunLockAsFallbackBasedOnSameUsername` parameter is enabled or investigate and resolve the synchronization discrepancies.
  
- **Error:** Lock action fails without throwing an error.
  - **Probable Cause:** Insufficient permissions or system connector misconfiguration.
  - **Solution:** Verify that the user or service account executing the workflow has adequate permissions and that the system connectors are correctly configured.