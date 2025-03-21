# Authorization Review Position Change Notification Header

**Technical Name:** AuthorizationReviewPositionChangeNotificationHeader

**Category:** Workflow

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether notifications for position changes during an authorization review process are visible. It is a configuration setting that enhances the management of user permissions by notifying relevant personnel about changes in user positions, which may affect their authorizations.

**Business Impact:**

Enabling this feature ensures that managers and compliance officers are aware of changes in user positions, which may necessitate a review of access permissions. This is crucial for maintaining security and compliance within the organization, as it helps to prevent unauthorized access to sensitive information.

**Technical Impact when configured:**

- Notifications are generated for position changes during the authorization review process.
- Enhances visibility and oversight over changes that could impact security and compliance.
- Allows for timely adjustments to user permissions, ensuring they align with their new roles.

**Examples Scenario:**

Suppose a user is promoted from a junior analyst to a senior analyst within the company. If this parameter is enabled, a notification will be sent to the relevant stakeholders, indicating the user's position change. This notification prompts a review of the user's access permissions to ensure they align with the responsibilities of the new position, thereby maintaining the integrity of the access privileges within the company systems.

**Related Settings:** 

- `AuthorizationReviewTakeFullNameFromUserRecord`: This setting, when enabled, affects how user names are displayed in notifications by including the full name from the user record.

**Best Practices:** 

- Configure when: It is essential to have tight control over permissions and maintain compliance with internal and regulatory standards. Especially useful in large organizations where roles and responsibilities frequently change.
  
- Avoid when: In smaller organizations with stable roles or where position changes do not significantly impact access permissions, or in environments where notification overload is a concern.