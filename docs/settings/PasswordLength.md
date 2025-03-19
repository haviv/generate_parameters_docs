# Password Length

**Technical Name:** PasswordLength  
**Category:** Security  
**Default Value:** Varies (based on system configuration)  
**Impact Level:** High  

## Description
The `PasswordLength` parameter defines the minimum and maximum length of passwords created within the Pathlock Cloud GRC platform. This parameter is crucial for enforcing password security policies across user accounts, ensuring that passwords are of sufficient complexity and length to protect against unauthorized access.

## Business Impact
Setting an appropriate `PasswordLength` directly influences the security posture of an organization's IT environment. Longer passwords are generally more secure, reducing the risk of brute force attacks and unauthorized access to sensitive information. This, in turn, aids in compliance with various regulatory requirements that mandate specific standards for password security.

## Technical Impact when configured
- **Enhanced Security:** Enforcing a minimum password length ensures that users create passwords that are harder to guess or crack.
- **Compliance:** Helps organizations meet security standards and compliance requirements that specify minimum password lengths.
- **User Management:** Affects how user passwords are generated and changed, impacting both automated system processes and manual user actions.

## Examples Scenario
- **Scenario:** An organization must comply with the PCI DSS requirements, which specify that passwords must be at least 7 characters long. By setting the `PasswordLength` parameter to a minimum of 7, the organization ensures that all user passwords meet this requirement, thereby maintaining PCI DSS compliance.

## Related Settings
- PasswordComplexity
- PasswordExpirationPeriod
- PasswordHistory

## Applicable Workflow Actions
- ChangeUserPassword
- CreateNewUser

## Best Practices
- **Configure when:** Establishing or updating security policies related to user authentication and access control. It is recommended to set this parameter at the onset of using the Pathlock platform to ensure all user accounts are created with secure passwords from the start.
- **Avoid when:** There is no specific scenario where you should avoid configuring `PasswordLength`, as it is a fundamental security measure. However, avoid setting it to a value that might be considered too lenient or too restrictive without considering the usability impact and user compliance.

## Context
This parameter is found in workflow actions related to changing user passwords and creating new user accounts. It is instrumental in ensuring that the passwords generated or updated through these processes meet the organization's security requirements.