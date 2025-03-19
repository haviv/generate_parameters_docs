**Authorization Certification Hide Indirect Role Assignment**

**Technical Name:** AuthorizationCertificationHideIndirectRoleAssisgment

**Category:** Configuration

**Default Value:** Not Specified

**Impact Level:** Medium

**Description:** This parameter controls the visibility of indirect role assignments during the authorization certification process within the Pathlock Cloud GRC platform. When enabled, it hides the roles that are assigned to a user indirectly through their organizational structure or inherited permissions.

**Business Impact:** Enabling this setting can streamline the certification process by focusing reviewers on direct role assignments, potentially reducing complexity and the time required for certification. However, it may also lead to overlooked risks associated with indirect roles if not carefully managed.

**Technical Impact when configured:** When enabled, the system filters out indirect role assignments from the certification review interface. This can simplify the review process but requires that reviewers have a clear understanding of the implications of indirect roles on access permissions.

**Examples Scenario:** In a scenario where an employee has been granted access to sensitive financial records both directly, through explicit role assignment, and indirectly, through inheritance from a departmental role, activating this parameter would hide the indirect role assignments during certification. This could be beneficial in focusing the review on direct access permissions, but may require separate consideration of indirect permissions for a comprehensive security posture.

**Related Settings:** 
- `AuthorizationReviewByRolesShowNumberOfActivities`

**Best Practices:** configure when the certification process needs streamlining and the implications of indirect roles are well-understood and managed through other means; avoid when full visibility of both direct and indirect role assignments is crucial for maintaining security and compliance.