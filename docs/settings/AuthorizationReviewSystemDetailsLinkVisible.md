# Authorization Review System Details Link Visible

**Technical Name:** AuthorizationReviewSystemDetailsLinkVisible

**Category:** Authorization Review

**Default Value:**

**Impact Level:** Medium

**Description:**

The Authorization Review System Details Link Visible parameter controls the visibility of a system-generated link within the Authorization Review workflow. This link directs users to detailed information or actions related to the authorization being reviewed.

**Business Impact:**

Enabling this parameter enhances the transparency and traceability of authorization review processes by providing easy access to comprehensive role or permission details. This is crucial for understanding the scope and implications of the authorizations under review, thereby supporting informed decision-making.

**Technical Impact when configured:**

When enabled, users participating in the authorization review process will see a clickable link leading to detailed information about the authorization item being reviewed. This could include historical data, role definitions, or the impact of the authorization on the business process. Conversely, disabling this parameter may streamline the review interface but at the expense of readily available detailed context.

**Examples Scenario:**

A security administrator conducting an annual review of user roles and permissions could utilize the detailed link to inspect the historical approval and usage of a specific role. This empowers the administrator to make an informed decision about revoking, maintaining, or adjusting the permissions associated with the role based on past and current business needs.

**Related Settings:**

- AuthorizationReviewShowSaveAndApprove

**Best Practices:** 

- **Configure when:** Additional context or historical information is necessary to make informed decisions during authorization reviews.
- **Avoid when:** Minimizing interface complexity and decision-making time is prioritized over detailed context availability.