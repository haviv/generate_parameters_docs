# Campaigns Review Details Tab UAR History

**Technical Name:** CampaignsReviewDetailsTabUARHistory

**Category:** User Management

**Default Value:** True

**Impact Level:** Medium

**Description:**

This parameter controls the visibility and functionality related to the User Access Review (UAR) history within the Campaigns Review Details tab. When enabled, it allows users to view and audit historical UAR activities directly from within the campaign's review interface.

**Business Impact:**

Enabling this feature enhances transparency and accountability in the access review process by providing a clear, auditable history of all UAR activities. It supports compliance efforts by ensuring that all user access changes and review activities are recorded and easily accessible for future audits.

**Technical Impact when configured:**

When enabled, the parameter activates the UAR history tab within the Campaigns Review Details, making it possible for reviewers and auditors to see past user access reviews. This can include changes in access levels, reviewer comments, and approval or denial of access rights. The presence of a comprehensive UAR history aids in understanding the context of user access rights over time.

**Examples Scenario:**

A compliance officer needs to audit the history of access reviews for a particular user to ensure that all changes in access levels have been appropriately approved and documented. By enabling the CampaignsReviewDetailsTabUARHistory feature, they can quickly navigate to the specific campaign, access the UAR history, and verify the complete trail of review decisions, comments, and adjustments made over the review period.

**Related Settings:**

- CampaignsReviewDetailsTabUAR
- CampaignsReviewDetailsTabUARUsage

**Best Practices:** configure when comprehensive audit trails of user access reviews are necessary for compliance purposes; avoid when minimal UI clutter and system performance are prioritized over detailed access review history logging.