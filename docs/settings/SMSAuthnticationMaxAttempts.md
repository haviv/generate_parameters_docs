# SMS Authentication Max Attempts

**Technical Name:** SMSAuthnticationMaxAttempts

**Category:** Security

**Default Value:** 

**Impact Level:** High

**Description:** This parameter defines the maximum number of attempts a user can make when trying to authenticate via SMS. Once this limit is reached, the user's ability to authenticate via SMS will be temporarily suspended to prevent brute force attacks.

**Business Impact:** Setting the SMS Authentication Max Attempts parameter appropriately ensures that unauthorized access via SMS authentication is minimized, protecting sensitive business data and systems from potential security breaches. It supports compliance with security policies and regulations by limiting the number of authentication attempts.

**Technical Impact when configured:** Configuring this parameter impacts user authentication flow by defining a threshold for how many times a user can incorrectly enter an SMS authentication code before being locked out. It directly influences security protocols around SMS-based two-factor authentication (2FA), enhancing the overall security posture of the system.

**Examples Scenario:** A company implements a policy where users must use SMS-based 2FA to access its Pathlock GRC platform. To prevent unauthorized access through guesswork, the company sets the SMS Authentication Max Attempts to 3. After 3 unsuccessful attempts, an employee would be temporarily unable to authenticate via SMS, thus requiring intervention from the security team to ensure legitimate access attempts and determine if the account is targeted by attackers.

**Related Settings:** SMSAuthnitcatorCode

**Best Practices:** configure when implementing SMS-based two-factor authentication to enhance security. Avoid setting this parameter too high, as it may allow attackers more attempts to guess the code; avoid setting it too low, as it could lock out legitimate users too quickly.