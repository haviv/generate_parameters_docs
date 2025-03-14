# `AuthorizationCertificationDeltaEnforceForPositionChange` Parameter Documentation

## Category:
Security Configuration

## Default Value:
True

## Impact Level:
High

## Description:
This parameter determines whether the authorization certification process should enforce a re-certification (hence not perform a delta certification) for users whose position within the company has changed since the last certification cycle. A delta certification only reviews permissions that have changed since the last full certification.

## Business Impact:
Enabling this setting ensures that employees who have transitioned to new roles or responsibilities undergo a full certification of their access rights, reducing the risk of retaining access that is no longer appropriate for their new position. This is crucial for maintaining the principle of least privilege and complying with internal and external audit requirements.

## Technical Impact when configured:
When enabled, the system checks if an employee's position has changed since the last authorization certification period. If a position change is detected, the system will bypass delta certification (which only considers changes since the last review) and will enforce a full certification review for the affected user, ensuring their access rights are fully vetted against their new role requirements.

## Examples Scenario:
- **Without Position Change**: If a user's position has not changed since the last authorization review and this parameter is set to True, the system may perform a delta review for that user, focusing only on what has changed.
  
- **With Position Change**: Conversely, if a user has changed positions since the last authorization review and this parameter is True, the system will require a full review of the user's access permissions, ignoring the delta and ensuring comprehensive oversight of their access rights in light of their new position.

## Related Settings:
- `DeltaSinceAuthorizationReviewId`
- Settings related to authorization review cycles and criteria for delta versus full reviews.

## Best Practices:
- **Configure when**: Position changes within the organization are common, and the risk of inappropriate access due to role changes is a concern.
- **Avoid when**: The organization has a very stable employee role environment, or the system cannot accurately track and process the change in positions due to limitations in the HR system integration.

## Context:
The `AuthorizationCertificationDeltaEnforceForPositionChange` parameter is a crucial security control within access governance frameworks, particularly for organizations with dynamic role environments or those subject to stringent compliance mandates relating to user access rights management.