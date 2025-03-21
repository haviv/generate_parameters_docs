# Authorization Review For Position Change Notify Manager

**Technical Name:** AuthorizationReviewForPositionChangeNotifyManager

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:** This parameter controls the notification process for managers in the event of an authorization review triggered by a position change. It ensures that managers are promptly informed when authorization reviews are started following changes in their team members' positions.

**Business Impact:** Streamlines the process of ensuring that access rights and permissions are accurately reflected following position changes, minimizing the risk of unauthorized access or insufficient permissions which could lead to operational inefficiencies or security breaches.

**Technical Impact when configured:** Once configured, the system automatically notifies managers when an authorization review is initiated due to a position change of their team members. This aids in maintaining transparency and allows for timely review and adjustments of access rights.

**Examples Scenario:** A team member is promoted, and their position change requires an authorization review. With this parameter configured, the manager is automatically notified of the initiated review, enabling them to take any necessary actions or follow-ups related to the review process.

**Related Settings:** 

- `AuthoirizationCertificationId` (to link the certification process with the authorization review id)
- `StartAuthoriztaionReviewBasedOnTemplate` (workflow action that initiates the authorization review process)

**Best Practices:** configure when position changes are a common occurrence within your organization to ensure management is always informed and can act accordingly. Avoid configuring this notification if your organization has a flat structure or changes in positions do not frequently result in significant changes in authorization criteria.