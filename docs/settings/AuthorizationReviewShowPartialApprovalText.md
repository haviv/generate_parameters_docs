# Authorization Review Show Partial Approval Text

**Technical Name:** AuthorizationReviewShowPartialApprovalText

**Category:** Workflow

**Default Value:** 

**Impact Level:** Medium

**Description:**

The AuthorizationReviewShowPartialApprovalText parameter determines whether text related to partial approvals in authorization reviews is displayed in the Pathlock Cloud GRC platform. This parameter affects the presentation layer of authorization certifications, enhancing user understanding of the certification process status.

**Business Impact:**

Enabling this parameter can provide additional clarity during the review process by making the status of partial approvals visible. This can help decision-makers and reviewers to accurately assess the progress and completeness of authorization reviews, resulting in more informed and nuanced decision-making.

**Technical Impact when configured:**

When this parameter is configured to show partial approval text, users involved in the authorization certification process will see detailed statuses regarding approvals. This can lead to an improved workflow as users have clearer information on which actions are required to move certifications forward.

**Examples Scenario:**

- A manager is reviewing user permissions as part of a quarterly access review. When the AuthorizationReviewShowPartialApprovalText is enabled, they can quickly identify which permissions have been partially approved and require further action, thus streamlining the certification process.

**Related Settings:**

- AuthorizationReviewPositionChangeNotificationYear

**Best Practices:** 

- Configure when transparency and detailed tracking of the certification process is necessary.
- Avoid when simplicity in the approval process display is preferred, or if the additional information may confuse the reviewers.