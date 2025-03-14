# AuthorizationCertificationByActivitiesIncludeRoleName Parameter Documentation

## Category
Security and Compliance

## Default Value
False

## Impact Level
Moderate

## Description
This parameter controls whether role names and descriptions are included in the authorization certification reports by activities. When enabled, it augments the certification data with role names and descriptions associated with each activity, providing more context for auditors and managers during the certification process.

## Business Impact
Enabling this setting enhances the understanding of user permissions by mapping activities directly to their corresponding roles. It aids in identifying excessive permissions or inaccuracies in role assignments, critical for maintaining the principle of least privilege and complying with internal and external audit requirements.

## Technical Impact when configured
- Enhances report granularity by adding role names and descriptions to the authorization certification reports.
- May slightly increase the time required to generate reports due to the additional data processing.
- Improves auditability and traceability of permissions, aiding in compliance efforts.

## Examples Scenario
Consider a scenario where an organization is undergoing a security audit, and auditors require detailed information on user permissions. By enabling `AuthorizationCertificationByActivitiesIncludeRoleName`, the authorization certification reports will include role names and descriptions alongside user activities. This addition provides auditors with a clearer understanding of each user's permissions, simplifying the audit process.

## Related Settings
- `SoxGroups` parameter to filter activities based on specific compliance groups.
- Custom field additions in reports, such as "RoleDescription".

## Best Practices
- **Configure when**: Detailed role information is necessary for understanding the context of user permissions during certification processes. This is especially relevant for organizations with complex role structures or those subject to stringent compliance requirements.
- **Avoid when**: The additional details are not required for certification purposes or might lead to information overload for reviewers. Also, consider avoiding it if system performance or report generation time is a critical concern.

## Context
The `AuthorizationCertificationByActivitiesIncludeRoleName` parameter is a part of the CommonSettings within the PathlockGRC suite, specifically used within the Authorization Review Providers to tailor the detail level of authorization certification reports. Its primary use is in enhancing the comprehensiveness of authorization reviews by including role-based data.