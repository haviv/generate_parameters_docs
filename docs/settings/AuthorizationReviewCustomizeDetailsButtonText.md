# Authorization Review Customize Details Button Text

**Technical Name:** AuthorizationReviewCustomizeDetailsButtonText

**Category:** Configuration

**Default Value:** Not specified

**Impact Level:** Medium

**Description:**

This parameter allows for the customization of the text displayed on the details button within the authorization review process. It enables organizations to tailor the user interface to better align with internal terminologies or languages, making the authorization review process more intuitive for users.

**Business Impact:**

Customizing the button text can enhance user understanding and interaction with the authorization review module, leading to a more efficient review process. This customization can especially benefit organizations with specific terminology for roles, departments, or job titles, or those operating in a multi-lingual environment.

**Technical Impact when configured:**

When configured, the text for the details button in the authorization review screens is changed according to the specified value. This change affects all instances of the authorization review process across the application, providing a consistent user experience that aligns with the organization's needs.

**Example Scenario:**

For a multinational company with operations in France, changing the default text to "Voir les détails" can make the tool more accessible and user-friendly for French-speaking reviewers, potentially increasing engagement and the accuracy of reviews.

**Related Settings:**

- AuthorizationReviewWideApproval_ShowJobTitle
- AuthorizationReviewWideApproval_ShowActivityGroup
- AuthorizationReviewWideApproval_ShowApplicationArea
- AuthorizationReviewWideApproval_ShowDeptLevel5

**Best Practices:** configure when you need to align the application terminology with your organization's specific language or when you aim to improve the clarity and accessibility of the authorization review process for non-English speakers. Avoid customization that could confuse users or detract from the standard usability of the application.