# Authorization Review Position Change Notification Text

**Technical Name:** AuthorizationReviewPositionChangeNotificationText

**Category:** Workflow

**Default Value:** N/A

**Impact Level:** Medium

**Description:**

The Authorization Review Position Change Notification Text parameter is used to specify the custom message or notification text sent during the authorization review process when there are changes in positions or roles within the organization's structure as detected by the Pathlock Cloud GRC platform. It is a pivotal component in ensuring that all stakeholders are promptly and accurately informed about modifications that could affect access rights or compliance postures.

**Business Impact:**

Configuring this parameter with a clear and informative message enhances communication and awareness during authorization reviews, helping to maintain a secure and compliant environment. It directly influences how changes in roles or permissions are perceived and acted upon by the involved parties, aiding in smoother transitions and reducing the risk of unauthorized access or compliance violations.

**Technical Impact when configured:**

- Ensures stakeholders are kept informed about changes in authorization that might impact security or compliance.
- Supports transparency and accountability in the access review and management processes.
- Facilitates quicker response actions from recipients due to clear understanding conveyed by the customized notification text.

**Examples Scenario:**

- **Before Role Change**: Employees and their managers receive generic notifications about pending authorization reviews, leading to confusion and delays in the review process.
- **After Configuring AuthorizationReviewPositionChangeNotificationText**: A customized notification text is sent stating, "Notice of Position Role Change: Your role privileges are under review due to recent organizational changes. Please review the attached details and provide necessary acknowledgments by [Date].", leading to increased awareness and efficiency in completing the authorization review process.

**Related Settings:** 

- AuthorizationReviewPositionChangeNotificationVisible
- AuthorizationReviewPositionChangeNotificationYear

**Best Practices:** 

- **Configure when**: Any changes to roles or permissions are frequent within the organization to ensure stakeholders are appropriately informed.
  
- **Avoid when**: The organization has a static structure with rare changes to roles or permissions, or if automated alerts could cause unnecessary alarm or confusion due to their frequency or content nature.