# Authorization Review Icon As Link

**Technical Name:** AuthorizationReviewIconAsLink

**Category:** Compliance

**Default Value:** False

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewIconAsLink` parameter controls the visibility and functionality of an icon that, when enabled, links directly to the Pathlock GRC portal for detailed authorization review processes. This feature aims to streamline the process of reviewing and managing authorizations by providing a direct link from notifications or profiles to the relevant section of the GRC platform.

**Business Impact:**

Enabling the Authorization Review Icon as a link enhances operational efficiency and compliance oversight by allowing managers and authorized personnel immediate access to authorization reviews. This can significantly expedite the review process, directly impacting the organization's ability to maintain compliance with various regulatory requirements and internal security policies.

**Technical Impact when configured:**

When configured to `True`, the Authorization Review Icon appears as a clickable link within the applicable interfaces, such as email notifications or user profiles. Clicking this link redirects the user to the specific authorization review page on the Pathlock GRC platform, simplifying the review and approval process by eliminating the need to navigate through the platform manually.

**Example Scenario:**

Consider a situation where a manager receives a notification about a position change that requires authorization review. With the `AuthorizationReviewIconAsLink` enabled, the manager can directly click on the icon/link provided in the notification to access the authorization review page for the specific case. This direct access saves time and reduces the steps required for review, enabling a quicker response to compliance and security tasks.

**Related Settings:**

- AuthorizationReviewDisableWideApproval
- AuthorizationReviewLinkToPortalVisible

**Best Practices:** 

Configure this parameter to `True` to streamline authorization reviews for positions of responsibility. Avoid enabling this link in scenarios where direct access may compromise the security or integrity of the authorization review process, such as in highly restricted or sensitive environments.