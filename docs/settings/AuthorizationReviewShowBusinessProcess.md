# Authorization Review Show Business Process

**Technical Name:** AuthorizationReviewShowBusinessProcess

**Category:** Authorization Review

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of business process information during authorization reviews within the Pathlock Cloud GRC platform. When enabled, users are able to view and consider associated business processes during review processes, providing a more comprehensive understanding of authorization contexts.

**Business Impact:**

Enabling this setting enhances the decision-making process during authorization reviews by providing additional business process context. This leads to more informed and secure authorization decisions, reducing the risk of inappropriate access and enhancing compliance with internal and external regulations.

**Technical Impact when configured:**

When configured, the system will display relevant business process information alongside authorization details in review screens. This assists reviewers in understanding the full impact of the authorizations under review, including how they relate to business operations.

**Examples Scenario:**

A financial institution implements the AuthorizationReviewShowBusinessProcess parameter to ensure that during authorization reviews, approvers can see not only the roles and permissions requested but also the business processes those permissions impact. This visibility helps to prevent unauthorized access to sensitive financial operations and ensures compliance with financial regulations.

**Related Settings:**

- `AuthorizationReviewPositionChangeNotificationHeader`
- `AuthorizationReviewShowPartialApprovalIcon`
- `AuthorizationReviewShowPartialApprovalText`

**Best Practices:** Configure this setting to enhance visibility and control over business processes during authorization reviews. Avoid enabling this setting if your organization does not require detailed business process visibility for authorization decisions, to streamline the review interface.