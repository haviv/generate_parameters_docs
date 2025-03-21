# Authorization Review Wide Approval Show Activity Group

**Technical Name:** AuthorizationReviewWideApproval_ShowActivityGroup

**Category:** Workflow

**Default Value:**

**Impact Level:** Medium

**Description:**

This parameter controls the visibility of activity group information in the authorization review process. It determines whether detailed activity or role-based information is displayed alongside the approval workflow, enhancing the decision-making context for authorizers.

**Business Impact:**

Enabling this feature provides reviewers with a broader context, making the approval process more efficient and informed. It aids in reducing the risk of unauthorized or inappropriate access being granted, by ensuring a clear understanding of the activities or roles under review.

**Technical Impact when configured:**

When enabled, this parameter ensures that activity group details are available to users involved in the authorization review process, leading to more accurate and faster decision-making. Conversely, disabling it simplifies the approval interface but may omit potentially crucial information needed for informed approvals.

**Examples Scenario:**

- A company implements the Authorization Review Wide Approval Show Activity Group feature to improve the granularity and context of information available during the review process of user roles and permissions, thereby enhancing the security posture and compliance with internal and external audit requirements.

**Related Settings:**

- DatabaseProviderType_Custom
- MarkRfcBackgroundTasksWithPrefix

**Best Practices:** configure when you need to increase the visibility and understanding of activities or roles during the authorization process, avoid when simplicity and speed in the approval process are preferred over detailed context.