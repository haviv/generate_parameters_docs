# NewUserAccountPassword Parameter Documentation

## Category
- Security and User Management

## Default Value
- Not explicitly set in the provided code references.

## Impact Level
- High

## Description
The `NewUserAccountPassword` parameter is used to define the password for new user accounts created within the Pathlock Cloud GRC platform. This parameter is crucial for the initial access security of new users.

## Business Impact
Setting up a secure `NewUserAccountPassword` is fundamental to ensuring that new accounts are protected against unauthorized access from the moment they are created. A strong default password helps in mitigating the risk of security breaches that can lead to data theft, compliance violations, and loss of customer trust.

## Technical Impact when configured
1. **Security Enhancement**: Enforces the application of a strong password policy right from the account creation phase.
2. **Automation Support**: Facilitates the automated creation of user accounts with a predetermined level of password security.
3. **Audit and Compliance**: Supports compliance with security standards and regulations that mandate the use of strong authentication measures for new user accounts.

## Examples Scenario
- **New Employee Onboarding**: When a new employee joins the company, the Pathlock Cloud GRC system automatically generates a user account with a secure password defined by the `NewUserAccountPassword` parameter. This password is then sent via SMS to the employee's mobile number, ensuring that only the intended user gains initial access.

## Related Settings
- `SMSNewUserAccountPassword`: Template for the SMS message that contains the new user account password.
- `SMSFileNameTemplate`: Template for storing SMS message content in a file, relevant when SMS cannot be directly sent.
- `SmsSenderProvider`: Specifies the service provider used for sending the SMS.

## Best Practices
- **Configure When**: It is recommended to configure the `NewUserAccountPassword` parameter during the initial setup of the Pathlock Cloud GRC platform to establish a secure default password policy.
- **Avoid When**: Refrain from using simple or predictable passwords. Avoid setting the parameter to a default that could be easily guessed or is commonly used.

Considering the critical role of `NewUserAccountPassword` in securing new user accounts, it is imperative to adopt a stringent password policy that incorporates a mix of letters, numbers, and special characters. Review and update the password policy periodically to align with evolving security standards and threats.