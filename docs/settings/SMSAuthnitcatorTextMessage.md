# SMS Authenticator Text Message

**Technical Name:** SMSAuthnitcatorTextMessage

**Category:** Security

**Default Value:**

**Impact Level:** High

**Description:**

The SMS Authenticator Text Message parameter is utilized within the Pathlock Cloud GRC platform to facilitate secure user authentication by sending a text message to a user's mobile device. This parameter helps ensure that only authorized individuals can access sensitive information and perform critical operations within the platform.

**Business Impact:**

Configuring the SMS Authenticator Text Message correctly has a significant impact on the organization's security posture. It enhances the security of user authentication processes, thereby helping to protect against unauthorized access and potential data breaches. This parameter plays a crucial role in ensuring that access to the system is securely managed and that compliance with regulatory requirements related to user authentication is maintained.

**Technical Impact: when configured**

When configured, the SMS Authenticator Text Message parameter triggers the sending of a text message containing authentication details or codes to the user's registered mobile number. This serves as an additional layer of security beyond just the username and password, making it more difficult for unauthorized users to gain access.

**Examples Scenario:**

An example scenario where the SMS Authenticator Text Message parameter could be particularly useful is when an employee attempts to access the Pathlock GRC platform from an unrecognized device or location. In this scenario, in addition to entering their regular login credentials, they would also be required to enter a code that they receive via SMS on their registered mobile number, thus providing dual-factor authentication.

**Related Settings:**

- SmptClientPort: This setting might be utilized in conjunction with the SMS Authenticator Text Message parameter to define the port through which SMS notifications are sent.

**Best Practices:** 

- Configure when:
    - You want to enhance the security of your authentication process
    - You need to comply with regulatory requirements that mandate two-factor authentication

- Avoid when:
    - Users do not have mobile devices that can receive SMS messages
    - The organization operates in areas with unreliable mobile network coverage