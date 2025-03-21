# Authorization Review Show Fill Empty To Decline

**Technical Name:** AuthorizationReviewShowFillEmptyToDecline

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewShowFillEmptyToDecline` parameter controls whether users in the authorization review process are shown an option to fill in empty fields automatically with a decline response. This feature aims to streamline the review process, particularly in scenarios where numerous entries are left blank and can be considered as implicitly declined by the reviewer.

**Business Impact:**

Enabling this feature may significantly expedite the authorization review process, reducing the manual effort required by reviewers. It can lead to faster compliance with internal policies and external regulations by ensuring that every action or access request is either approved or explicitly declined, leaving no entries without a decision. This setting impacts the efficiency of the authorization review process and adherence to policy enforcement, potentially affecting audit outcomes.

**Technical Impact when configured:**

When enabled, this setting impacts the user interface by presenting an additional option or button within the authorization review sections of the Pathlock Cloud GRC platform. This option, when utilized by a reviewer, automatically marks all empty fields as "Decline" without the need for manual entry, which in turn can speed up the process of completing reviews, especially within large datasets.

**Examples Scenario:**

A compliance officer overseeing the quarterly access review for enterprise applications enables this feature to streamline the review process. During the review, the officer encounters numerous access rights not applicable or no longer needed by users. Instead of manually declining each empty field, the officer uses the option provided by `AuthorizationReviewShowFillEmptyToDecline` to automatically decline all undecided requests, thus ensuring compliance and efficiency.

**Related Settings:**

- TestConnectionBeforeEmergencyAccessCompletion

**Best Practices:** configure when the review process is known to contain numerous items that typically would be declined or when looking to streamline the review process greatly. Avoid when individual review of each item is necessary, or when automatic declining of items could overlook necessary approvals.