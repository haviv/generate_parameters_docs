# UnlockByIncorrectLogonsOnly

**Category:** User Management

**Description:**

The `UnlockByIncorrectLogonsOnly` action is designed to automate the process of unlocking user accounts that have been locked due to incorrect login attempts. This action specifically targets scenarios within SAP systems managed by the BaseSapWASConnector, ensuring that users who have been unintentionally locked out can regain access in an efficient manner. The action is initiated by verifying the user's lock status and then proceeding with the unlock process if the user has been locked out due to incorrect logon attempts.

**Parameters:**

- **Basic Parameters:**
    - Name: SystemId
    - Description: This parameter identifies the specific system (e.g., SAP instance) the user belongs to. It is used to initialize the context for the ProfileTailor system connector, facilitating the correct application of the unlock action within the targeted system environment.
    - Default value: N/A
    - Mandatory: Yes

**Business impact:**

Implementing this action within the Pathlock cloud platform significantly minimizes downtime for users encountering lockouts due to authentication errors. By streamlining the unlock process, organizations can maintain higher levels of productivity and ensure that access control mechanisms do not inadvertently impede user operations. Moreover, it reinforces security policies by automating a critical aspect of user account management, specifically within SAP environments.

**Example of usage:**

A common usage scenario would involve a user unsuccessfully attempting to log into their SAP account multiple times, resulting in their account being locked. The system administrator can configure a workflow within the Pathlock cloud platform that includes the `UnlockByIncorrectLogonsOnly` action. When triggered, this action would automatically unlock the user's account, provided the lockout was due to incorrect logon attempts, thus allowing the user to attempt login again or reset their password without requiring direct administrative intervention.

**Prerequisites:**

- The user must have a valid account within an SAP system managed by BaseSapWASConnector.
- Proper configuration and connectivity between the Pathlock cloud platform and the SAP system must be established.

**Error Handling and Troubleshooting:**

- **Error Scenario:** The user's account remains locked despite the action being triggered.
    - **Probable Cause:** The account may be locked due to reasons other than incorrect logon attempts, or the system might not be responding as expected.
    - **Solution:** Verify the lock reason via the SAP administrative console. If the issue persists, check the integration logs between Pathlock cloud and the SAP system for potential connectivity or configuration issues.
  
- **Error Scenario:** The action fails to execute, returning a null verification response.
    - **Probable Cause:** There could be an issue with the system ID provided or a connection issue with the SAP system.
    - **Solution:** Confirm the system ID's accuracy and ensure there are no connectivity issues affecting communication between the Pathlock cloud platform and the SAP system.