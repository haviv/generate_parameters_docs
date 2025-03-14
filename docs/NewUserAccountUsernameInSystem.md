# NewUserAccountUsernameInSystem Parameter Documentation

## Category
New Employees Creation

## Default Value
Not applicable (N/A)

## Impact Level
Medium

## Description
The `NewUserAccountUsernameInSystem` parameter is used to specify the username of a new user account within a specified system. It forms part of the automated workflows for creating new user accounts across various systems as managed by the Pathlock Cloud GRC platform. This parameter is dynamically populated based on the system in question and the username assigned to the new user.

## Business Impact
Proper configuration and usage of this parameter directly influence the efficiency and reliability of onboarding new employees into an organization's IT ecosystem. It ensures that user accounts are correctly set up with appropriate usernames, facilitating smooth access to necessary systems and resources. This can significantly reduce the time it takes for new employees to become productive and mitigate the risk of access-related issues that can arise from incorrect account setup.

## Technical Impact when Configured
When `NewUserAccountUsernameInSystem` is correctly configured:
- New user accounts are automatically assigned usernames consistent with organizational naming conventions.
- Reduces manual intervention and human error in the account creation process.
- Enhances the security posture by ensuring that access rights and usernames are correctly aligned with organizational policies.

## Examples Scenario
Consider an organization that utilizes multiple systems (e.g., email, HR management system, and an internal communication platform). When a new employee is onboarded:
- The `NewUserAccountUsernameInSystem` parameter is utilized within the Pathlock Cloud GRC platform to specify the employee's username in each of these systems.
- For example, if the new employee's name is John Doe, the parameter could be configured to create usernames such as "jdoe" for the email system, "john.doe" for the HR management system, and "JDoe" for the internal communication platform.

## Related Settings
- `NewUserAccountPassword`: Configures the default password for new user accounts.

## Best Practices
- **Configure when**: Setting up automated workflows for creating new user accounts. Ensure that the chosen usernames align with the organization's naming conventions and policies.
- **Avoid when**: Usernames are to be manually assigned or when a system requires unique username configurations that cannot be standardized.

**Note**: The specific implementation and configuration details for `NewUserAccountUsernameInSystem` will vary depending on the organizational requirements and the technical environment. It is crucial to collaborate with IT security, HR, and system administrators to ensure that this parameter is optimally configured.