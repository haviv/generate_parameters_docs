# Authorization Review Position Change Notification Visible

**Technical Name:** AuthorizationReviewPositionChangeNotificationVisible

**Category:** Authorization Review

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of notifications related to changes in position during the authorization review process within the Pathlock Cloud GRC platform.

**Business Impact:**

Enabling this feature assists in maintaining real-time oversight and ensures relevant stakeholders are informed about critical changes in user positions, which may affect access rights and compliance status.

**Technical Impact when configured:**

When enabled, it triggers notifications to be sent out to designated recipients whenever there are changes in user positions. This can aid in timely review and adjustment of permissions, helping to prevent unauthorized access or compliance breaches.

**Examples Scenario:**

A company utilizes the Pathlock platform for managing GRC. The company has strict compliance requirements that necessitate immediate action when an employee's position changes, potentially altering their access needs. By enabling this parameter, the system automatically alerts the compliance team, allowing for a swift review and adjustment of the employee's access rights, thereby maintaining security and compliance.

**Related Settings:**

- EnableCustomActionForAuthorizationReviewRemoveAuthorization
- AuthorizationReviewLinkToPortalVisible

**Best Practices:** 

- **configure when:** Immediate notification of position changes is critical for compliance and access management.
- **avoid when:** The organization does not require instant updates on position changes or if it could lead to notification fatigue.