# CreateNewUserUpdateImmediately Parameter Documentation

## Category
New Employees Creation

## Default Value
The default behavior of the `CreateNewUserUpdateImmediately` parameter is not explicitly stated in the provided code. It depends on the configuration in `CommonSettings.Default`.

## Impact Level
Medium

## Description
The `CreateNewUserUpdateImmediately` parameter controls whether new user information is immediately refreshed and applied in the system upon user creation or tied to a specific event or condition. This immediate update is crucial in scenarios where timely access and user data accuracy are critical, ensuring that new users have the correct permissions, roles, and access levels as soon as they are added to the Pathlock GRC platform.

## Business Impact
- Ensures that new employees can immediately start working with the necessary system access without delays.
- Minimizes the risk of access-related errors or security vulnerabilities that can occur if new users are not updated in the system in a timely manner.
- Facilitates smoother onboarding experiences, contributing to operational efficiency and employee satisfaction.

## Technical Impact when configured
- Immediate propagation of user rights and roles, reducing the latency between user creation and access granting.
- Potential increased load on the system during user creation due to additional processing requirements.
- Reduction in administrative overhead by automating the immediate update process, rather than requiring manual intervention.

## Examples Scenario
1. **Immediate Access for New Users**: When `CreateNewUserUpdateImmediately` is enabled, a new user added to the Pathlock GRC platform for compliance monitoring will have immediate access to their required tools and resources, facilitating a seamless start to their role.
2. **Compliance Requirements**: In a scenario where compliance dictates that users must have access reviewed and applied as soon as they are onboarded, enabling this setting ensures the organization meets these requirements without manual follow-up.

## Related Settings
- `ChangeInstanceUserForSystem`: Toggles whether the user instance should be changed for the system, impacting the refresh behavior.
- `autoRefreshUserInformation`: Toggles automatic refreshing of user information, which can work in tandem with `CreateNewUserUpdateImmediately` for enhanced user data synchronization.

## Best Practices
- **Configure when**:
  - Immediate system access for new users is critical.
  - Compliance and security policies require up-to-date user information and permissions.
- **Avoid when**:
  - System resources are limited, and the additional processing load can cause performance issues.
  - Immediate access is not necessary, and delayed updates are preferable for batch processing or review.

This parameter is part of the Pathlock Cloud GRC platform's ecosystem, emphasizing the significance of timely user information updates in maintaining system security, compliance, and operational efficiency.