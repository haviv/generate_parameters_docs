**Technical Name:** AuthorizationReviewShowSubmitOnlyHandledItems

**Category:** Workflow

**Default Value:** True

**Impact Level:** Medium

**Description:**

This setting controls the visibility of handled items submission options within the Authorization Review process. When enabled, users are required to review and submit only those items they have handled, simplifying the review process by focusing the user's attention on relevant items.

**Business Impact:**

Implementing this setting streamlines the authorization review process, improving compliance and oversight within the organizational GRC framework. It ensures a focused and efficient review process by reducing clutter and potential confusion, leading to a more effective and timely completion of reviews.

**Technical Impact when configured:**

When enabled, this setting will filter the Authorization Review interface to display only items that have been acted upon (handled) by the reviewer. This results in a more streamlined and focused user experience, allowing users to concentrate on finalizing their reviews without the distraction of unhandled items.

**Examples Scenario:**

- **Scenario:** An organization is undergoing an internal compliance audit and must ensure that all access rights are appropriately reviewed. The Authorization Review Show Submit Only Handled Items setting is enabled to ensure that reviewers concentrate on items requiring their attention, thus improving the audit's efficiency and effectiveness.

**Related Settings:**

- AuthorizationReviewPageSize

**Best Practices:** 

- **Configure when:** there is a need to streamline the authorization review process, improve compliance, and ensure users are not overwhelmed by the volume of items requiring review.
- **Avoid when:** the review process requires visibility of all items, including those not directly handled by the reviewer, to provide a comprehensive overview of all available items for audit or training purposes.