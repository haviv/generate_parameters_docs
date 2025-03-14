# Documentation for `AuthorizationCertificationHideIndirectRoleAssisgment`

## Category:
Security Configuration

## Default Value:
False

## Impact Level:
System-Wide

## Description:
The `AuthorizationCertificationHideIndirectRoleAssisgment` parameter is used to control the visibility of indirectly assigned roles during the authorization certification process. When enabled, it filters out roles that users have been granted indirectly through composite roles, focusing the certification process solely on directly assigned roles.

## Business Impact:
Enabling this parameter can streamline the authorization review process by focusing on directly assigned roles, potentially reducing the complexity and time required for certifiers to review and validate user access. It may enhance the clarity and relevance of the certification process, ensuring that emphasis is placed on explicit role assignments.

## Technical Impact:
When configured to `True`, this setting filters out indirect role assignments from the authorization certification process. This can lead to a more simplified and focused certification scope, where only direct role assignments are considered, potentially decreasing load times and improving the efficiency of the certification process due to fewer roles being processed.

## Example Scenario:
Imagine an organization with a complex role structure where users are granted access through a mixture of direct role assignments and indirect assignments via composite roles. By setting `AuthorizationCertificationHideIndirectRoleAssisgment` to `True`, during authorization certification, administrators and reviewers will only see the roles directly assigned to a user, omitting those inherited indirectly. This can significantly simplify the review process, especially in scenarios where the focus is on auditing direct permissions granted to users for compliance purposes.

## Related Settings:
- Composite Role Definition Settings
- Direct Role Assignment Visibility Settings

## Best Practices:
- **Configure when:** A streamlined review process is desired or when focus is needed on directly assigned roles for compliance or audit purposes. It is especially useful in complex environments where indirect role assignments might obscure the review process.
- **Avoid when:** A comprehensive view of all direct and indirect role assignments is required for a thorough authorization review. In cases where understanding a user's complete authorization scope (including indirect role assignments) is necessary, keeping this setting disabled ensures that no assignment is overlooked.

## Context:
The parameter `AuthorizationCertificationHideIndirectRoleAssisgment` is part of a broader set of security settings aimed at enhancing the manageability and clarity of the authorization process within applications leveraged by PathlockGRC software. As roles and responsibilities within an organization evolve, managing how access is granted, either directly or indirectly, becomes crucial for maintaining security and compliance. This parameter provides flexibility in how the certification process can be tailored to meet organizational needs.