# Authorization Review Disable Session For Waiting Items

**Technical Name:** AuthorizationReviewDisableSessionForWaitingItems

**Category:** Configuration

**Default Value:**

**Impact Level:** Medium

**Description:**

The `AuthorizationReviewDisableSessionForWaitingItems` parameter is designed to control the behavior of user sessions during the authorization review process. Specifically, it determines whether a user's session should be disabled for items that are marked as waiting in the authorization certification process.

**Business Impact:**

This parameter directly influences the efficiency and flow of authorization reviews within an organization. By enabling this setting, reviewers can ensure that users do not have active sessions for items under review, thereby maintaining the integrity of the review process. It is particularly relevant for compliance and security purposes, ensuring that no unauthorized actions are taken while items are under review.

**Technical Impact: when configured**

When this parameter is configured to disable user sessions for waiting items, it adds an additional layer of control during the review process. This can prevent unauthorized access or changes to sensitive information or settings, thereby enhancing the overall security posture during the authorization certification process.

**Examples Scenario:**

Imagine a scenario where an employee's access rights to a critical financial application are under review due to suspected misuse. With the `AuthorizationReviewDisableSessionForWaitingItems` parameter set to disable sessions for waiting items, the employee will not be able to access the application until the review is completed and their access is either approved or revoked. This prevents potential further misuse during the review period.

**Related Settings:**

- WorkflowRisksDisableFilterBySchemaOwner
- WorkflowTypeUploadOverwrite

**Best Practices:** configure when, avoid when

- **Configure when:** It's crucial to ensure compliance and security during the authorization review process. Enabling this parameter is particularly beneficial in environments where strict control over user sessions is necessary to prevent unauthorized actions.
  
- **Avoid when:** If the review process does not require stringent controls over user sessions or if disabling sessions could unduly hinder business operations. For example, in environments where access reviews are frequent and the disabling of sessions could significantly impact user productivity or system usability.