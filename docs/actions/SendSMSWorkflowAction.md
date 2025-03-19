# SendSMSWorkflowAction

**Category:** User Management

**Description:** The SendSMSWorkflowAction is designed to automate the process of sending SMS messages to users, primarily for the purpose of notifications, verifications, or any critical communication via mobile text messages. This action retrieves a specified user's mobile number, either from the provided parameters or from the user's profile, and sends an SMS message to that number. The underlying workflow supports conditional retrieval of user mobile numbers, ensuring messages are delivered even when initial parameters are insufficient, thereby improving the robustness of communication strategies within the system.

**Parameters:**

- Basic:
    - Name: SmsMessage
    - Description: The body of the SMS message to be sent. This is the actual text that will be received by the user's mobile device.
    - Default value: N/A
    - Mandatory: yes

    - Name: MobileNumber
    - Description: The target mobile number for the SMS. If not provided, the system will attempt to retrieve the user's mobile number associated with their profile in the system.
    - Default value: N/A
    - Mandatory: no

**Business impact:** This action directly impacts how effectively the company communicates with its users, particularly in scenarios requiring immediate attention or action from the user. By leveraging direct SMS communication, the system ensures higher engagement rates compared to other forms of notification. This is particularly crucial for timely matters such as access verifications, risk alerts, or compliance notifications, thus reinforcing the security and operational integrity of the platform.

**Example of usage:** 

To send a verification code via SMS for two-factor authentication (2FA) setup, one could use the SendSMSWorkflowAction with the parameters set as follows: `SmsMessage` to "Your verification code is: 123456", and `MobileNumber` to "+1234567890". If the mobile number is not known by the caller, the action will attempt to retrieve it based on the user's profile.

**Prerequisites:** The user executing this action needs to have the rights to initiate workflow actions and access user information within the system. Additionally, there must be a functional SMS sending service configured and accessible to the workflow engine.

**Error Handling and Troubleshooting:** 

- If an SMS fails to send, check the following:
    - Ensure the `MobileNumber` provided is valid and in the correct international format.
    - Verify the SMS service connectivity and availability within the system's network.
    - Confirm that sufficient permissions and API limits for the SMS sending service are not exceeded.

- Missing or invalid `SmsMessage` parameter will result in an inability to perform the action. Always validate the input parameters before initiating the action.

- In case the mobile number cannot be retrieved from the user profile, ensure that the user data is complete and up to date within the system. Missing information should be rectified at the source to avoid communication gaps.