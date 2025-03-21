**Authorization Review Show User Type**

**Technical Name:** AuthorizationReviewShowUserType

**Category:** User Management

**Default Value:** False

**Impact Level:** Medium

**Description:**

This parameter controls whether to display advanced user details in authorization review grids. When enabled, it allows for a more detailed view of user information during the authorization review process.

**Business Impact:**

Enabling this feature impacts the visibility of user details during authorization reviews, potentially enhancing the security and compliance oversight by allowing for a finer-grained review of user permissions and roles.

**Technical Impact when configured:**

When enabled, additional user-related columns are added to the grid views within the authorization certification process. This may include but is not limited to, user roles, permissions, and other relevant user attributes.

**Examples Scenario:**

- **Enhancing Review Processes:** A compliance officer requires detailed information about user types and their respective access levels across different departments for a comprehensive audit. Enabling this setting will facilitate a more detailed data presentation, aiding in identifying potential compliance risks or access anomalies.
  
**Related Settings:**

- AuthorizationReviewShowBasicUserDetails

**Best Practices:** 

- **Configure when:** Detailed user information is essential for in-depth authorization reviews, such as during audits or compliance checks.
- **Avoid when:** Minimal detail sufficiency for authorization reviews or when the additional information could clutter the interface unnecessarily, impacting usability.