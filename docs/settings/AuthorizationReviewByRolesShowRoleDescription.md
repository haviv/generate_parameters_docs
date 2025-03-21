# Authorization Review By Roles Show Role Description

**Technical Name:** AuthorizationReviewByRolesShowRoleDescription

**Category:** User Management

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of role descriptions in the Authorization Review process within the Pathlock Cloud GRC platform. When enabled, it allows for a more detailed review by displaying the descriptions associated with each role during the authorization certification process.

**Business Impact:**

Enabling this feature can significantly aid in the understanding of roles during review processes, leading to more informed decision-making. It enhances the reviewer's ability to assess the appropriateness of a role assignment to a user, which is crucial for maintaining proper access controls and adhering to regulatory compliance standards.

**Technical Impact when configured:**

When configured, this setting modifies the display behavior in the Authorization Review interfaces, specifically within the ProfileTailor application sections dealing with User Details and Authorization Certifications. It can improve the efficiency and accuracy of reviews by providing essential context about what each role entails.

**Examples Scenario:**

A company's compliance officer is conducting a periodic review of user roles within the organization's ERP system. With the AuthorizationReviewByRolesShowRoleDescription parameter enabled, they can see not just the role names but also descriptions detailing the access level and responsibilities associated with each role. This additional information enables them to quickly identify any discrepancies or inappropriate role assignments, thereby reducing the risk of unauthorized access or data breaches.

**Related Settings:** 

- CustomAuthenticationProviderUrl
- CustomAuthenticationProviderAdditionalParameter

**Best Practices:** Configure when performing detailed authorization reviews and compliance audits to ensure that all role assignments are adequately understood and justified. Avoid when simplicity is preferred during the review process or if role descriptions are not maintained up-to-date, as outdated information can lead to confusion.