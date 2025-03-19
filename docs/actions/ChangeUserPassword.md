# ChangeUserPassword

**Category:** User Management

**Description:** This action automates the process of changing user passwords within the Pathlock Cloud environment. It caters to various scenarios such as unlocking user accounts, resetting passwords to a custom or randomly generated value, and sending the new password to the user via email or SMS. The action interprets inputs to verify user identity, unlock accounts, generate new passwords based on provided criteria or requested randomness, and notify the user through specified channels. It incorporates system-specific behavior to handle password changes in SapConnector or ActiveDirectory environments, ensuring compliance with organizational policies and external system requirements.

**Parameters:** 

- **Basic Parameters:**
    - Name: UnlockUser
      Description: Determines if the user's account should be unlocked during the password change process. It's assessed in the context of user account status within connected systems such as SAP or Active Directory.
      Default value: (none specified)
      Mandatory: No

    - Name: ResetPassword
      Description: Indicates whether the password should be reset. The action uses this parameter to decide on executing the password change logic.
      Default value: (none specified)
      Mandatory: No

    - Name: RandomPassword
      Description: If set to Yes, the system will generate a random password. It triggers a password generation flow that may include checks against defined rules for password complexity.
      Default value: (none specified)
      Mandatory: No

    - Name: new_password
      Description: Specifies a custom password. It is used when `RandomPassword` is not requested. Supports placeholders for semi-random elements.
      Default value: (none specified)
      Mandatory: No

    - Name: SendTemporaryPassowrdByMail
      Description: Determines if the new temporary password should be sent to the user's email. It conditions the flow for constructing and sending the email notification.
      Default value: (none specified)
      Mandatory: No

- **Advanced Parameters:**
    - Name: CustomSystemId
      Description: A system identifier overriding the default system for the password reset action. This parameter influences the system context initialization.
      Default value: (none specified)
      Mandatory: No

    - Name: VerifyUserByPhoneNumber
      Description: Enables verification of the user's identity via phone number before performing the password reset. It's part of safeguarding against unauthorized requests.
      Default value: (none specified)
      Mandatory: No

    - Name: SendTemporaryPassowrdBySMS
      Description: If Yes, sends the new password via SMS, using either a direct mobile number or one retrieved through system connectors.
      Default value: (none specified)
      Mandatory: No

**Business impact:** Executing this action securely manages password resets and account unlocks, directly impacting user access and security compliance. It aids in mitigating unauthorized access risks by ensuring only verified users can initiate password changes, while also supporting compliance by enforcing password policies. Timely and secure user notification via email or SMS enhances user experience and operational efficiency.

**Example of usage:** A scenario where a user's account has been locked due to multiple incorrect login attempts. The user requests a password reset through the self-service portal. By executing `ChangeUserPassword` with `UnlockUser` set to Yes and `ResetPassword` set to Yes, the user's account is unlocked, and a new password is generated and sent to their registered email.

**Prerequisites:** 
- The user must exist in the system connected to Pathlock Cloud (e.g., SAP, Active Directory).
- The executing agent must have sufficient permissions to alter user account statuses and issue password changes in the connected systems.
- Necessary email or SMS notification templates must be configured and available for use.

**Error Handling and Troubleshooting:** 
- Failure to change the password, possibly due to connection issues with the target system, will log an error message and might send a failure notification if configured.
- If user verification fails (e.g., incorrect phone number), the process will halt, and a relevant failure message will be set.
- Issues sending notifications (email or SMS) due to invalid templates or recipient details will result in logging the error detail for further administrative review.